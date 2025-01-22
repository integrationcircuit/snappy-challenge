import streamlit as st
import requests

def show_registration_form(team_name_record: str):
    st.subheader("Workshop Feedback")
    
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Email Address (for completion badges)", key="form_email")
        st.selectbox("Your Role", key="form_role",
                     options=[
                        "Solution Architect",
                        "DevOps Engineer",
                        "Software Developer",
                        "Sales Engineer",
                        "Technical Consultant",
                        "Project Manager",
                        "Other"],
                     placeholder="Select Your Role")
        
    with col2:
        st.selectbox("What is your experience level with GenerativeAI?", key="form_experience",
                     options=["Explorer (Very New/This was my first time)", 
                              "Adventurer (I used some AI Tools before)", 
                              "Champion (Using AI tools regularly)", 
                              "Hero (Built and deployed production usecases, use LLMs daily)"],
                     placeholder="Select Your Experience Level")
        st.selectbox("Would you be interested in longer, deep-dive workshop?", key="form_follow_up",
                     options=["Yes", "No", "Maybe - will elaborate below"],
                     placeholder="Select Your Interest")
    st.text_area("Feedback", key="form_feedback")
    if st.button("Submit Feedback"):
        register_feedback(team_name_record)
    

def register_feedback(team_name_record: str):
    try:
        request_params = {
            "team_name": str(team_name_record),
            "email": str(st.session_state["form_email"]),
            "role": str(st.session_state["form_role"]),
            "experience": str(st.session_state["form_experience"]),
            "follow_up": str(st.session_state["form_follow_up"]),
            "feedback": str(st.session_state["form_feedback"])
        }
        
        response = requests.post(url="https://emea.snaplogic.com/api/1/rest/slsched/feed/ConnectFasterInc/0_StanGPT/StanCoE/Workshop_ReceiveFeedbackTask",
                                 headers={"Authorization": "Bearer 3OXXvsGp6qMdGmcwfQNLcInWaOqUJ7wu"},
                                 json=request_params)
        
        if response.status_code == 200:
            st.success("Feedback submitted successfully.")
        else:
            st.error("Failed to submit feedback.")
    except Exception as e:
        st.error(f"Error: {e}")