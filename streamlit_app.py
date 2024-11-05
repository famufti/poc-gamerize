# import streamlit as st
# import requests

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
#         # Prepare data to send
#         data = {
#             "Question": Question,
#             "Answer": Answer
#         }
        
#         # API endpoint
#         api_url = "https://9qrchwwpqa.execute-api.us-west-2.amazonaws.com/dev/text-to-text-api"
        
#         # Send data to the API endpoint
#         try:
#             response = requests.post(api_url, json=data)
#             response_data = response.json()
            
#             if response.status_code == 200:
#                 st.success("Data submitted successfully!")
                
#                 # Display the response in a more visually appealing way
#                 st.subheader("Response from API:")
#                 st.json(response_data)  # This will format the JSON nicely
                
#                 # Alternatively, display individual components with more styling
#                 st.markdown("### Evaluation Results")
#                 st.markdown(f"**Correctness:** {response_data['sample_responses']['Correctness']}")
#                 st.markdown(f"**Semantic Match:** {response_data['sample_responses']['Semantic Match']}")
#                 st.markdown(f"**Syntactic Structure:** {response_data['sample_responses']['Syntactic Structure']}")
#                 st.markdown(f"**Pragmatic Fit:** {response_data['sample_responses']['Pragmatic Fit']}")
                
#                 # Entities Identified
#                 st.markdown("### Entities Identified")
#                 entities = response_data['sample_responses']['Entities Identified']
#                 for entity, values in entities.items():
#                     st.markdown(f"**{entity}:** {', '.join(values)}")
                
#                 # Additional evaluation details
#                 st.markdown("### Rating and Evaluation")
#                 st.markdown(f"**Rating:** {response_data['sample_responses']['Rating']}")
#                 st.markdown(f"**Evaluation:** {response_data['sample_responses']['Evaluation']}")
                
#                 # Breakdown of the evaluation
#                 breakdown = response_data['sample_responses']['Breakdown of the evaluation']
#                 st.markdown("### Breakdown of the Evaluation")
#                 for criterion, explanation in breakdown.items():
#                     st.markdown(f"**{criterion}:** {explanation}")
                
#             else:
#                 st.error(f"Error: {response.status_code}")
#                 st.write(response_data)
                
#         except requests.exceptions.RequestException as e:
#             st.error("Failed to connect to the API")
#             st.write(f"Exception: {e}")
#     else:
#         st.error("Please fill out all fields before submitting.")

import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Gamerize Learning App", layout="centered")

# Add custom CSS for background and styling
st.markdown("""
    <style>
    body {
        background-image: url('https://example.com/your-background-image.jpg'); /* Replace with your image URL */
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .main {
        background-color: rgba(240, 248, 255, 0.8); /* Slightly transparent white for contrast */
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
    }
    h1 {
        color: #ff6347; /* Tomato color */
        font-family: 'Comic Sans MS', cursive;
        text-align: center;
    }
    h2, h3 {
        color: #ff4500; /* OrangeRed color */
        font-family: 'Comic Sans MS', cursive;
    }
    .stTextInput > div > input {
        background-color: #fff8dc; /* Cornsilk */
        border: 2px solid #ff6347; /* Tomato */
        border-radius: 0.5rem;
        padding: 0.5rem;
    }
    .stButton > button {
        background-color: #ff6347; /* Tomato */
        color: white;
        border: none;
        font-weight: bold;
        font-size: 1.2rem;
        padding: 0.75rem 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
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
        api_url = "https://9qrchwwpqa.execute-api.us-west-2.amazonaws.com/dev/api"
        
        # Send data to the API endpoint
        try:
            response = requests.post(api_url, json=data)
            response_data = response.json()
            
            if response.status_code == 200:
                st.success("Data submitted successfully!")
                
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
