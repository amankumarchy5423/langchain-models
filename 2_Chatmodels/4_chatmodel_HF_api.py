from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",  # or another provider-backed model
    task="text-generation",
)

# llm1 = HuggingFaceEndpoint(
#     repo_id = 'mvp-lab/MiniMax-H3-RAVEN-Streaming-LoRA',
#     task = 'Text-to-Video'
# )
model = ChatHuggingFace(llm=llm)

output = model.invoke("tell some line on nit silchar ")
print(output.content)