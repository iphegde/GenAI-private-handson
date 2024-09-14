from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"  #Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

os.environ["LANGCHAIN_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a AWS Platform Engineer, Do not answer any other questions"),
        ("user", "Question:{question}")
    ]
)

#Streamlit

st.title("Langchain With OpenAI")
input_text=st.text_input("As me anything!")

#Open llm
llm=ChatOpenAI()
# llm.invoke("Hellow, World")
OutputParser=StrOutputParser()
chain=prompt|llm|OutputParser

if input_text:
   st.write(chain.invoke({'question':input_text}))