from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
document=[
    'Delhi is capital of India ',
    'kolkata is a capital of west bangal',
    'paris is a capital of France'

]
result=embedding.embed_query(document)
print(str(result))