import json
import os
import streamlit as st
from google import genai
from google.genai import types

API_KEY = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY") or "AIzaSyDODrppTnV4r92GGtM_noVWt7vn034fyK0"
client = genai.Client(api_key=API_KEY)

def generate_roadmap(target_role, experience_level, current_skills):
    """
    Takes user profile inputs, sends a structured system prompt to Gemini,
    and returns a clean Python Dictionary parsed from the AI's JSON output.
    """
    # 🌟 FIXED: Removed the old legacy genai.GenerativeModel initialization line
    
    prompt = f"""
    You are an Elite IT career Strategist and Tech Market Analyst.
    Analyze the following Candidate Profile and provide an industry-aligned
    learning path according to current 2026 market standards.
    
    CANDIDATE PROFILE:
    - Target Role: {target_role}
    - Current Experience Tier: {experience_level}
    - Existing Skills: {', '.join(current_skills)}

    YOUR INSTRUCTIONS:
    1. Assess the 2026 market demand status and average entry salary for this target role.
    2. Conduct a brief skill gap analysis warning.
    3. Provide exactly 3 'Easy Options' (Low Hanging fruit modules) to bridge immediate gaps.
    4. Provide exactly 2 'Better Options' (High Value, Premium core competencies) for long-term career growth.

    CRITICAL CONSTRAINT: You must output your entire response only as a single valid JSON Object.
    Do not include any conversational text, intro, or markdown wrapper layout tags like ```json.
    Follow this exact JSON Structural template perfectly:

    {{
        "market_demand": "string (e.g., Critical (94)%)",
        "average_salary": "string (e.g., $120,000+)",
        "hiring_velocity": "string (e.g., Aggressive)",
        "gap_analysis_text": "string (A Direct assessment of what they lack)",
        "market_trend_data": {{
            "months": ["Jan", "Feb", "Mar", "Apr", "May"],
            "job_openings": [100, 120, 145, 130, 165],
            "applicants": [80, 85, 90, 88, 95]
        }},
        "easy_modules": [
            {{
                "title": "string",
                "objective": "string",
                "action_plan": "string"
            }}
        ],
        "better_options": [
            {{
                "competency": "string",
                "project_scope": "string",
                "market_premium": "string"
            }}
        ]
    }}
    """

    try:
        # 🌟 FIXED: Restructured with appropriate commas and clear dictionary parameters
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )
        
        raw_json_text = response.text
        data_dictionary = json.loads(raw_json_text)

        if "easy_modules" not in data_dictionary or not isinstance(data_dictionary["easy_modules"], list):
            data_dictionary["easy_modules"] = []

        possible_keys = ["better_options", "Better_Options", "better_paths", "premium_options", "better options"]
        target_key = None

        for k in possible_keys:
            if k in data_dictionary:
                target_key = k
                break
                
        if target_key and target_key != "better_options":
            data_dictionary["better_options"] = data_dictionary.pop(target_key)

        if "better_options" not in data_dictionary or not isinstance(data_dictionary["better_options"], list):
            data_dictionary["better_options"] = [
                {
                    "competency": f"Advanced {target_role} Architecture",
                    "project_scope": f"Design and Implement a high-throughput system optimizing modern industry benchmarks.",
                    "market_premium": f"Elite Tier Premium"
                }
            ]

        for module in data_dictionary["easy_modules"]:
            if not isinstance(module, dict):
                continue
            if "title" not in module: module["title"] = "Custom Learning Module"
            if "objective" not in module: module["objective"] = "Deepen Technical mastery of this Stack Component."
            if "action_plan" not in module: module["action_plan"] = "Build a localized project showcasing this competency."
            
        return data_dictionary
        
    except Exception as e:
        print(f"Error calling AI Engine: {e}")
        st.sidebar.error(f"⚠️ Google API Gateway Response: {e}")
        return None
