from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI(model = 'gpt-4', temprature = 0.4)

output = model.invoke('capital of india ')

print(output)