from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct-1M",
    task="text-generation",
)
model = ChatHuggingFace(llm = llm)

output = model.invoke("what is the capital of india")
print(output.content)