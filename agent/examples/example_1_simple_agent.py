import asyncio

from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

from agent.core.llm import HelloAgentsLLM
from agent.agents.simple_agent import SimpleAgent


async def demo_simple_agent():
    """演示SimpleAgent - 基础对话"""
    print("\n" + "="*60)
    print("🤖 SimpleAgent 演示 - 基础对话Agent")
    print("="*60)

    # 创建LLM实例
    llm = HelloAgentsLLM()

    # 创建简单Agent
    agent = SimpleAgent(
        name="助手",
        llm=llm,
        system_prompt="你是一个有用的AI助手，请用中文回答问题。"
    )

    # 测试对话
    test_questions = [
        "你好，请介绍一下自己",
        "什么是人工智能？",
        "请用一句话总结机器学习的核心思想"
    ]

    for question in test_questions:
        print(f"\n用户: {question}")
        try:
            response = await agent.run(question)
            print(f"助手: {response}")
        except Exception as e:
            print(f"❌ 错误: {e}")


# 1. SimpleAgent演示
asyncio.run(demo_simple_agent())