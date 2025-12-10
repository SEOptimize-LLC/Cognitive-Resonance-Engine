"""
Markdown Report Generator
=========================
Generates comprehensive Markdown reports from research results.
"""

from datetime import datetime
from typing import List

from app.models.research_models import (
    ResearchResults,
    ICPAnalysisResult,
    JourneyStage
)


def generate_markdown(results: ResearchResults) -> str:
    """
    Generate a comprehensive Markdown report from research results.
    
    Args:
        results: The complete research results
        
    Returns:
        Markdown formatted string
    """
    sections = []
    
    # Title
    sections.append(
        f"# Audience Research Report: {results.client_input.client_name}"
    )
    sections.append(f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
    
    # Table of Contents
    sections.append("## Table of Contents\n")
    sections.append("1. [Executive Summary](#executive-summary)")
    sections.append("2. [Company Profile](#company-profile)")
    sections.append("3. [Ideal Customer Profiles](#ideal-customer-profiles)")
    sections.append("4. [Value Propositions](#value-propositions)")
    sections.append("5. [Pain Point Analysis](#pain-point-analysis)")
    sections.append("6. [Customer Journey Maps](#customer-journey-maps)")
    sections.append("7. [Cost Summary](#cost-summary)\n")
    
    # Executive Summary
    sections.append(generate_executive_summary(results))
    
    # Company Profile
    sections.append(generate_company_section(results))
    
    # ICPs
    sections.append(generate_icps_section(results))
    
    # Value Propositions
    sections.append(generate_vp_section(results))
    
    # Pain Points
    sections.append(generate_pain_section(results))
    
    # Journey Maps
    sections.append(generate_journey_section(results))
    
    # Cost Summary
    sections.append(generate_cost_section(results))
    
    return "\n".join(sections)


def generate_executive_summary(results: ResearchResults) -> str:
    """Generate executive summary section."""
    lines = ["## Executive Summary\n"]
    
    client = results.client_input
    profile = results.company_profile
    
    lines.append(
        f"This report presents comprehensive audience research for "
        f"**{client.client_name}**, a {client.business_model.value} company "
        f"in the {client.industry} industry."
    )
    
    if profile:
        lines.append(f"\n{profile.overview}\n")
    
    # Key findings
    lines.append("### Key Findings\n")
    
    num_icps = len(results.icps)
    lines.append(f"- **{num_icps} Ideal Customer Profiles** identified")
    
    high_priority = sum(
        1 for icp_result in results.icps
        if icp_result.icp.segment_priority == "high"
    )
    if high_priority:
        lines.append(f"- **{high_priority} High-Priority Segments** for targeting")
    
    # List ICPs
    if results.icps:
        lines.append("\n**Identified ICPs:**\n")
        for icp_result in results.icps:
            icp = icp_result.icp
            priority = f"({icp.segment_priority})"
            lines.append(f"- **{icp.icp_name}** {priority}: {icp.one_liner}")
    
    lines.append("")
    return "\n".join(lines)


def generate_company_section(results: ResearchResults) -> str:
    """Generate company profile section."""
    lines = ["## Company Profile\n"]
    
    profile = results.company_profile
    if not profile:
        lines.append("*Company profile not available.*\n")
        return "\n".join(lines)
    
    lines.append(f"### {profile.name}\n")
    lines.append(f"**Website:** {profile.website_url}\n")
    lines.append(f"**Industry:** {profile.industry}\n")
    lines.append(f"**Business Model:** {profile.business_model.value}\n")
    
    if profile.overview:
        lines.append(f"\n{profile.overview}\n")
    
    # Products & Services
    if profile.products_services:
        lines.append("### Products & Services\n")
        for ps in profile.products_services:
            lines.append(f"#### {ps.name}\n")
            lines.append(f"{ps.description}\n")
            if ps.features:
                lines.append("**Features:**")
                for f in ps.features:
                    lines.append(f"- {f}")
            if ps.unique_aspects:
                lines.append("\n**Unique Aspects:**")
                for u in ps.unique_aspects:
                    lines.append(f"- {u}")
            lines.append("")
    
    # Value Propositions
    if profile.stated_value_propositions:
        lines.append("### Stated Value Propositions\n")
        for vp in profile.stated_value_propositions:
            lines.append(f"- {vp}")
        lines.append("")
    
    # Competitors
    if profile.competitors:
        lines.append("### Competitive Landscape\n")
        for comp in profile.competitors[:5]:
            lines.append(f"- **{comp.name}**")
            if comp.description:
                lines.append(f"  - {comp.description}")
            if comp.key_differentiators:
                diffs = ", ".join(comp.key_differentiators[:3])
                lines.append(f"  - Differentiators: {diffs}")
        lines.append("")
    
    return "\n".join(lines)


def generate_icps_section(results: ResearchResults) -> str:
    """Generate ICPs section."""
    lines = ["## Ideal Customer Profiles\n"]
    
    if not results.icps:
        lines.append("*No ICPs generated.*\n")
        return "\n".join(lines)
    
    for i, icp_result in enumerate(results.icps, 1):
        icp = icp_result.icp
        
        lines.append(f"### ICP {i}: {icp.icp_name}\n")
        lines.append(f"**Priority:** {icp.segment_priority.upper()}\n")
        lines.append(f"*{icp.one_liner}*\n")
        
        # Demographics
        lines.append("#### Demographics/Firmographics\n")
        demo = icp.demographics
        if demo.company_size:
            lines.append(f"- **Company Size:** {demo.company_size}")
        if demo.job_titles:
            lines.append(f"- **Job Titles:** {', '.join(demo.job_titles)}")
        if demo.industry_verticals:
            lines.append(
                f"- **Industries:** {', '.join(demo.industry_verticals)}"
            )
        if demo.geographic_focus:
            lines.append(f"- **Geography:** {demo.geographic_focus}")
        if demo.budget_range:
            lines.append(f"- **Budget Range:** {demo.budget_range}")
        lines.append("")
        
        # Psychographics
        lines.append("#### Psychographics\n")
        psycho = icp.psychographics
        lines.append(f"- **Decision Style:** {psycho.decision_style.value}")
        lines.append(f"- **Risk Tolerance:** {psycho.risk_tolerance.value}")
        if psycho.core_values:
            lines.append(f"- **Core Values:** {', '.join(psycho.core_values)}")
        if psycho.aspirations:
            lines.append(f"- **Aspirations:** {', '.join(psycho.aspirations)}")
        if psycho.fears:
            lines.append(f"- **Key Fears:** {', '.join(psycho.fears)}")
        lines.append("")
        
        # Behavior
        lines.append("#### Behavioral Profile\n")
        behav = icp.behavioral
        if behav.research_channels:
            lines.append(
                f"- **Research Channels:** {', '.join(behav.research_channels)}"
            )
        if behav.decision_timeline:
            lines.append(f"- **Decision Timeline:** {behav.decision_timeline}")
        if behav.content_preferences:
            lines.append(
                f"- **Content Preferences:** "
                f"{', '.join(behav.content_preferences)}"
            )
        if behav.current_solutions:
            lines.append(
                f"- **Current Solutions:** {', '.join(behav.current_solutions)}"
            )
        lines.append("")
        
        # Motivations
        if icp.motivations:
            lines.append("#### Key Motivations\n")
            for m in icp.motivations[:5]:
                lines.append(
                    f"- {m.statement} *(Intensity: {m.intensity}/10)*"
                )
            lines.append("")
        
        # Pain Points
        if icp.pain_points:
            lines.append("#### Key Pain Points\n")
            for p in icp.pain_points[:5]:
                lines.append(
                    f"- {p.statement} *(Severity: {p.severity}/10)*"
                )
            lines.append("")
        
        # Narrative
        if icp.detailed_narrative:
            lines.append("#### Detailed Profile\n")
            lines.append(f"{icp.detailed_narrative}\n")
        
        lines.append("---\n")
    
    return "\n".join(lines)


def generate_vp_section(results: ResearchResults) -> str:
    """Generate value propositions section."""
    lines = ["## Value Propositions\n"]
    
    has_vp = any(r.value_proposition for r in results.icps)
    if not has_vp:
        lines.append("*Value propositions not analyzed.*\n")
        return "\n".join(lines)
    
    for icp_result in results.icps:
        if not icp_result.value_proposition:
            continue
        
        vp = icp_result.value_proposition
        icp = icp_result.icp
        
        lines.append(f"### Value Proposition for {icp.icp_name}\n")
        
        if vp.value_proposition_statement:
            lines.append(f"> {vp.value_proposition_statement}\n")
        
        if vp.fit_score:
            lines.append(f"**Fit Score:** {vp.fit_score}/100\n")
        
        # Pain Relievers
        if vp.pain_relievers:
            lines.append("#### Pain Relievers\n")
            for pr in vp.pain_relievers[:5]:
                lines.append(f"**{pr.pain_addressed}**")
                lines.append(f"- *Feature:* {pr.feature_or_capability}")
                lines.append(f"- *How:* {pr.how_relieved}")
                lines.append("")
        
        # Gain Creators
        if vp.gain_creators:
            lines.append("#### Gain Creators\n")
            for gc in vp.gain_creators[:5]:
                lines.append(f"**{gc.gain_created}**")
                lines.append(f"- *Feature:* {gc.feature_or_capability}")
                lines.append(f"- *How:* {gc.how_created}")
                lines.append("")
        
        # Unique Differentiators
        if vp.unique_differentiators:
            lines.append("#### Unique Differentiators\n")
            for d in vp.unique_differentiators:
                lines.append(f"- {d}")
            lines.append("")
        
        lines.append("---\n")
    
    return "\n".join(lines)


def generate_pain_section(results: ResearchResults) -> str:
    """Generate pain points section."""
    lines = ["## Pain Point Analysis\n"]
    
    has_pain = any(r.pain_taxonomy for r in results.icps)
    if not has_pain:
        lines.append("*Pain taxonomy not analyzed.*\n")
        return "\n".join(lines)
    
    for icp_result in results.icps:
        if not icp_result.pain_taxonomy:
            continue
        
        pt = icp_result.pain_taxonomy
        icp = icp_result.icp
        
        lines.append(f"### Pain Taxonomy for {icp.icp_name}\n")
        
        # Functional Pains
        if pt.functional_pains:
            lines.append("#### Functional Pain Points\n")
            lines.append("| Pain | Category | Severity |")
            lines.append("|------|----------|----------|")
            for p in pt.functional_pains[:7]:
                lines.append(f"| {p.statement} | {p.category} | {p.severity}/10 |")
            lines.append("")
        
        # Financial Pains
        if pt.financial_pains:
            lines.append("#### Financial Pain Points\n")
            lines.append("| Pain | Category | Severity |")
            lines.append("|------|----------|----------|")
            for p in pt.financial_pains[:7]:
                lines.append(f"| {p.statement} | {p.category} | {p.severity}/10 |")
            lines.append("")
        
        # Emotional Pains
        if pt.emotional_pains:
            lines.append("#### Emotional Pain Points\n")
            lines.append("| Pain | Category | Severity |")
            lines.append("|------|----------|----------|")
            for p in pt.emotional_pains[:7]:
                lines.append(f"| {p.statement} | {p.category} | {p.severity}/10 |")
            lines.append("")
        
        # Forces Analysis
        if pt.forces_analysis:
            fa = pt.forces_analysis
            lines.append("#### Forces of Progress Analysis\n")
            
            if fa.push_factors:
                lines.append("**Push Factors** (away from status quo):")
                for f in fa.push_factors[:3]:
                    lines.append(f"- {f}")
            
            if fa.pull_factors:
                lines.append("\n**Pull Factors** (toward new solution):")
                for f in fa.pull_factors[:3]:
                    lines.append(f"- {f}")
            
            if fa.habit_factors:
                lines.append("\n**Habit Factors** (resistance to change):")
                for f in fa.habit_factors[:3]:
                    lines.append(f"- {f}")
            
            if fa.anxiety_factors:
                lines.append("\n**Anxiety Factors** (fear of new):")
                for f in fa.anxiety_factors[:3]:
                    lines.append(f"- {f}")
            
            if fa.net_force_assessment:
                lines.append(f"\n**Assessment:** {fa.net_force_assessment}")
            
            if fa.recommended_focus:
                lines.append(f"\n**Recommended Focus:** {fa.recommended_focus}")
            
            lines.append("")
        
        lines.append("---\n")
    
    return "\n".join(lines)


def generate_journey_section(results: ResearchResults) -> str:
    """Generate journey maps section."""
    lines = ["## Customer Journey Maps\n"]
    
    has_journey = any(r.journey_map for r in results.icps)
    if not has_journey:
        lines.append("*Journey maps not generated.*\n")
        return "\n".join(lines)
    
    for icp_result in results.icps:
        if not icp_result.journey_map:
            continue
        
        jm = icp_result.journey_map
        icp = icp_result.icp
        
        lines.append(f"### Journey Map for {icp.icp_name}\n")
        
        if jm.overall_timeline:
            lines.append(f"**Overall Timeline:** {jm.overall_timeline}\n")
        
        stages = [
            ("Awareness", jm.awareness_stage),
            ("Consideration", jm.consideration_stage),
            ("Decision", jm.decision_stage),
            ("Onboarding", jm.onboarding_stage),
            ("Expansion", jm.expansion_stage)
        ]
        
        for stage_name, stage in stages:
            if not stage:
                continue
            
            lines.append(f"#### Stage: {stage_name}\n")
            lines.append(f"**Objective:** {stage.objective}\n")
            
            if stage.emotional_state:
                lines.append(
                    f"**Emotional State:** {', '.join(stage.emotional_state)}"
                )
            
            if stage.key_questions:
                lines.append("\n**Key Questions:**")
                for q in stage.key_questions[:5]:
                    lines.append(f"- {q}")
            
            if stage.content_themes:
                lines.append("\n**Content Themes:**")
                for t in stage.content_themes[:5]:
                    lines.append(f"- {t}")
            
            if stage.content_ideas:
                lines.append("\n**Content Ideas:**")
                for idea in stage.content_ideas[:5]:
                    lines.append(f"\n**{idea.title}** ({idea.format})")
                    if idea.hook:
                        lines.append(f"- *Hook:* {idea.hook}")
                    if idea.key_message:
                        lines.append(f"- *Message:* {idea.key_message}")
                    if idea.cta:
                        lines.append(f"- *CTA:* {idea.cta}")
            
            if stage.preferred_channels:
                lines.append(
                    f"\n**Channels:** {', '.join(stage.preferred_channels)}"
                )
            
            if stage.kpis:
                lines.append(f"\n**KPIs:** {', '.join(stage.kpis)}")
            
            lines.append("")
        
        lines.append("---\n")
    
    return "\n".join(lines)


def generate_cost_section(results: ResearchResults) -> str:
    """Generate cost summary section."""
    lines = ["## Cost Summary\n"]
    
    summary = results.cost_summary
    if not summary:
        lines.append("*Cost tracking not available.*\n")
        return "\n".join(lines)
    
    lines.append(f"**Total Cost:** ${summary.get('total_cost', 0):.4f}\n")
    lines.append(f"**Total Requests:** {summary.get('total_requests', 0)}\n")
    
    tokens = summary.get('total_tokens', {})
    lines.append(f"**Input Tokens:** {tokens.get('input', 0):,}")
    lines.append(f"**Output Tokens:** {tokens.get('output', 0):,}")
    lines.append(f"**Total Tokens:** {tokens.get('total', 0):,}\n")
    
    by_model = summary.get('by_model', {})
    if by_model:
        lines.append("### Usage by Model\n")
        lines.append("| Model | Requests | Tokens | Cost |")
        lines.append("|-------|----------|--------|------|")
        for model, data in by_model.items():
            short_name = model.split('/')[-1]
            lines.append(
                f"| {short_name} | {data['requests']} | "
                f"{data['total_tokens']:,} | ${data['cost']:.4f} |"
            )
        lines.append("")
    
    return "\n".join(lines)