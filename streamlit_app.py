import streamlit as st
import requests
import pandas as pd
# Set page configuration
st.set_page_config(page_title="Gamerize Learning App", layout="centered")

# Add custom CSS for background and styling
st.markdown("""
    <style>
    .main {
        background-color: rgba(240, 248, 255, 0.8); /* Slightly transparent white for contrast */
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
    }
    h1 {
        text-align: center;
    }
    h2, h3 {
        text-align: left;
    }
    .stTextInput > div > input {
        border: 2px solid #ccc; /* Light gray */
        border-radius: 0.5rem;
        padding: 0.5rem;
    }
    .stButton > button {
        color: white;
        border: 2px solid #ff4500; /* OrangeRed border */
        font-weight: bold;
        padding: 0.75rem 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("🧩 Gamerize Learning POC")
st.write("This POC allows users to answer open-ended questions from a mini game in a kids app, and get their answers evaluated as correct, incorrect or somewhat correct using a simple system using large language models. The app uses AWS services like Bedrock, Lambda and tries to use sentence similarity concepts like semantic similarity, pragmatic similarity etc.")

st.write("Simply pick a question from the dropdown and type an answer for it to evaluate its correctness and also give a detailed analysis for different types of sentence similarities.")
# Load questions from the CSV file
@st.cache_data
def load_questions():
    # Replace 'your_questions.csv' with your actual CSV file path
    df = pd.read_csv('questions.csv')
    return df['question'].tolist()

questions = load_questions()

# Initialize session state for expected answers
if "expected_answers" not in st.session_state:
    st.session_state.expected_answers = []

# Initialize session state for the new answer field
if "new_answer" not in st.session_state:
    st.session_state.new_answer = ""

# Question selection
Question = st.selectbox("Select a question:", questions)

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
                
                # Display the correctness prominently next to the submit button
                correctness = response_data['sample_responses']['Correctness']
                
                # Create columns for layout
                col1, col2 = st.columns([2, 3])  # Adjust the column widths as needed
                
                with col1:
                    # Display correctness message prominently on the left side
                    if correctness == "Correct":
                        st.markdown(f"<div style='padding: 10px; border-radius: 5px; background-color: #d4edda; color: #155724; font-weight: bold; text-align: center;'>Correct</div>", unsafe_allow_html=True)
                    elif correctness == "Incorrect":
                        st.markdown(f"<div style='padding: 10px; border-radius: 5px; background-color: #f8d7da; color: #721c24; font-weight: bold; text-align: center;'>Incorrect</div>", unsafe_allow_html=True)
                    elif correctness == "Somewhat Correct":
                        st.markdown(f"<div style='padding: 10px; border-radius: 5px; background-color: #fff3cd; color: #856404; font-weight: bold; text-align: center;'>Somewhat Correct</div>", unsafe_allow_html=True)

                with col2:
                    # Placeholder for any additional content you may want
                    st.markdown("")  # This can be left empty or used for other content
                
                
                # Display the response in a more visually appealing way
                st.subheader("Response from API:")
                st.markdown("<div style='padding: 10px; border-radius: 5px; background-color: rgba(255, 255, 255, 0.9);'>", unsafe_allow_html=True)
                st.json(response_data)  # This will format the JSON nicely
                st.markdown("</div>", unsafe_allow_html=True)

                # Detailed presentation of the response
                st.markdown("### Evaluation Results", unsafe_allow_html=True)
                st.markdown(f"**Correctness:** {response_data['sample_responses']['Correctness']}")
                st.markdown(f"**Semantic Match:** {response_data['sample_responses']['Semantic Match']}")
                st.markdown(f"**Syntactic Structure:** {response_data['sample_responses']['Syntactic Structure']}")
                st.markdown(f"**Pragmatic Fit:** {response_data['sample_responses']['Pragmatic Fit']}")

                # Entities Identified
                st.markdown("### Entities Identified")
                entities = response_data['sample_responses']['Entities Identified']
                for entity, values in entities.items():
                    st.markdown(f"**{entity}:** {', '.join(values)}")

                # Additional evaluation details
                st.markdown("### Rating and Evaluation")
                st.markdown(f"**Rating:** {response_data['sample_responses']['Rating']}")
                st.markdown(f"**Evaluation:** {response_data['sample_responses']['Evaluation']}")

                # Breakdown of the evaluation
                st.markdown("### Breakdown of the Evaluation")
                breakdown = response_data['sample_responses']['Breakdown of the evaluation']
                for criterion, explanation in breakdown.items():
                    st.markdown(f"**{criterion}:** {explanation}")
                
            else:
                st.error(f"Error: {response.status_code}")
                st.write(response_data)
                
        except requests.exceptions.RequestException as e:
            st.error("Failed to connect to the API")
            st.write(f"Exception: {e}")
    else:
        st.error("Please fill out all fields before submitting.")
