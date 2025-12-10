"""
Cognitive Resonance Engine - Main Application
=============================================
Streamlit-based audience research platform.

Run with: streamlit run streamlit_app.py
"""

import streamlit as st
import sys
from pathlib import Path

# Add the app directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent))

from app.config import (
    APP_CONFIG,
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
from app.llm.openrouter_client import CostTracker


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
        st.title("🧠 Settings")
        
        st.markdown("---")
        
        # Model Selection
        st.subheader("🤖 Analysis Model")
        
        model_options = list(ANALYSIS_MODELS.keys())
        
        selected_idx = 0
        if DEFAULT_ANALYSIS_MODEL in model_options:
            selected_idx = model_options.index(DEFAULT_ANALYSIS_MODEL)
        
        selected_model = st.selectbox(
            "Select model for analysis:",
            options=model_options,
            format_func=lambda x: ANALYSIS_MODELS[x].name,
            index=selected_idx,
            help="Perplexity Sonar is always used for web research. "
                 "This model handles the analysis."
        )
        
        # Show model info
        model_config = ANALYSIS_MODELS[selected_model]
        st.caption(f"*{model_config.description}*")
        st.caption(
            f"💰 ${model_config.input_price_per_million}/M input, "
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
        
        # Cost Summary (only show if there's usage)
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
            
            with st.expander("📊 Breakdown by Model"):
                for model, data in summary['by_model'].items():
                    short_name = model.split('/')[-1]
                    st.write(f"**{short_name}**")
                    st.write(f"  Requests: {data['requests']}")
                    st.write(f"  Tokens: {data['total_tokens']:,}")
                    st.write(f"  Cost: ${data['cost']:.4f}")
            
            st.markdown("---")
        
        # Reset Button
        if st.button("🔄 Reset Session", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        
        # Info
        st.markdown("---")
        st.caption(f"v{APP_CONFIG['version']}")
        st.caption("Powered by OpenRouter")
        
        return selected_model, num_icps


# ===== Input Form =====

def render_input_form(num_icps: int):
    """Render the client input form."""
    
    st.header("📋 Client Information")
    st.markdown(
        "Enter information about the client to begin the audience research. "
        "Fields marked with * are required."
    )
    
    with st.form("client_input_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            client_name = st.text_input(
                "Company/Brand Name *",
                placeholder="e.g., Acme Corporation",
                help="The name of the company you're researching"
            )
            
            website_url = st.text_input(
                "Website URL *",
                placeholder="https://www.example.com",
                help="Main website URL"
            )
            
            about_page_url = st.text_input(
                "About Page URL",
                placeholder="https://www.example.com/about",
                help="Link to About Us or Company page"
            )
            
            products_url = st.text_input(
                "Products/Services Page URL",
                placeholder="https://www.example.com/products",
                help="Link to Products or Services page"
            )
        
        with col2:
            industry = st.selectbox(
                "Industry *",
                options=INDUSTRIES,
                index=None,
                placeholder="Select an industry...",
                help="Primary industry category"
            )
            
            business_model = st.radio(
                "Business Model *",
                options=BUSINESS_MODELS,
                horizontal=True,
                help="Primary customer type"
            )
            
            target_market = st.text_input(
                "Target Market",
                placeholder="e.g., North America, SMBs, Healthcare",
                help="Geographic or demographic focus (optional)"
            )
            
            known_competitors = st.text_area(
                "Known Competitors",
                placeholder="List competitor names or URLs, one per line",
                height=80,
                help="Competitors you're aware of (optional)"
            )
        
        additional_context = st.text_area(
            "Additional Context",
            placeholder="Any other relevant information about the business, "
                       "target audience, or specific research focus...",
            height=100,
            help="Provide any additional context (optional)"
        )
        
        additional_urls = st.text_area(
            "Additional URLs (one per line)",
            placeholder="https://www.example.com/case-studies\n"
                       "https://www.example.com/team\n"
                       "https://www.example.com/blog",
            height=80,
            help="Additional pages to research (optional)"
        )
        
        st.markdown("---")
        
        submitted = st.form_submit_button(
            "🚀 Start Audience Research",
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
                errors.append("Please select an industry")
            
            if errors:
                for error in errors:
                    st.error(f"❌ {error}")
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
                about_page_url=about_page_url if about_page_url else None,
                products_services_url=products_url if products_url else None,
                additional_urls=url_list,
                industry=industry,
                business_model=bm_map[business_model],
                target_market=target_market if target_market else None,
                known_competitors=known_competitors if known_competitors else None,
                additional_context=additional_context if additional_context else None,
                num_icps=num_icps
            )
    
    return None


# ===== Progress Display =====

def render_progress():
    """Render the research progress."""
    if not st.session_state.is_running:
        return
    
    st.header("🔄 Research in Progress")
    st.info("Please wait while we analyze your client's audience...")
    
    progress_bar = st.progress(0)
    status_container = st.empty()
    
    # Calculate progress
    total_stages = len(PIPELINE_STAGES)
    completed = sum(
        1 for stage in PIPELINE_STAGES
        if st.session_state.stage_outputs.get(
            stage["id"], {}
        ).get("status") == "complete"
    )
    progress = completed / total_stages
    progress_bar.progress(progress)
    
    # Show stage status
    with status_container.container():
        for stage in PIPELINE_STAGES:
            stage_id = stage["id"]
            status = st.session_state.stage_outputs.get(
                stage_id, {}
            ).get("status", "pending")
            
            if status == "running":
                st.info(f"⏳ **{stage['name']}**: {stage['description']}...")
            elif status == "complete":
                st.success(f"✅ **{stage['name']}**: Complete")
            elif status == "error":
                error_msg = st.session_state.stage_outputs.get(
                    stage_id, {}
                ).get("error", "Unknown error")
                st.error(f"❌ **{stage['name']}**: {error_msg}")
            else:
                st.write(f"⬜ **{stage['name']}**: Pending")


# ===== Results Display =====

def render_results():
    """Render the research results."""
    results: ResearchResults = st.session_state.results
    
    if not results:
        return
    
    st.header("📊 Research Results")
    
    # Check for errors
    if results.error:
        st.warning(
            f"⚠️ Research completed with errors for "
            f"**{results.client_input.client_name}**"
        )
        st.error(f"Error: {results.error}")
    else:
        st.success(
            f"✅ Research complete for **{results.client_input.client_name}**"
        )
    
    # Tabs for different sections
    tabs = st.tabs([
        "🏢 Company",
        "👥 ICPs",
        "💎 Value Props",
        "😰 Pain Points",
        "🗺️ Journeys",
        "📥 Export"
    ])
    
    # Company Profile Tab
    with tabs[0]:
        render_company_profile(results)
    
    # ICPs Tab
    with tabs[1]:
        render_icps(results)
    
    # Value Propositions Tab
    with tabs[2]:
        render_value_propositions(results)
    
    # Pain Points Tab
    with tabs[3]:
        render_pain_points(results)
    
    # Journey Maps Tab
    with tabs[4]:
        render_journey_maps(results)
    
    # Export Tab
    with tabs[5]:
        render_export(results)


def render_company_profile(results: ResearchResults):
    """Render company profile section."""
    if not results.company_profile:
        st.info("Company profile not available.")
        return
    
    profile = results.company_profile
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(profile.name)
        st.write(profile.overview)
    
    with col2:
        st.write(f"**Industry:** {profile.industry}")
        st.write(f"**Model:** {profile.business_model.value}")
        if profile.stated_target_audience:
            st.write(f"**Target:** {profile.stated_target_audience}")
    
    if profile.products_services:
        st.markdown("### 📦 Products & Services")
        for ps in profile.products_services:
            with st.expander(f"**{ps.name}**"):
                st.write(ps.description)
                if ps.features:
                    st.write("**Features:**")
                    for f in ps.features:
                        st.write(f"• {f}")
                if ps.unique_aspects:
                    st.write("**Unique Aspects:**")
                    for u in ps.unique_aspects:
                        st.write(f"• {u}")
    
    if profile.stated_value_propositions:
        st.markdown("### 💡 Stated Value Propositions")
        for vp in profile.stated_value_propositions:
            st.write(f"• {vp}")
    
    if profile.competitors:
        st.markdown("### 🎯 Competitive Landscape")
        for comp in profile.competitors:
            with st.expander(f"**{comp.name}**"):
                if comp.description:
                    st.write(comp.description)
                if comp.key_differentiators:
                    st.write("**Differentiators:**")
                    for d in comp.key_differentiators:
                        st.write(f"• {d}")


def render_icps(results: ResearchResults):
    """Render ICPs section."""
    if not results.icps:
        st.info("ICPs not available.")
        return
    
    for icp_result in results.icps:
        icp = icp_result.icp
        
        with st.expander(
            f"👤 **{icp.icp_name}** — {icp.segment_priority}",
            expanded=True
        ):
            st.markdown(f"*{icp.one_liner}*")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("##### Demographics")
                if icp.demographics.company_size:
                    st.write(f"**Size:** {icp.demographics.company_size}")
                if icp.demographics.job_titles:
                    st.write(f"**Titles:** {', '.join(icp.demographics.job_titles[:3])}")
                if icp.demographics.industry_verticals:
                    st.write(f"**Industries:** {', '.join(icp.demographics.industry_verticals[:3])}")
            
            with col2:
                st.markdown("##### Psychographics")
                if icp.psychographics.decision_style:
                    st.write(f"**Decision:** {icp.psychographics.decision_style.value}")
                if icp.psychographics.risk_tolerance:
                    st.write(f"**Risk:** {icp.psychographics.risk_tolerance.value}")
                if icp.psychographics.core_values:
                    st.write(f"**Values:** {', '.join(icp.psychographics.core_values[:3])}")
            
            with col3:
                st.markdown("##### Behavior")
                if icp.behavioral.decision_timeline:
                    st.write(f"**Timeline:** {icp.behavioral.decision_timeline}")
                if icp.behavioral.research_channels:
                    st.write(f"**Channels:** {', '.join(icp.behavioral.research_channels[:3])}")
            
            st.markdown("---")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if icp.motivations:
                    st.markdown("##### 🎯 Motivations")
                    for m in icp.motivations[:5]:
                        st.write(f"• {m.statement}")
            
            with col2:
                if icp.pain_points:
                    st.markdown("##### 😰 Pain Points")
                    for p in icp.pain_points[:5]:
                        st.write(f"• {p.statement} ({p.severity}/10)")
            
            if icp.detailed_narrative:
                st.markdown("##### 📖 Detailed Profile")
                st.write(icp.detailed_narrative)


def render_value_propositions(results: ResearchResults):
    """Render value propositions section."""
    if not results.icps:
        st.info("Value propositions not available.")
        return
    
    for icp_result in results.icps:
        if not icp_result.value_proposition:
            continue
        
        vp = icp_result.value_proposition
        
        with st.expander(
            f"💎 **Value Proposition for {icp_result.icp.icp_name}**",
            expanded=True
        ):
            if vp.value_proposition_statement:
                st.info(f"💡 {vp.value_proposition_statement}")
            
            if vp.fit_score:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.metric("Fit Score", f"{vp.fit_score:.0f}/100")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("##### Pain Relievers")
                for pr in vp.pain_relievers[:5]:
                    st.write(f"**{pr.pain_addressed}**")
                    st.write(f"  → {pr.how_relieved}")
            
            with col2:
                st.markdown("##### Gain Creators")
                for gc in vp.gain_creators[:5]:
                    st.write(f"**{gc.gain_created}**")
                    st.write(f"  → {gc.how_created}")
            
            if vp.unique_differentiators:
                st.markdown("##### 🌟 Unique Differentiators")
                for d in vp.unique_differentiators:
                    st.write(f"• {d}")


def render_pain_points(results: ResearchResults):
    """Render pain points section."""
    if not results.icps:
        st.info("Pain points not available.")
        return
    
    for icp_result in results.icps:
        if not icp_result.pain_taxonomy:
            continue
        
        pt = icp_result.pain_taxonomy
        
        with st.expander(
            f"😰 **Pain Taxonomy for {icp_result.icp.icp_name}**",
            expanded=True
        ):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("##### ⚙️ Functional")
                for p in pt.functional_pains[:5]:
                    st.write(f"• {p.statement}")
                    st.caption(f"  Severity: {p.severity}/10 | {p.category}")
            
            with col2:
                st.markdown("##### 💰 Financial")
                for p in pt.financial_pains[:5]:
                    st.write(f"• {p.statement}")
                    st.caption(f"  Severity: {p.severity}/10 | {p.category}")
            
            with col3:
                st.markdown("##### 💔 Emotional")
                for p in pt.emotional_pains[:5]:
                    st.write(f"• {p.statement}")
                    st.caption(f"  Severity: {p.severity}/10 | {p.category}")
            
            if pt.forces_analysis:
                st.markdown("---")
                st.markdown("##### ⚖️ Forces of Progress Analysis")
                
                fa = pt.forces_analysis
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Push Factors** (away from status quo)")
                    for f in fa.push_factors[:3]:
                        st.write(f"• {f}")
                    
                    st.markdown("**Pull Factors** (toward new solution)")
                    for f in fa.pull_factors[:3]:
                        st.write(f"• {f}")
                
                with col2:
                    st.markdown("**Habit Factors** (inertia)")
                    for f in fa.habit_factors[:3]:
                        st.write(f"• {f}")
                    
                    st.markdown("**Anxiety Factors** (fear of change)")
                    for f in fa.anxiety_factors[:3]:
                        st.write(f"• {f}")
                
                if fa.net_force_assessment:
                    st.info(f"**Assessment:** {fa.net_force_assessment}")
                if fa.recommended_focus:
                    st.success(f"**Recommended Focus:** {fa.recommended_focus}")


def render_journey_maps(results: ResearchResults):
    """Render journey maps section."""
    if not results.icps:
        st.info("Journey maps not available.")
        return
    
    for icp_result in results.icps:
        if not icp_result.journey_map:
            continue
        
        jm = icp_result.journey_map
        
        with st.expander(
            f"🗺️ **Journey Map for {icp_result.icp.icp_name}**",
            expanded=True
        ):
            if jm.overall_timeline:
                st.write(f"**Overall Timeline:** {jm.overall_timeline}")
            
            stages = [
                ("1️⃣ Awareness", jm.awareness_stage),
                ("2️⃣ Consideration", jm.consideration_stage),
                ("3️⃣ Decision", jm.decision_stage),
                ("4️⃣ Onboarding", jm.onboarding_stage),
                ("5️⃣ Expansion", jm.expansion_stage)
            ]
            
            stage_tabs = st.tabs([s[0] for s in stages if s[1]])
            
            for tab, (stage_name, stage) in zip(
                stage_tabs,
                [(n, s) for n, s in stages if s]
            ):
                with tab:
                    st.markdown(f"**Objective:** {stage.objective}")
                    
                    if stage.emotional_state:
                        st.write(
                            f"**Emotional State:** "
                            f"{', '.join(stage.emotional_state)}"
                        )
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if stage.key_questions:
                            st.markdown("**Key Questions:**")
                            for q in stage.key_questions[:5]:
                                st.write(f"• {q}")
                        
                        if stage.content_themes:
                            st.markdown("**Content Themes:**")
                            for t in stage.content_themes[:5]:
                                st.write(f"• {t}")
                    
                    with col2:
                        if stage.preferred_channels:
                            st.markdown("**Preferred Channels:**")
                            for c in stage.preferred_channels[:5]:
                                st.write(f"• {c}")
                        
                        if stage.kpis:
                            st.markdown("**KPIs:**")
                            for k in stage.kpis[:5]:
                                st.write(f"• {k}")
                    
                    if stage.content_ideas:
                        st.markdown("**Content Ideas:**")
                        for idea in stage.content_ideas[:5]:
                            st.write(f"• **{idea.title}** ({idea.format})")
                            if idea.hook:
                                st.caption(f"  Hook: {idea.hook}")


def render_export(results: ResearchResults):
    """Render export section."""
    st.subheader("📥 Export Research Results")
    
    st.markdown(
        "Download your research results in your preferred format."
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📝 Markdown")
        st.write("Best for documentation, GitHub, Notion, etc.")
        
        try:
            from app.export.markdown_generator import generate_markdown
            md_content = generate_markdown(results)
            
            st.download_button(
                "📥 Download Markdown",
                data=md_content,
                file_name=f"{results.client_input.client_name}_research.md",
                mime="text/markdown",
                use_container_width=True
            )
        except ImportError:
            st.warning("Markdown export module not available yet.")
    
    with col2:
        st.markdown("### 📄 DOCX")
        st.write("Best for Word, Google Docs, presentations.")
        
        try:
            from app.export.docx_generator import generate_docx
            docx_bytes = generate_docx(results)
            
            st.download_button(
                "📥 Download DOCX",
                data=docx_bytes,
                file_name=f"{results.client_input.client_name}_research.docx",
                mime="application/vnd.openxmlformats-officedocument"
                     ".wordprocessingml.document",
                use_container_width=True
            )
        except ImportError:
            st.warning("DOCX export module not available yet.")
    
    st.markdown("---")
    
    # Cost summary
    st.subheader("💰 Session Cost Summary")
    summary = st.session_state.cost_tracker.get_summary()
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Cost", f"${summary['total_cost']:.4f}")
    col2.metric("Total Requests", summary['total_requests'])
    col3.metric("Input Tokens", f"{summary['total_tokens']['input']:,}")
    col4.metric("Output Tokens", f"{summary['total_tokens']['output']:,}")


# ===== Run Research =====

def run_research(client_input: ClientInput, selected_model: str):
    """Run the research pipeline."""
    st.session_state.is_running = True
    st.session_state.stage_outputs = {}
    
    try:
        from app.core.orchestrator import ResearchOrchestrator
        
        # Progress callback
        def progress_callback(stage_id: str, status: str, data=None, error=None):
            if stage_id not in st.session_state.stage_outputs:
                st.session_state.stage_outputs[stage_id] = {}
            st.session_state.stage_outputs[stage_id]["status"] = status
            if data:
                st.session_state.stage_outputs[stage_id]["data"] = data
            if error:
                st.session_state.stage_outputs[stage_id]["error"] = error
        
        # Create orchestrator
        orchestrator = ResearchOrchestrator(
            analysis_model=selected_model,
            cost_tracker=st.session_state.cost_tracker
        )
        
        # Run research
        results = orchestrator.run_research(
            client_input,
            progress_callback=progress_callback
        )
        
        st.session_state.results = results
        st.session_state.is_running = False
        
        return True
        
    except Exception as e:
        st.session_state.is_running = False
        st.error(f"❌ Research failed: {str(e)}")
        return False


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
        
        st.markdown("---")
        if st.button("🔄 Start New Research", use_container_width=True):
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
            st.session_state.session.client_input = client_input
            
            with st.spinner("🚀 Starting research pipeline..."):
                success = run_research(client_input, selected_model)
                if success:
                    st.rerun()


if __name__ == "__main__":
    main()