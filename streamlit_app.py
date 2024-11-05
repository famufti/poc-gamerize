# import streamlit as st

# st.title("🎈 My new app")
# st.write(
#     "Let's start building app for Hassaan Mahboob.Hello G For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st

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

# Input fields
question = st.text_input("Enter your question here:")

# Expected answers section with dynamic inputs
st.subheader("Expected Answers")
expected_answers = []
new_answer = st.text_input("Add an expected answer")

# Button to add expected answers to the list
if st.button("➕ Add Expected Answer"):
    expected_answers.append(new_answer)
    st.experimental_rerun()

# Display added answers
for i, ans in enumerate(expected_answers):
    st.write(f"{i+1}. {ans}")

# Actual answer input
actual_answer = st.text_input("Enter the actual answer:")

# Submit button
if st.button("Submit"):
    # Check that mandatory fields are filled
    if question and expected_answers and actual_answer:
        # Capture all variables
        data = {
            "question": question,
            "expected_answers": expected_answers,
            "actual_answer": actual_answer
        }
        st.success("Data submitted successfully!")
        st.write(data)
    else:
        st.error("Please fill out all fields before submitting.")
