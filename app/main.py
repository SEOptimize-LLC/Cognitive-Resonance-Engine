"""
Cognitive Resonance Engine - Main Application
=============================================
Streamlit-based audience research platform.
"""

import streamlit as st
from typing import Optional

from app.config import (
    APP_CONFIG,
    AVAILABLE_MODELS,
    ANALYSIS_MODELS,
    INDUSTRIES,
    BUSINESS_MODELS,
    DEFAULT_ANALYSIS_MODEL,
    PIPELINE_STAGES
)
from app.models.research_models import (
    ClientInput,
    BusinessModelType,
    ResearchResults,
    SessionState
)
from app.llm.openrouter_client import OpenRouterClient, CostTracker
from app.core.orchestrator import ResearchOrchestrator


# ===== Page Configuration =====

st.set_page_config(
    page_title=APP_CONFIG["app_name"],
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ===== Session State Initialization =====

def init_session_state():
    """Initialize session state variables."""
    if "session" not in st.session_state:
        st.session_state.session = SessionState()
    if "cost_tracker" not in st.session_state:
        st.session_state.cost_tracker = CostTracker()
    if "results" not in st.session_state:
        st.session_state.results = None
    if "is_running" not in st.session_state:
        st.session_state.is_running = False
    if "current_stage" not in st.session_state:
        st.session_state.current_stage = None
    if "stage_outputs" not in st.session_state:
        st.session_state.stage_outputs = {}


# ===== Sidebar =====

def render_sidebar():
    """Render the sidebar with model selection and settings."""
    with st.sidebar:
        st.image(
            "https://img.icons8.com/fluency/96/brain.png",
            width=80
        )
        st.title("Settings")
        
        st.markdown("---")
        
        # Model Selection
        st.subheader("🤖 Analysis Model")
        
        model_options = list(ANALYSIS_MODELS.keys())
        model_names = [ANALYSIS_MODELS[m].name for m in model_options]
        
        selected_idx = model_options.index(DEFAULT_ANALYSIS_MODEL) \
            if DEFAULT_ANALYSIS_MODEL in model_options else 0
        
        selected_model = st.selectbox(
            "Select model for analysis:",
            options=model_options,
            format_func=lambda x: ANALYSIS_MODELS[x].name,
            index=selected_idx,
            help="Perplexity Sonar is always used for research. "
                 "This model is used for analysis."
        )
        
        # Show model info
        model_config = ANALYSIS_MODELS[selected_model]
        st.caption(f"*{model_config.description}*")
        st.caption(
            f"Cost: ${model_config.input_price_per_million}/M input, "
            f"${model_config.output_price_per_million}/M output"
        )
        
        st.markdown("---")
        
        # Number of ICPs
        st.subheader("👥 ICP Settings")
        num_icps = st.slider(
            "Number of ICPs to generate:",
            min_value=APP_CONFIG["min_icps"],
            max_value=APP_CONFIG["max_icps"],
            value=APP_CONFIG["default_num_icps"],
            help="Generate 2-5 Ideal Customer Profiles"
        )
        
        st.markdown("---")
        
        # Cost Summary
        if st.session_state.cost_tracker.usage_log:
            st.subheader("💰 Cost Summary")
            summary = st.session_state.cost_tracker.get_summary()
            st.metric(
                "Total Cost",
                f"${summary['total_cost']:.4f}"
            )
            st.metric(
                "Total Tokens",
                f"{summary['total_tokens']['total']:,}"
            )
            
            with st.expander("Breakdown by Model"):
                for model, data in summary['by_model'].items():
                    short_name = model.split('/')[-1]
                    st.write(f"**{short_name}**")
                    st.write(f"  - Requests: {data['requests']}")
                    st.write(f"  - Tokens: {data['total_tokens']:,}")
                    st.write(f"  - Cost: ${data['cost']:.4f}")
        
        st.markdown("---")
        
        # Reset Button
        if st.button("🔄 Reset Session", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        
        return selected_model, num_icps


# ===== Input Form =====

def render_input_form(num_icps: int) -> Optional[ClientInput]:
    """Render the client input form."""
    
    st.header("📋 Client Information")
    st.markdown(
        "Enter information about the client to begin the audience research."
    )
    
    with st.form("client_input_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            client_name = st.text_input(
                "Company/Brand Name *",
                placeholder="e.g., Acme Corporation"
            )
            
            website_url = st.text_input(
                "Website URL *",
                placeholder="https://www.example.com"
            )
            
            about_page_url = st.text_input(
                "About Page URL",
                placeholder="https://www.example.com/about"
            )
            
            products_url = st.text_input(
                "Products/Services Page URL",
                placeholder="https://www.example.com/products"
            )
        
        with col2:
            industry = st.selectbox(
                "Industry *",
                options=[""] + INDUSTRIES,
                index=0
            )
            
            business_model = st.radio(
                "Business Model *",
                options=BUSINESS_MODELS,
                horizontal=True
            )
            
            target_market = st.text_input(
                "Target Market (optional)",
                placeholder="e.g., North America, SMBs"
            )
            
            known_competitors = st.text_area(
                "Known Competitors (optional)",
                placeholder="List competitor names or URLs",
                height=80
            )
        
        additional_context = st.text_area(
            "Additional Context (optional)",
            placeholder="Any other relevant information...",
            height=100
        )
        
        additional_urls = st.text_area(
            "Additional URLs (optional, one per line)",
            placeholder="https://www.example.com/case-studies\n"
                       "https://www.example.com/team",
            height=80
        )
        
        submitted = st.form_submit_button(
            "🚀 Start Research",
            use_container_width=True,
            type="primary"
        )
        
        if submitted:
            # Validation
            errors = []
            if not client_name:
                errors.append("Company name is required")
            if not website_url:
                errors.append("Website URL is required")
            if not industry:
                errors.append("Industry is required")
            
            if errors:
                for error in errors:
                    st.error(error)
                return None
            
            # Parse business model
            bm_map = {
                "B2B (Business to Business)": BusinessModelType.B2B,
                "B2C (Business to Consumer)": BusinessModelType.B2C,
                "Both B2B and B2C": BusinessModelType.BOTH
            }
            
            # Parse additional URLs
            url_list = [
                u.strip() for u in additional_urls.split('\n')
                if u.strip()
            ]
            
            return ClientInput(
                client_name=client_name,
                website_url=website_url,
                about_page_url=about_page_url or None,
                products_services_url=products_url or None,
                additional_urls=url_list,
                industry=industry,
                business_model=bm_map[business_model],
                target_market=target_market or None,
                known_competitors=known_competitors or None,
                additional_context=additional_context or None,
                num_icps=num_icps
            )
    
    return None


# ===== Progress Display =====

def render_progress():
    """Render the research progress."""
    if not st.session_state.is_running:
        return
    
    st.header("🔄 Research in Progress")
    
    progress_container = st.container()
    
    with progress_container:
        for stage in PIPELINE_STAGES:
            stage_id = stage["id"]
            status = st.session_state.stage_outputs.get(stage_id, {}).get(
                "status", "pending"
            )
            
            if status == "running":
                st.info(f"⏳ {stage['name']}: {stage['description']}...")
            elif status == "complete":
                st.success(f"✅ {stage['name']}: Complete")
            elif status == "error":
                error_msg = st.session_state.stage_outputs[stage_id].get(
                    "error", "Unknown error"
                )
                st.error(f"❌ {stage['name']}: {error_msg}")
            else:
                st.write(f"⬜ {stage['name']}: Pending")


# ===== Results Display =====

def render_results():
    """Render the research results."""
    results: ResearchResults = st.session_state.results
    
    if not results:
        return
    
    st.header("📊 Research Results")
    
    # Tabs for different sections
    tabs = st.tabs([
        "🏢 Company Profile",
        "👥 ICPs",
        "💎 Value Propositions",
        "😰 Pain Points",
        "🗺️ Journey Maps",
        "📥 Export"
    ])
    
    # Company Profile Tab
    with tabs[0]:
        if results.company_profile:
            profile = results.company_profile
            st.subheader(profile.name)
            st.write(f"**Industry:** {profile.industry}")
            st.write(f"**Business Model:** {profile.business_model.value}")
            
            st.markdown("### Overview")
            st.write(profile.overview)
            
            if profile.products_services:
                st.markdown("### Products & Services")
                for ps in profile.products_services:
                    with st.expander(ps.name):
                        st.write(ps.description)
                        if ps.features:
                            st.write("**Features:**")
                            for f in ps.features:
                                st.write(f"- {f}")
            
            if profile.stated_value_propositions:
                st.markdown("### Stated Value Propositions")
                for vp in profile.stated_value_propositions:
                    st.write(f"- {vp}")
            
            if profile.competitors:
                st.markdown("### Competitors")
                for comp in profile.competitors:
                    st.write(f"- **{comp.name}**: {comp.description or ''}")
    
    # ICPs Tab
    with tabs[1]:
        if results.icps:
            for icp_result in results.icps:
                icp = icp_result.icp
                with st.expander(
                    f"👤 {icp.icp_name} ({icp.segment_priority})",
                    expanded=True
                ):
                    st.write(f"*{icp.one_liner}*")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("**Demographics**")
                        if icp.demographics.company_size:
                            st.write(
                                f"Company Size: {icp.demographics.company_size}"
                            )
                        if icp.demographics.job_titles:
                            st.write(
                                f"Job Titles: {', '.join(icp.demographics.job_titles)}"
                            )
                        if icp.demographics.industry_verticals:
                            st.write(
                                f"Industries: "
                                f"{', '.join(icp.demographics.industry_verticals)}"
                            )
                    
                    with col2:
                        st.markdown("**Psychographics**")
                        if icp.psychographics.decision_style:
                            st.write(
                                f"Decision Style: "
                                f"{icp.psychographics.decision_style.value}"
                            )
                        if icp.psychographics.risk_tolerance:
                            st.write(
                                f"Risk Tolerance: "
                                f"{icp.psychographics.risk_tolerance.value}"
                            )
                        if icp.psychographics.core_values:
                            st.write(
                                f"Values: "
                                f"{', '.join(icp.psychographics.core_values[:3])}"
                            )
                    
                    if icp.motivations:
                        st.markdown("**Top Motivations**")
                        for m in icp.motivations[:3]:
                            st.write(f"- {m.statement}")
                    
                    if icp.pain_points:
                        st.markdown("**Top Pain Points**")
                        for p in icp.pain_points[:3]:
                            st.write(f"- {p.statement} (Severity: {p.severity}/10)")
                    
                    if icp.detailed_narrative:
                        st.markdown("**Detailed Profile**")
                        st.write(icp.detailed_narrative)
    
    # Value Propositions Tab
    with tabs[2]:
        if results.icps:
            for icp_result in results.icps:
                if icp_result.value_proposition:
                    vp = icp_result.value_proposition
                    with st.expander(
                        f"💎 VP for {icp_result.icp.icp_name}",
                        expanded=True
                    ):
                        if vp.value_proposition_statement:
                            st.info(vp.value_proposition_statement)
                        
                        if vp.fit_score:
                            st.metric("Fit Score", f"{vp.fit_score}/100")
                        
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.markdown("**Pain Relievers**")
                            for pr in vp.pain_relievers[:5]:
                                st.write(
                                    f"- **{pr.pain_addressed}**: {pr.how_relieved}"
                                )
                        
                        with col2:
                            st.markdown("**Gain Creators**")
                            for gc in vp.gain_creators[:5]:
                                st.write(
                                    f"- **{gc.gain_created}**: {gc.how_created}"
                                )
                        
                        if vp.unique_differentiators:
                            st.markdown("**Unique Differentiators**")
                            for d in vp.unique_differentiators:
                                st.write(f"- {d}")
    
    # Pain Points Tab
    with tabs[3]:
        if results.icps:
            for icp_result in results.icps:
                if icp_result.pain_taxonomy:
                    pt = icp_result.pain_taxonomy
                    with st.expander(
                        f"😰 Pain Points for {icp_result.icp.icp_name}",
                        expanded=True
                    ):
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.markdown("**Functional Pains**")
                            for p in pt.functional_pains[:5]:
                                st.write(
                                    f"- {p.statement} "
                                    f"({p.severity}/10)"
                                )
                        
                        with col2:
                            st.markdown("**Financial Pains**")
                            for p in pt.financial_pains[:5]:
                                st.write(
                                    f"- {p.statement} "
                                    f"({p.severity}/10)"
                                )
                        
                        with col3:
                            st.markdown("**Emotional Pains**")
                            for p in pt.emotional_pains[:5]:
                                st.write(
                                    f"- {p.statement} "
                                    f"({p.severity}/10)"
                                )
                        
                        if pt.forces_analysis:
                            st.markdown("**Forces Analysis**")
                            fa = pt.forces_analysis
                            st.write(
                                f"Assessment: {fa.net_force_assessment}"
                            )
                            st.write(
                                f"Recommended Focus: {fa.recommended_focus}"
                            )
    
    # Journey Maps Tab
    with tabs[4]:
        if results.icps:
            for icp_result in results.icps:
                if icp_result.journey_map:
                    jm = icp_result.journey_map
                    with st.expander(
                        f"🗺️ Journey for {icp_result.icp.icp_name}",
                        expanded=True
                    ):
                        st.write(f"**Timeline:** {jm.overall_timeline}")
                        
                        stages = [
                            ("Awareness", jm.awareness_stage),
                            ("Consideration", jm.consideration_stage),
                            ("Decision", jm.decision_stage),
                            ("Onboarding", jm.onboarding_stage),
                            ("Expansion", jm.expansion_stage)
                        ]
                        
                        for stage_name, stage in stages:
                            if stage:
                                with st.container():
                                    st.markdown(f"#### {stage_name}")
                                    st.write(f"*{stage.objective}*")
                                    
                                    if stage.content_themes:
                                        st.write(
                                            f"**Themes:** "
                                            f"{', '.join(stage.content_themes[:3])}"
                                        )
                                    
                                    if stage.content_ideas[:2]:
                                        st.write("**Content Ideas:**")
                                        for idea in stage.content_ideas[:2]:
                                            st.write(
                                                f"- {idea.title} ({idea.format})"
                                            )
    
    # Export Tab
    with tabs[5]:
        st.subheader("📥 Export Results")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📄 Download Markdown", use_container_width=True):
                # Generate markdown export
                from app.export.markdown_generator import generate_markdown
                md_content = generate_markdown(results)
                st.download_button(
                    "📥 Download .md File",
                    data=md_content,
                    file_name=f"{results.client_input.client_name}_research.md",
                    mime="text/markdown"
                )
        
        with col2:
            if st.button("📝 Download DOCX", use_container_width=True):
                # Generate DOCX export
                from app.export.docx_generator import generate_docx
                docx_bytes = generate_docx(results)
                st.download_button(
                    "📥 Download .docx File",
                    data=docx_bytes,
                    file_name=f"{results.client_input.client_name}_research.docx",
                    mime="application/vnd.openxmlformats-officedocument"
                         ".wordprocessingml.document"
                )
        
        # Cost summary
        st.markdown("---")
        st.subheader("💰 Session Cost Summary")
        summary = st.session_state.cost_tracker.get_summary()
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Cost", f"${summary['total_cost']:.4f}")
        col2.metric("Input Tokens", f"{summary['total_tokens']['input']:,}")
        col3.metric("Output Tokens", f"{summary['total_tokens']['output']:,}")


# ===== Main Function =====

def main():
    """Main application entry point."""
    init_session_state()
    
    # Sidebar
    selected_model, num_icps = render_sidebar()
    
    # Header
    st.title("🧠 Cognitive Resonance Engine")
    st.markdown(
        "*AI-powered audience research and customer intelligence platform*"
    )
    st.markdown("---")
    
    # Show results if available
    if st.session_state.results:
        render_results()
        
        if st.button("🔄 Start New Research"):
            st.session_state.results = None
            st.session_state.stage_outputs = {}
            st.rerun()
    
    # Show progress if running
    elif st.session_state.is_running:
        render_progress()
    
    # Show input form
    else:
        client_input = render_input_form(num_icps)
        
        if client_input:
            # Start research
            st.session_state.is_running = True
            st.session_state.session.client_input = client_input
            
            with st.spinner("Initializing research pipeline..."):
                try:
                    # Create orchestrator
                    orchestrator = ResearchOrchestrator(
                        analysis_model=selected_model,
                        cost_tracker=st.session_state.cost_tracker
                    )
                    
                    # Run research with progress updates
                    def progress_callback(stage_id: str, status: str, data=None):
                        if stage_id not in st.session_state.stage_outputs:
                            st.session_state.stage_outputs[stage_id] = {}
                        st.session_state.stage_outputs[stage_id]["status"] = status
                        if data:
                            st.session_state.stage_outputs[stage_id]["data"] = data
                    
                    results = orchestrator.run_research(
                        client_input,
                        progress_callback=progress_callback
                    )
                    
                    st.session_state.results = results
                    st.session_state.is_running = False
                    st.rerun()
                    
                except Exception as e:
                    st.session_state.is_running = False
                    st.error(f"Research failed: {str(e)}")
                    raise e


if __name__ == "__main__":
    main()