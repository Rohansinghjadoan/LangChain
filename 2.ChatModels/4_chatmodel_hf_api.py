from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of India?")
print(response.content)
