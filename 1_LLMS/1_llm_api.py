from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


llm = OpenAI(model = 'gpt-3.5-turbo-instruct')


print(llm.invoke("capital of USA"))

# 1_LLMS/1_llm_api.py
# /workspaces/langchain-models/1_LLMS/1_llm_api.py