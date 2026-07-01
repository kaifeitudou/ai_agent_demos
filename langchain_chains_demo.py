from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from models import *

# make prompt
prompt = ChatPromptTemplate.from_template("请用简洁的语言解释什么是{topic}?")

# make chain
# prompt -> llm -> output text
chain = prompt | qwen | StrOutputParser()

# run chain and print result
response = chain.invoke({"topic": "爱屋及乌"})
print("===模型回复===")
print(response)