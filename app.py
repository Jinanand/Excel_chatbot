# chatbot_excel_analyzer

import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent


# Load .env file
load_dotenv()

st.markdown("""
    <style>
        .main { background-color: #f8f9ea; }
        h1 { color: #4b4b4f; }
    </style>
""", unsafe_allow_html=True)


# Streamlit page configuration
st.set_page_config(page_title="Excel Analyzer Chatbot", page_icon="🤖")
st.title("Excel Analyzer Chatbot")

# Upload Excel file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

# Main logic
if uploaded_file is not None:
    try:
        # Read Excel file
        df = pd.read_excel(uploaded_file)
        st.success("File uploaded successfully!")
        st.dataframe(df.head())

        # Initialize Groq LLM
        groq_api_key = os.getenv("GROQ_API_KEY")
        llm = ChatGroq(temperature=0, model_name="llama3-8b-8192", api_key=groq_api_key)

        # Create agent
        agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)

        # Query input
        st.subheader("Ask me anything about your data")
        query = st.text_input("Your question:", placeholder="e.g., How many rows and columns are there?")

        if query:
            with st.spinner("Analyzing..."):
                try:
                    response = agent.run(query)

                    # Display text response
                    if isinstance(response, pd.DataFrame):
                        st.dataframe(response)
                    elif isinstance(response, str):
                        st.write(response)

                    # Show plots if created
                    st.pyplot(plt)  # display current matplotlib figure

                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

    except Exception as e:
        st.error(f"❌ Failed to read Excel file: {str(e)}")
else:
    st.info("Please upload an Excel file to begin.")
