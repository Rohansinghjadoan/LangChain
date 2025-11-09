from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
lmm=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model=ChatHuggingFace(llm=lmm)
result=model.invoke('why my hugging face model is not working with api ')
print(result.content)