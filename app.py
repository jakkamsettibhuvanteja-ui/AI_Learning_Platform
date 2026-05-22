import streamlit as st
import pandas as pd
from ai_engine import generate_roadmap

st.set_page_config(
    page_title = "AI Market-Driven Learning Platform",
    page_icon = "🤖",
    layout = "wide"
)

if "ai_data" not in st.session_state:
    st.session_state.ai_data = None

st.sidebar.header("👤 Candidate Current Situation")
user_name = st.sidebar.text_input("Candidate Name", value="Bhuvan")
target_role = st.sidebar.selectbox("Target Domain/Role", ["AI/ML Engineer", "Full Stack Developer", "Data Engineer"])
experience_level = st.sidebar.select_slider("Select your Current Skills", options=["Fresher", "Intermediate", "Experienced"])
current_skills = st.sidebar.multiselect("Select your Current Skills", ["Python", "Java", "C++", "SQL", "HTML/CSS", "JavaScript", "Git"], default=["Python"])

if st.sidebar.button("🚀 Generate Market Aligned Roadmap"):
    with st.spinner("Analyzing 2026 Market Standards and generating your path..."):
        # 🌟 FIXED: Changed hyphen to underscore and passed inputs matching ai_engine definition
        live_result = generate_roadmap(target_role, experience_level, current_skills)

        if live_result:
            st.session_state.ai_data = live_result
            st.success("Roadmap generated successfully!")
            st.balloons()
        else:
            st.error("Failed to generate roadmap. Please check your API configuration or Internet Connection.")

st.title("🤖 AI-Powered Adaptive Learning Platform ")
st.caption(f"Personalized Curriculum Roadmap generated for {user_name} according to the Current Marketing Standards.")
st.markdown("---")

if "ai_data" not in st.session_state or st.session_state.ai_data is None:
    st.info("👈 Please adjust your profile details in the left sidebar and click 'Generate Market-Aligned Roadmap' to begin your Analysis.")
else:
    data = st.session_state.ai_data
    st.header("📈 2026 Real-Time Market Analysis")
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    with metric_col1:
        st.metric(label="Market Demand Status", value=data.get("market_demand", "N/A"), delta="Growth Trend", delta_color="normal", border=True)
    with metric_col2:
        st.metric(label="Average Entry/Mid Salary", value=data.get("average_salary", "N/A"), delta="Premium Scale", border=True)
    with metric_col3:
        st.metric(label="Hiring Velocity", value=data.get("hiring_velocity", "N/A"), delta="Short Interview Cycles", border=True)

    st.write("### Job Openings Volume vs. Candidate Supply Trends")
    trend_raw = data.get("market_trend_data", {})
    months_index = trend_raw.get('months', ['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    openings_list = trend_raw.get('job_openings', [100, 120, 140, 130, 150])
    applicants_list = trend_raw.get('applicants', [80, 90, 95, 85, 100])
    
    chart_data = pd.DataFrame(
        {
            'Job Openings': openings_list,
            'Applicants': applicants_list
        }
    )
    if len(months_index) == len(chart_data):
        chart_data.index = months_index
    else:
        chart_data.index = ['Jan', 'Feb', 'Mar', 'Apr', 'May'][:len(chart_data)]
    st.line_chart(chart_data)
    st.divider()

    st.header("📊 Details of Current Situation & Diagnosis")
    col_left, col_right = st.columns([1, 2])
    with col_left:
        st.subheader("👤 Profile Snapshot")
        st.write(f"**Target Role:** {target_role}")
        st.write(f"**Experience Classification:** {experience_level}")
        st.write(f"**Registered Skills:** {', '.join(current_skills) if current_skills else 'None declared'}")
    with col_right:
        st.subheader("🚨 Skill-Gap Analysis Alert")
        st.warning(data.get("gap_analysis_text", "No gap text provided by AI."))
        st.info("💡 Market Alignment: Modern Industry Benchmarks require moving towards Automated Frameworks.")
    st.divider()

    st.header("🏁 Easy Options (Low-Hanging Fruit Paths)")
    st.markdown("_Immediate Courses/certifications to check off first to make your Profile visible to indexers:_")
    easy_list = data.get("easy_modules", [])
    for i, module in enumerate(easy_list):
        title = module.get("title", f"Module {i+1}")
        with st.expander(f"📘 {title} (Estimated Time: 1 Week)"):
            st.write(f"**Objective:** {module.get('objective', 'N/A')}")
            st.write(f"**Action Plan:** {module.get('action_plan', 'N/A')}")
    st.divider()

    st.header("🚀 Better Options (Maximum Market Value Roadmap)")
    st.write("Focus on these complex core competencies to unlock elite tier profiles:")
    better_list = data.get("better_options", [])
    if isinstance(better_list, list) and len(better_list) > 0:
        better_df = pd.DataFrame(better_list)
        better_df.columns = [col.replace('_', ' ').title() for col in better_df.columns]
        st.dataframe(better_df, use_container_width=True)
    else:
        st.info("💡 The AI did not return premium path metrics for this specific stack combination.")

    st.divider()
    st.header("💾 Export your Personalized Curriculum")
    st.write("_Save your AI-Generated market roadmap locally to track your progress offline:")

    download_text = f""" AI-POWERED LEARNING CURRICULUM ROADMAP
    Generated for: {user_name}
    Target_Domain: {target_role}
    Experience_Classification: {experience_level}
    Current Baseline Skills: {', '.join(current_skills) if current_skills else 'None'}
    ==========================================================================

    ## 1. 2026 REAL-TIME MARKET DIAGNOSIS
    - Market Demand Status: {data.get("market_demand", "N/A")}
    - Average Salary Bracket: {data.get("average_salary", "N/A")}
    - Hiring Velocity Scale: {data.get("hiring_velocity", "N/A")}

    ### 🚨 SKILL_GAP ANALYSIS EVALUATION:
    {data.get("gap_analysis_text", 'N/A')}

    ===========================================================================
    ## 2. EASY OPTIONS (QUICK-WIN MODULES)
    """
    for i, module in enumerate(data.get('easy_modules', [])):
        download_text += f"\n### Module {i+1}: {module.get('title', 'N/A')}\n"
        download_text += f"- Objective: {module.get('objective', 'N/A')}\n"
        download_text += f"- Action Plan: {module.get('action_plan', 'N/A')}\n"

    download_text += "\n=================================================================\n## 3. BETTER OPTIONS (PREMIUM CORE COMPETENCIES)\n"

    for i, option in enumerate(data.get('better_options', [])):
        download_text += f"\n### Path {i+1}: {option.get('competency', 'N/A') or option.get('Advanced Competency Focus', 'N/A')}\n"
        download_text += f"- Target Scope: {option.get('project_scope', 'N/A') or option.get('Project Target Scope', 'N/A')}\n"
        download_text += f"- Market Premium: {option.get('market_premium', 'N/A') or option.get('Market Premium', 'N/A')}\n"

    st.download_button(
        label="📥 Download Roadmap as Text File",
        data=download_text,
        file_name=f"{user_name}_{target_role.replace(' ', '_')}_Roadmap.txt",
        mime="text/plain",
        use_container_width = True
    )
    st.success("🎯 Project Execution Complete. Your Custom AI Learning engine is fully synchronized with 2026 Industry Frameworks.")
