from langchain.agents import create_agent
from langchain_core.tools import tool
from models import *

# define tool
@tool()
def multiply(a: int, b: int) -> int:
    """将两个整数相乘。当你需要计算两个数的乘积时，使用此工具"""
    return a*b

@tool()
def add(a: int, b: int) -> int:
    """将两个整数相加。当你需要计算两个数的和时，使用此工具"""
    return a+b

# add tool into the list
tools = [multiply, add]

# 创建agent
agent = create_agent(qwen, tools=tools, system_prompt="你是一个乐于助人的数学助手。")

inputs = {"messages": [{"role": "user", "content": "3乘以4等于多少，再加上20是多少？"}]}
response = agent.invoke(inputs)

print("\n===最终回复===")
print(response)