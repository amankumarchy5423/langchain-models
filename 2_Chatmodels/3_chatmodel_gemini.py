from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-3.6-flash')

output = model.invoke("what is capital of india ")

print(output.content)