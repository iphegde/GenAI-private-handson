from gen_ai_hub.proxy.langchain.openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

# Get all the env variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"  #Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]= os.getenv("LANGCHAIN_PROJECT")

os.environ["AICORE_AUTH_URL"] = os.getenv("AICORE_AUTH_URL")
os.environ["AICORE_CLIENT_ID"] = os.getenv("AICORE_CLIENT_ID")
os.environ["AICORE_CLIENT_SECRET"] = os.getenv("AICORE_CLIENT_SECRET")
os.environ["AICORE_RESOURCE_GROUP"] = os.getenv("AICORE_RESOURCE_GROUP")
os.environ["AICORE_BASE_URL"] = os.getenv("AICORE_BASE_URL")

prompt = ChatPromptTemplate.from_messages(
        {
          ("system","you are an experienced SAP ABAP Developer, Only answer ABAP related questions"),
          ("user","Question:{question}")      
        }
)


st.title("SAP GenAI Hub Based Chatbot")
input_text=st.text_input("you can ask about ABAP!")

llm = ChatOpenAI(deployment_id=os.getenv("LLM_DEPLOYMENT_ID"))
output_parser=StrOutputParser()
Chain = prompt|llm|output_parser

if input_text:
    st.write(Chain.invoke({"question":input_text}))