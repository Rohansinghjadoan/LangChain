from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
modoel=ChatOpenAI(model="gpt-4",temperature=1.5,max_completion_tokens=10)#(Temperature)higher value creavite more ,max_completion_tokens(hw many tokens we want)
result=modoel.invoke("what is the capital of India?")

print(result.content)