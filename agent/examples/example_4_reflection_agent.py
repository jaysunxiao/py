import asyncio

from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

from agent.core.llm import HelloAgentsLLM
from agent.agents.reflection_agent import ReflectionAgent


def demo_reflection_agent():
    """演示ReflectionAgent - 自我反思与迭代优化"""
    print("\n" + "=" * 60)
    print("🔄 ReflectionAgent 演示 - 自我反思与迭代优化的Agent")
    print("=" * 60)

    # 创建LLM实例
    llm = HelloAgentsLLM()

    # 1. 默认配置演示
    print("\n--- 默认配置 ---")
    default_agent = ReflectionAgent(name="通用助手", llm=llm, max_iterations=2)

    task1 = "解释什么是递归算法，并给出一个简单的例子"
    print(f"\n🎯 任务: {task1}")
    try:
        response = asyncio.run(default_agent.run(task1))
        print(f"\n✅ 默认配置结果:\n{response}")
    except Exception as e:
        print(f"❌ 错误: {e}")

    # 2. 自定义配置演示 - 代码生成专家
    print("\n--- 自定义配置：代码生成专家 ---")
    code_prompts = {
        "initial": """
你是一位资深的程序员。请根据以下要求编写代码：

要求: {task}

请提供完整的代码实现，包含必要的注释和文档。
""",
        "reflect": """
你是一位严格的代码评审专家。请审查以下代码：

# 原始任务: {task}
# 待审查的代码: {content}

请分析代码的质量，包括算法效率、可读性、错误处理等。
如果代码质量良好，请回答"无需改进"。否则请提出具体的改进建议。
""",
        "refine": """
请根据代码评审意见优化你的代码：

# 原始任务: {task}
# 上一轮代码: {last_attempt}
# 评审意见: {feedback}

请提供优化后的代码。
""",
    }

    code_agent = ReflectionAgent(
        name="代码专家", llm=llm, custom_prompts=code_prompts, max_iterations=2
    )

    task2 = "编写一个Python函数，找出1到n之间所有的素数 (prime numbers)。"
    print(f"\n🎯 任务: {task2}")
    try:
        response = asyncio.run(code_agent.run(task2))
        print(f"\n✅ 代码专家结果:\n{response}")
    except Exception as e:
        print(f"❌ 错误: {e}")


demo_reflection_agent()
