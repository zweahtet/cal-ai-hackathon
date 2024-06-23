import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()

# LLMs
llama_3_8b_llm_groq = ChatGroq(
    temperature=0.0, model="llama3-8b-8192", api_key=os.getenv("GROQ_API")
)

llama_3_70b_llm_groq = ChatGroq(
    temperature=0.0, model="llama3-70b-8192", api_key=os.getenv("GROQ_API")
)

mixtral_8x7b_llm_groq = ChatGroq(
    temperature=0.0, model="mixtral-8x7b-32768", api_key=os.getenv("GROQ_API")
)

gpt4_turbo_llm_openai = ChatOpenAI(
    temperature=0.0, model="gpt-4-turbo", api_key=os.getenv("OPENAI_API_KEY")
)
