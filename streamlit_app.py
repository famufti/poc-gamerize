# import streamlit as st

# # Styling for a kid-friendly and immersive experience
# st.set_page_config(page_title="Gamerize Learning App", layout="centered")
# st.markdown("""
#     <style>
#     .main {
#         background-color: #f0f8ff;
#         padding: 2rem;
#         border-radius: 1rem;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
#     }
#     h1 {
#         color: #ff6347;
#         font-family: 'Comic Sans MS', cursive;
#         text-align: center;
#     }
#     .stTextInput > div > input {
#         background-color: #fff8dc;
#         border: 2px solid #ff6347;
#         border-radius: 0.5rem;
#         padding: 0.5rem;
#     }
#     .stButton > button {
#         background-color: #ff6347;
#         color: white;
#         border: None;
#         font-weight: bold;
#         font-size: 1.2rem;
#         padding: 0.75rem 1.5rem;
#         border-radius: 1rem;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
#     }
#     </style>
# """, unsafe_allow_html=True)

# # App title
# st.title("🧩 Gamerize Learning POC")

# # Initialize session state for expected answers
# if "expected_answers" not in st.session_state:
#     st.session_state.expected_answers = []

# # Initialize session state for the new answer field
# if "new_answer" not in st.session_state:
#     st.session_state.new_answer = ""

# # Input fields
# Question = st.text_input("Enter your question here:")

# # Expected answers section with dynamic inputs
# st.subheader("Expected Answers")

# # Actual answer input
# Answer = st.text_input("Enter the actual answer:")

# # Submit button
# if st.button("Submit"):
#     # Check that mandatory fields are filled
#     if Question and Answer:
#         # Capture all variables
#         data = {
#             "question": Question,
#             "actual_answer": Answer
#         }
#         st.success("Data submitted successfully!")
#         st.write(data)
#     else:
#         st.error("Please fill out all fields before submitting.")


import streamlit as st
import requests

# Styling for a kid-friendly and immersive experience
st.set_page_config(page_title="Gamerize Learning App", layout="centered")
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    h1 {
        color: #ff6347;
        font-family: 'Comic Sans MS', cursive;
        text-align: center;
    }
    .stTextInput > div > input {
        background-color: #fff8dc;
        border: 2px solid #ff6347;
        border-radius: 0.5rem;
        padding: 0.5rem;
    }
    .stButton > button {
        background-color: #ff6347;
        color: white;
        border: None;
        font-weight: bold;
        font-size: 1.2rem;
        padding: 0.75rem 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("🧩 Gamerize Learning POC")

# Initialize session state for expected answers
if "expected_answers" not in st.session_state:
    st.session_state.expected_answers = []

# Initialize session state for the new answer field
if "new_answer" not in st.session_state:
    st.session_state.new_answer = ""

# Input fields
Question = st.text_input("Enter your question here:")

# Expected answers section with dynamic inputs
st.subheader("Expected Answers")

# Actual answer input
Answer = st.text_input("Enter the actual answer:")

# Submit button
if st.button("Submit"):
    # Check that mandatory fields are filled
    if Question and Answer:
        # Prepare data to send
        data = {
            "Question": Question,
            "Answer": Answer
        }
        
        # API endpoint
        api_url = "https://9qrchwwpqa.execute-api.us-west-2.amazonaws.com/dev/text-to-text-api"
        
        # Send data to the API endpoint
        try:
            response = requests.post(api_url, json=data)
            response_data = response.json()
            
            if response.status_code == 200:
                st.success("Data submitted successfully!")
                st.write("Response from API:", response_data)
            else:
                st.error(f"Error: {response.status_code}")
                st.write(response_data)
                
        except requests.exceptions.RequestException as e:
            st.error("Failed to connect to the API")
            st.write(f"Exception: {e}")
    else:
        st.error("Please fill out all fields before submitting.")
