from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()


SECRET_KEY=os.getenv("OPENAI_API_KEY")
# llm = OpenAI(openai_api_key=SECRET_KEY)
chat = ChatOpenAI(openai_api_key=SECRET_KEY)

# Chat Model
# Few Shot Examples
examples = [
    {"input": "2+2", "output": "4"},
    {"input": "2+3", "output": "5"},
]

example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}"),
])
# print("Example Prompt: ", example_prompt)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt
)

# print("Few Shot Prompt: ", few_shot_prompt.format())

final_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful math problem solver."),
    few_shot_prompt,
    ("human", "{input}"),
])

# print("Final Prompt: ", final_prompt)

formattedChatPrompt = final_prompt.format_messages(
    input="What's the square of a triangle?"
)
# print("Formatted Chat Prompt: ", formattedChatPrompt)

response = chat.invoke(formattedChatPrompt)
print("Response Content: ", response.content)
