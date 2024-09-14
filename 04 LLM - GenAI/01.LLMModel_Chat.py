from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI  #Chat Model
from langchain_openai import OpenAI   #LLM Model

import os
from dotenv import load_dotenv
load_dotenv()

# print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

SECRET_KEY = os.getenv("OPENAI_API_KEY")

#LLM Model 
#llm = OpenAI(api_key=SECRET_KEY)
#print(llm.invoke("Who is PM of India?"))


Chat = ChatOpenAI(api_key=SECRET_KEY, model_name= 'gpt-4o')

message = [
    SystemMessage(content='Act like CEO of Google'),
    HumanMessage(content='Can you please tell me what is the current number of employees in Deepminds')
]

res = Chat.invoke(message)
print(res)

# # HumanMessage=



# # SystemMessage





