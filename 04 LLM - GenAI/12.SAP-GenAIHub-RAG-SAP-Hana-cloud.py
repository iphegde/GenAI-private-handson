from gen_ai_hub.proxy.langchain.openai import ChatOpenAI
from gen_ai_hub.proxy.langchain.openai import OpenAIEmbeddings

from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain_community.vectorstores.hanavector import HanaDB
from hdbcli import dbapi

import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
# os.environ[""]= os.getenv("")

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

user=os.getenv("user")
password=os.getenv("password")
host=os.getenv("host")
database=os.getenv("database")

url=os.getenv("url")
port=os.getenv("port")


os.environ["AICORE_AUTH_URL"] = os.getenv("AICORE_AUTH_URL")
os.environ["AICORE_CLIENT_ID"] = os.getenv("AICORE_CLIENT_ID")
os.environ["AICORE_CLIENT_SECRET"] = os.getenv("AICORE_CLIENT_SECRET")
os.environ["AICORE_RESOURCE_GROUP"] = os.getenv("AICORE_RESOURCE_GROUP")
os.environ["AICORE_BASE_URL"] = os.getenv("AICORE_BASE_URL")

llm = ChatOpenAI(deployment_id= os.getenv("LLM_DEPLOYMENT_ID"))

# Use connection settings from the environment
connection = dbapi.connect(
    address=url,
    port=port,
    user=user,
    password=password,
    autocommit=True,
    sslValidateCertificate=False,
)


pdfloader = PyPDFLoader("./mgi_big_data_exec_summary.pdf")


documents = pdfloader.load()


TextSplitter = CharacterTextSplitter(chunk_size=500,chunk_overlap=50)


texts = TextSplitter.split_documents(documents)
print(f"Number of document chunks: {len(texts)}")

embeddings = OpenAIEmbeddings(deployment_id=os.getenv("EMB_DEPLOYMENT_ID"))


db = HanaDB(
    embedding=embeddings, connection=connection, table_name="ZAI_RAG_MCKINSEY"
)

db.delete(filter=[])
db.add_documents(texts)


retriever = db.as_retriever()


qa = RetrievalQA.from_llm(llm=llm, retriever=retriever)

query = st.text_input("Enter your Query:")

if st.button("Submit"):
    if query:
        response = qa(query)
        st.write("*** Response ***")
        st.write(response['result'])
    else:
        st.write("Please enter your query")