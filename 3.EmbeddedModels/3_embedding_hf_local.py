from langchain_huggingface import HuggingFaceEmbeddings

embedidings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
text='delhi is a capital of india'
vector=embedidings.embed_query(text)
print(str(vector))