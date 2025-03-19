import streamlit as st
import pandas as pd
from datetime import datetime
from typing import Dict, List
import requests
import json
import feedback as fd



showcase_url = "https://snaplogic-genai-builder.streamlit.app/"

if "challenge_1_complete" not in st.session_state:
    st.session_state["challenge_1_complete"] = False
if "challenge_2_complete" not in st.session_state:
    st.session_state["challenge_2_complete"] = False
if "challenge_3_complete" not in st.session_state:
    st.session_state["challenge_3_complete"] = False
if "all_challenges_complete" not in st.session_state:
    st.session_state["all_challenges_complete"] = False

# Config and page setup
st.set_page_config(page_title="SnapLogic GenAI Workshop", layout="centered")

def get_credentials() -> Dict[str, str]:
    """Return mock credentials for the workshop."""
    url = "https://emea.snaplogic.com/api/1/rest/slsched/feed/ConnectFasterInc/0_StanGPT/StanCoE/Workshops_RetrieveCredentialsForUserApi"
    bearer = "oRCpXlz9ztv4xvxi9KcqsMmo3R7H96Ht"
    headers = {
        "Authorization": f"Bearer {bearer}",
        "Content-Type": "application/json"
    }
    
    print(st.session_state['user_email'])
    response = requests.get(
        url,
        headers=headers,
        params={"useremail": st.session_state['user_email']}
    )
    
    response.raise_for_status()
    data = response.json()[0]
    print(data)
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
    if "credentials_available" not in st.session_state:
        st.session_state["credentials_available"] = True
    
    return {
        "username": username,
        "password": password,
        "url": url
    }

def get_workshop_tips() -> List[str]:
    """Return workshop tips."""
    return [
        "Click on the \"Prompt Generator\" Snap to edit your prompt (the Yellow icon) that says EDIT HERE",
        "Try different types of questions to get a desired result - slight change in wording can have... interesting outcomes",
        "When viewing a data preview (light green icon at the end of our process), click \"Formatted\" for better readability",
        "Ask questions in the chast - your hosts are here to help",
        "If the LLM gets overwhelmed and is not responding or erroring out, wait a minute and try again"
    ]
    
def validate_submission(submission: str, challenge: int) -> bool:
    """Validate user submission with mock rules."""
    if challenge == 1.1:
        return "small bronze lamp" in submission.lower()
    if challenge == 1.2:
        return "small bronze lamp" in submission.lower()
    if challenge == 2.1: 
        return "123456880" in submission.lower()
    if challenge == 2.2:
        return "123456882" in submission.lower()
    if challenge == 3.1:
        return "lowe" in submission.lower() and "hane" in submission.lower() and "bergstrom" in submission.lower() and "75" in submission.lower() and "371" in submission.lower() and "over" in submission.lower() and "123456880" in submission.lower()
    if challenge == 3.2:
        return "legros" in submission.lower() and "group" in submission.lower() and "59" in submission.lower() and "257" in submission.lower() and "under" in submission.lower() and "123456882" in submission.lower()
    return True


# Main app layout
st.title("SnapLogic GenAI Workshop Portal")

# Credentials section
st.subheader("Get Started")
user_email = st.text_input("Enter Your Emaiil Address (that you used to register for the workshop)")
# if "user_email" not in st.session_state:
st.session_state['user_email'] = user_email.strip()
if len(user_email) > 0:
    if st.button("Get My Credentials"):
        if "user_email" not in st.session_state:
            st.session_state['user_email'] = user_email
        try: 
            creds = get_credentials()
            st.write("Here are your workshop credentials (do not refresh this page or they will disappear):")
            st.write(f"Username: {creds['username']}")
            st.write(f"Password: {creds['password']}")
            st.link_button("Login", url=creds['url'])
        except:
            st.error("No credentials found for this email. Please check your email and try again.")

    # Document preview
    # st.subheader("Workshop Materials")
    # st.link_button("Preview Workshop Materials", url="https://www.drax.com/wp-content/uploads/2024/03/Final-Signed-ESG-2023-Supplement.pdf")
    # Tips section
    

            
    # with st.expander("Sample Prompts"):
    #     for prompt in get_sample_prompts():
    #         st.write(prompt)

    # Submission form
    st.divider()
    st.subheader("Your Tasks Start Here")
    
    with st.expander("Tips (click to expand)"):
        for tip in get_workshop_tips():
            st.markdown(f"• {tip}")
    
    st.subheader("Challenge #1")
    st.divider()
    st.write("Your first task is to use the provided invoice and report the product name with the most items invoiced, as well as the product name with the highest total cost in the invoice.")
    st.write("Use the following invoice to answer the questions:")
    st.link_button("View Invoice", url="https://escaperoom.snapdemo.site/game/invoice/cb249e16-8c3f-4225-a679-4b0e46dea7ef")
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        user_submission_1_1 = st.text_input("Product Name with the largest items count")
    with col2:
        user_submission_1_2 = st.text_input("Product Name with the highest total cost")
    
    if st.button("Check Answer", key=1):
        if validate_submission(user_submission_1_1, 1.1) and validate_submission(user_submission_1_2, 1.2):
            # st.success("Correct! Challenge #1 is complete.")
            # is_challenge_1_complete = True
            st.session_state["challenge_1_complete"] = True
        else:
            st.error("Incorrect! Please try again.")
    
    if st.session_state["challenge_1_complete"]:
        st.success("Success! Challenge 1 Done.")
    st.divider()
    
    st.subheader("Challenge #2")
    st.write("Your second task is to look through all of your invoices to identify the invoices where the total cost of products does not match the total charged invoice price.")
    st.write("You have been overcharged in one invoice and undercharged in one invoice.")
    st.write("You need to identify the invoice where you were overcharged (charged amount was more than the total product cost) and identify the invoice where you were undercharged (charged amount was less than the total product cost)")
    st.write("Once done, submit the corresponding invoice ID into the appropriate field to continue.")
    st.write("Use the following invoices to answer the questions:")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.link_button("View Invoice", url="https://escaperoom.snapdemo.site/game/invoice/cb249e16-8c3f-4225-a679-4b0e46dea7ef")
    with col2:
        st.link_button("View Invoice", url="https://escaperoom.snapdemo.site/game/invoice/cb249e16-8c3f-4225-a679-4b0e46dea7ef")
    with col3:
        st.link_button("View Invoice", url="https://escaperoom.snapdemo.site/game/invoice/cb249e16-8c3f-4225-a679-4b0e46dea7ef")
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        user_submission_2_1 = st.text_input("Overcharged Invoice ID")
    with col2:
        user_submission_2_2 = st.text_input("Undercharged Invoice ID")
    if st.button("Check Answer", key=2):
        if validate_submission(user_submission_2_1, 2.1) and validate_submission(user_submission_2_2, 2.2):
            # st.success("Correct! Challenge #2 is complete.")
            # is_challenge_2_complete = True
            st.session_state["challenge_2_complete"] = True
        else:
            st.error("Incorrect! Please try again.")
    
    if st.session_state["challenge_2_complete"]:
        st.success("Success! Challenge 2 Done,")
    st.divider()

    st.subheader("Challenge #3")
    st.write("Your third task is to put together an email to send to your suppliers (named in the invoices) who you overpaid and underpaid")
    st.write("This message should elaborate how you will pay them the difference in the product cost and charged amount or how you expect to get reimbursement for the overpayment.")
    st.write("Your email body should include the customer's name, the invoice ID, the total cost that should have been charged, and the charged amount.")
    st.divider()
    
    user_submission_3_1 = st.text_area("Overpaid Supplier Email Body")
    user_submission_3_2 = st.text_area("Underpaid Supplier Email Body")
    if st.button("Check Answer", key=3):
        if validate_submission(user_submission_3_1, 3.1) and validate_submission(user_submission_3_2, 3.2):
            # st.success("Correct! Challenge #3 is complete.")
            # is_challenge_3_complete = True
            st.session_state["challenge_3_complete"] = True
        else:
            st.error("Incorrect! Please try again.")
            
    if st.session_state["challenge_3_complete"]:
        st.success("Success! Challenge 3 Done.")
    st.divider()
            
    if st.button("Submit All Answers"):
        if validate_submission(user_submission_1_1, 1.1) and validate_submission(user_submission_1_2, 1.2) and validate_submission(user_submission_2_1, 2.1) and validate_submission(user_submission_2_2, 2.2) and validate_submission(user_submission_3_1, 3.1) and validate_submission(user_submission_3_2, 3.2):
            st.session_state["all_challenges_complete"] = True
            
        else:
            st.warning("Please complete all challenges before submitting.")
    
    if st.session_state["all_challenges_complete"]:
        st.divider()
        st.success("Congratulations! You have completed all challenges. Please submit your feedback below.")
        st.info("We enrourage you to experiment with SnapLogic and explore the data further - find the most interesting question to be answered by AI.")
        fd.show_registration_form(st.session_state['user_email'])
        
    
    
    
    
    
    
    
    # if st.session_state["challenge_1_complete"] and st.session_state["challenge_2_complete"]  and st.session_state["challenge_3_complete"] :
    
    
 
    #     st.success("Congratulations! You have completed all challenges. Please submit your feedback below.")
    #     # Feedback form
    #     st.subheader("Workshop Feedback")
    #     with st.expander("Share Your Feedback"):
    #         email = st.text_input("Email Address")
    #         role = st.selectbox(
    #             "Your Role",
    #             ["Student", "Professional", "Academic", "Other"]
    #         )
    #         follow_up = st.selectbox(
    #             "Would you like to:",
    #             ["Receive workshop materials", "Join future workshops", "Connect with mentors", "None"]
    #         )
    #         feedback = st.text_area("Additional Comments")
            
    #         if st.button("Submit Feedback"):
    #             if email and feedback:
    #                 st.success("Thank you for your feedback!")
    #             else:
    #                 st.warning("Please fill in all required fields.")


    #     leaderboard = pd.DataFrame(get_sample_leaderboard())
    #     st.subheader("Leaderboard")
    #     st.dataframe(leaderboard)

# Add some styling
# st.markdown("""
# <style>
#     .stButton > button {
#         width: auto;
#     }
# </style>
# """, unsafe_allow_html=True)