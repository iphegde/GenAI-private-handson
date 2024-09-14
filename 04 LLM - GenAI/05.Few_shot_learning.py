from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()



SECRET_KEY=os.getenv("OPENAI_API_KEY")
llm = OpenAI(openai_api_key=SECRET_KEY)



# LLMs
# Few Shot Examples
examples = [
    {
        "input": "give me all the sales order created today with the Sales order number, materials(items) and price",
        "output": "SELECT VBELN, MATNR, NETWR from VBAP where ERDAT = '31-05-2024'"
    },
    {
        "input": "show me the total purchase orders for today",
        "output": "SELECT SUM(EKKO.NETWR) AS total_purchase_order_amount_today FROM EKKO WHERE EKKO.BEDAT = CURRENT_DATE"
    },

    {
        "input": "what are the meetings today",
        "output": "SELECT meeting_name from nexgen_meetings where schedule_date = '31-05-2024'"
    },    
]


example_prompt = PromptTemplate(
    input_variables=["input", "output"], template="{input}\n{output}"
)



prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="{myiinput}",
    input_variables=["myiinput"]
)


myprompt = prompt.format(
    # myinput="total purchase order for this month"
    # myinput="list all the customer bought products this month"
    myiinput="how many meeting I have during 2pm to 4pm today"
)

# print("My Prompt: ", myprompt)
response = llm.invoke(myprompt)
print("Response: ", response)
