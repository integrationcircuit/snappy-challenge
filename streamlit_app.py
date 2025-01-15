import streamlit as st
import pandas as pd
from datetime import datetime
from typing import Dict, List

is_challenge_1_complete = False
is_challenge_2_complete = False

# Config and page setup
st.set_page_config(page_title="SnapLogic GenAI Workshop", layout="centered")

def get_credentials() -> Dict[str, str]:
    """Return mock credentials for the workshop."""
    return {
        "username": "workshop_user_2024",
        "password": "hackathon#123",
        "url": "https://cdn.emea.snaplogic.com/sl/designer.html?v=20842#pipe_snode=671221badb1d381136a8433d"
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
    
def validate_submission(submission: str) -> bool:
    """Validate user submission with mock rules."""
    return True

# Main app layout
st.title("SnapLogic GenAI Workshop Portal")

# Credentials section
st.subheader("Get Started")
team_name = st.text_input("Enter Your Team Name")
if len(team_name) > 0:
    if st.button("Get My Credentials"):
        creds = get_credentials()
        st.write("Here are your workshop credentials:")
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
    user_submission_1 = st.text_area("What’s the total group energy consumption in 2022?")
    user_submission_2 = st.text_area("Across all three years (2023, 2022, 2021), what’s the total nitrogen oxides generation?")
    if st.button("Submit"):
        if validate_submission(user_submission_1):
            st.success("Solution submitted successfully!")
            is_challenge_1_complete = True
        else:
            st.error("Invalid submission. Please check your solution.")

    if is_challenge_1_complete:
        with st.expander("Bonus Challenge"):
            user_submission_bonus = st.text_area("Bonus Challenge: Copy-Paste Your Solution Here")
            st.button("Submit Bonus Challenge")

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