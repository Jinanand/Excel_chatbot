# Excel_chatbot
This is an interactive Excel Analyzer Chatbot built with **Streamlit**, **LangChain**, and **Groq's LLaMA3 LLM**. It allows users to upload any Excel file and ask natural language questions about the data, with responses powered by a large language model.
## Tech Stack

- [Python](https://www.python.org/)
  The core programming language used for writing the entire backend of the application
- [Streamlit](https://streamlit.io/)
  Frontend framework for building the web-based user interface
  Streamlit makes it easy to build interactive data apps in Python with very little code. It handles file uploads, button clicks, and displays chat and plots.
- [LangChain](https://www.langchain.com/)
  Provides an interface to connect language models with tools like Pandas or plotting libraries
  It simplifies chaining LLMs with data (agents/tools), enabling natural language interaction with structured data like Excel
- [Groq LLaMA3](https://groq.com/)
  The large language model (LLM) backend that understands and responds to user queries
  Groq provides fast inference using Meta's LLaMA3 model, enabling rapid natural language processing and reasoning over your data
- [dotenv](https://pypi.org/project/python-dotenv/)
  Loads sensitive data (like API keys) from a .env file into environment variables
  To securely manage API keys without hardcoding them into the codebase
- [pandas](https://pandas.pydata.org/)
  Core data manipulation library used to read and process Excel files
- [matplotlib](https://matplotlib.org/)
  Used to create plots and graphs based on the Excel data
- [seaborn](https://seaborn.pydata.org/)
  High-level interface for making attractive and informative statistical graphics
