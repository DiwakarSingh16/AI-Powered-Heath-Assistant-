import streamlit as st 
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

chatbot=pipeline("text-generation",model='distilgpt2')

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please Consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule appointment with the Doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly."
    else:
        response=chatbot(user_input,max_length = 500,num_return_sequences=1)

    return response[0]['generated_text']
def main():
     # Inject custom CSS for background image and footer
    st.markdown(
        """
        <style>
        /* Full page background with blur */
        .stApp {
            background-image: url('https://www.shutterstock.com/shutterstock/videos/3592163003/thumb/12.jpg?ip=x480');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }

        /* Overlay to blur only the background */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            backdrop-filter: blur(5px); /* Blurs only the background image */
            z-index: -1; /* Keeps it in the background */
        }

        /* App content styling */
        .block-container {
            background-color: rgba(255, 255, 255, 0.85); /* Semi-transparent background for content */
            padding: 20px;
            border-radius: 10px;
        }

        /* Footer styling */
        footer {
            text-align: center;
            margin-top: 50px;
            font-size: 14px;
            color: #555;
        }

        footer a {
            text-decoration: none;
            color: #007BFF;
            font-weight: bold;
        }

        footer a:hover {
            color: #0056b3;
            text-decoration: underline;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("AI-Powered Health Assistant")
    user_input=st.text_input("How can I assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User : ",user_input)
            with st.spinner("Processing your query ..."):
              response=healthcare_chatbot(user_input)
            st.write("Healthcare Assistant :",response)
        else:
            st.write("Please enter a message to get a response.")

         # Add footer with name, LinkedIn, and GitHub links
    st.markdown(
        """
        <footer>
            <p>Developed by <strong>DIWAKAR SINGH</strong></p>
            <p>
                <a href="https://www.linkedin.com/in/diwakar-singh-328981293/" target="_blank">LinkedIn</a> |
                <a href="https://github.com/DiwakarSingh16/Diwakar.github.io" target="_blank">GitHub</a>
            </p>
        </footer>
        """,
        unsafe_allow_html=True,
    )



if __name__ == "__main__":
    main()