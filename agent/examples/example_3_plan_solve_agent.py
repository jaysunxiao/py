import asyncio

from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

from agent.core.llm import HelloAgentsLLM
from agent.agents.plan_solve_agent import PlanAndSolveAgent


def demo_plan_solve_agent():
    """演示PlanAndSolveAgent - 分解规划与逐步执行"""
    print("\n" + "=" * 60)
    print("📋 PlanAndSolveAgent 演示 - 分解规划与逐步执行的Agent")
    print("=" * 60)

    # 创建LLM实例
    llm = HelloAgentsLLM()

    # 1. 默认配置演示
    print("\n--- 默认配置 ---")
    default_agent = PlanAndSolveAgent(name="通用助手", llm=llm)

    task1 = "如何学习Python编程？请制定一个详细的学习计划。"
    print(f"\n🎯 任务: {task1}")
    try:
        response = asyncio.run(default_agent.run(task1))
        print(f"\n✅ 默认配置结果:\n{response}")
    except Exception as e:
        print(f"❌ 错误: {e}")

    # 2. 自定义配置演示 - 数学问题专家
    print("\n--- 自定义配置：数学问题专家 ---")
    math_prompts = {
        "planner": """
你是一个数学问题分解专家。请将以下数学问题分解为清晰的计算步骤。
每个步骤应该是一个具体的数学运算或逻辑推理。

数学问题: {question}

请按以下格式输出计算计划:
```python
["步骤1: 具体计算", "步骤2: 具体计算", ...]
```
""",
        "executor": """
你是一个数学计算专家。请严格按照计划执行数学计算。

# 原始问题: {question}
# 计算计划: {plan}
# 已完成的计算: {history}
# 当前计算步骤: {current_step}

请执行当前步骤的计算，只输出计算结果:
""",
    }

    math_agent = PlanAndSolveAgent(
        name="数学专家", llm=llm, custom_prompts=math_prompts
    )

    task2 = "一个水果店周一卖出了15个苹果。周二卖出的苹果数量是周一的两倍。周三卖出的数量比周二少了5个。请问这三天总共卖出了多少个苹果？"
    print(f"\n🎯 任务: {task2}")
    try:
        response = asyncio.run(math_agent.run(task2))
        print(f"\n✅ 数学专家结果:\n{response}")
    except Exception as e:
        print(f"❌ 错误: {e}")


# 4. PlanAndSolveAgent演示（默认 + 自定义）
demo_plan_solve_agent()
