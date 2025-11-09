from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv

model=ChatAnthropic(model='model_name')

result=model.invoke("what is capital of india")
print (result.content)
