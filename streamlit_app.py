import streamlit as st
import pandas as pd
from datetime import datetime
from typing import Dict, List
import requests
import json

is_challenge_1_complete = False
is_challenge_2_complete = False
is_challenge_3_complete = False

# Config and page setup
st.set_page_config(page_title="SnapLogic GenAI Workshop", layout="centered")

def get_credentials() -> Dict[str, str]:
    """Return mock credentials for the workshop."""
    url = "https://emea.snaplogic.com/api/1/rest/slsched/feed/ConnectFasterInc/0_StanGPT/StanCoE/Workshops_RetrieveNextAvailableCredentials_Task"
    bearer = "SUnx6ZN9Dt8xQCwtUdzNJIkoC3CipCiX"
    headers = {
        "Authorization": f"Bearer {bearer}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(
        url,
        headers=headers
    )
    
    response.raise_for_status()
    data = response.json()[0]
    # st.write(data)
    
    username = data["username"]
    password = data["password"]
    url = data["pipelineUrl"]
    
    if "username" not in st.session_state:
        st.session_state['username'] = username
    if "password" not in st.session_state:
        st.session_state['password'] = password
    if "url" not in st.session_state:
        st.session_state['url'] = url
    
    return {
        "username": username,
        "password": password,
        "url": url
    }

def get_workshop_tips() -> List[str]:
    """Return workshop tips."""
    return [
        "Start with the provided template code to save time",
        "Make sure to test your solution with different input formats",
        "Don't forget to handle edge cases in your implementation",
        "Use the documentation resources available at docs.example.com"
    ]
    
def get_sample_prompts() -> List[str]:
    """Return sample prompts for the workshop."""
    return [
        "Prompt 1: Sample Prompt 1 Goes Here",
        "Prompt 2: Sample Prompt 2 Goes Here",
        "Prompt 3: Sample Prompt 3 Goes Here"
    ]

def get_sample_leaderboard() -> List[Dict[str, str]]:
    """Return sample leaderboard data."""
    return [
        {"Rank": 1, "Name": "Bob@email.com", "SubmissionTime": datetime(2025, 1, 10, 11, 2, 5) .strftime("%H:%M:%S")},
        {"Rank": 2, "Name": "GarryVee@email.com", "SubmissionTime": datetime(2025, 1, 10, 11, 3, 5).strftime("%H:%M:%S")},
        {"Rank": 3, "Name": "Charlie@email.com", "SubmissionTime": datetime(2025, 1, 10, 11, 4, 5).strftime("%H:%M:%S")},
        {"Rank": 4, "Name": "David@email.com", "SubmissionTime": datetime(2025, 1, 10, 11, 5, 5).strftime("%H:%M:%S")},
        {"Rank": 5, "Name": "Eve@email.com", "SubmissionTime": datetime(2025, 1, 10, 11, 5, 6).strftime("%H:%M:%S")},
    ]
    
def validate_submission(submission: str, challenge: int) -> bool:
    """Validate user submission with mock rules."""
    if challenge == 1:
        return "92" in submission.lower()
    if challenge == 2: 
        return "384" in submission.lower()
    if challenge == 3:
        return "power" in submission.lower()
    return True


# Main app layout
st.title("SnapLogic GenAI Workshop Portal")

# Credentials section
st.subheader("Get Started")
team_name = st.text_input("Enter Your Team Name (or your own name if remote/solo)")
if len(team_name) > 0:
    if st.button("Get My Credentials"):
        if "team_name" not in st.session_state:
            st.session_state['team_name'] = team_name
        
        creds = get_credentials()
        st.write("Here are your workshop credentials (do not refresh this page or they will disappear):")
        st.write(f"Username: {creds['username']}")
        st.write(f"Password: {creds['password']}")
        st.link_button("Login", url=creds['url'])

    # Document preview
    st.subheader("Workshop Materials")
    st.link_button("Preview Workshop Materials", url="https://www.drax.com/wp-content/uploads/2024/03/Final-Signed-ESG-2023-Supplement.pdf")
    # Tips section
    with st.expander("Tips "):
        for tip in get_workshop_tips():
            st.markdown(f"• {tip}")
    with st.expander("Sample Prompts"):
        for prompt in get_sample_prompts():
            st.write(prompt)

    # Submission form
    st.subheader("Submit Your Answers")
    st.subheader("Challenge #1")
    user_submission_1 = st.text_area("Write a prompt to find what percentage of electricity supplied to customers by Drax came from renewable sources in 2023. ")
    if st.button("Check Answer", key=1):
        if validate_submission(user_submission_1, 1):
            st.success("Correct! Challenge #1 is complete.")
            is_challenge_1_complete = True
        else:
            st.error("Incorrect! Please try again.")
    
    st.subheader("Challenge #2")
    user_submission_2 = st.text_area("Write a prompt to calculate the total reduction in Carbon emissions (in ktCO2e) from Generation between the earliest and most recent years provided in the report. Express this reduction in kilotonnes, as a positive number. ")
    if st.button("Check Answer", key=2):
        if validate_submission(user_submission_2, 2):
            st.success("Correct! Challenge #1 is complete.")
            is_challenge_2_complete = True
        else:
            st.error("Incorrect! Please try again.")
    

    st.subheader("Bonus Challenge: ")
    user_submission_3 = st.text_area("Write a prompt to identify which activity (power generation or pellet production) contributes more to nitrogen oxides (NOx) emissions per tonne of biomass used. Provide the name of the activity. ")
    if st.button("Check Answer", key=3):
        if validate_submission(user_submission_3, 3):
            st.success("Correct! Bonus Challenge is complete.")
            is_challenge_3_complete = True
        else:
            st.error("Incorrect! Please try again.")
            
    if st.button("Submit All Answers"):
        if validate_submission(user_submission_1, 1) and validate_submission(user_submission_2, 2) and validate_submission(user_submission_3, 3):
            st.success("Congratulations! You have completed all challenges. Please submit your feedback below.")
        else:
            st.warning("Please complete all challenges before submitting.")
    
    
    
    
    
    
    
    
    
    
    if is_challenge_1_complete and is_challenge_2_complete and is_challenge_3_complete:
        st.success("Congratulations! You have completed all challenges. Please submit your feedback below.")
        # Feedback form
        st.subheader("Workshop Feedback")
        with st.expander("Share Your Feedback"):
            email = st.text_input("Email Address")
            role = st.selectbox(
                "Your Role",
                ["Student", "Professional", "Academic", "Other"]
            )
            follow_up = st.selectbox(
                "Would you like to:",
                ["Receive workshop materials", "Join future workshops", "Connect with mentors", "None"]
            )
            feedback = st.text_area("Additional Comments")
            
            if st.button("Submit Feedback"):
                if email and feedback:
                    st.success("Thank you for your feedback!")
                else:
                    st.warning("Please fill in all required fields.")


        leaderboard = pd.DataFrame(get_sample_leaderboard())
        st.subheader("Leaderboard")
        st.dataframe(leaderboard)

# Add some styling
# st.markdown("""
# <style>
#     .stButton > button {
#         width: auto;
#     }
# </style>
# """, unsafe_allow_html=True)