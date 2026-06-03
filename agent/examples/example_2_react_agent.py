import asyncio

from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

from agent.agents.react_agent import ReActAgent
from agent.core.llm import HelloAgentsLLM
from agent.tools.builtin.calculator import calculate
from agent.tools.builtin.search_tool import search
from agent.tools.registry import ToolRegistry


def demo_react_agent():
    """演示ReActAgent - 推理与行动结合"""
    print("\n" + "=" * 60)
    print("🔧 ReActAgent 演示 - 推理与行动结合的Agent")
    print("=" * 60)

    # 创建LLM实例
    llm = HelloAgentsLLM()

    # 创建工具注册表
    tool_registry = ToolRegistry()

    # 注册工具
    tool_registry.register_function(
        name="search",
        description="一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。",
        func=search,
    )

    tool_registry.register_function(
        name="calculate",
        description="执行数学计算。支持基本运算、数学函数等。例如：2+3*4, sqrt(16), sin(pi/2)等。",
        func=calculate,
    )

    # 1. 默认配置演示
    print("\n--- 默认配置 ---")
    default_agent = ReActAgent(
        name="通用助手", llm=llm, tool_registry=tool_registry, max_steps=3
    )

    task1 = "计算 15 * 23 + 45 的结果"
    print(f"\n🎯 任务: {task1}")
    try:
        response = asyncio.run(default_agent.run(task1))
        print(f"\n✅ 默认配置结果: {response}")
    except Exception as e:
        print(f"❌ 错误: {e}")

    # 2. 自定义配置演示 - 研究助手
    print("\n--- 自定义配置：研究助手 ---")
    research_prompt = """
你是一个专业的研究助手，擅长信息收集和分析。

可用工具如下：
{tools}

请按照以下格式进行研究：

Thought: 分析问题，确定需要什么信息，制定研究策略。
Action: 选择合适的工具获取信息，格式为：
- `{{tool_name}}[{{tool_input}}]`：调用工具获取信息。
- `Finish[研究结论]`：当你有足够信息得出结论时。

研究问题：{question}
已完成的研究：{history}
"""

    research_agent = ReActAgent(
        name="研究助手",
        llm=llm,
        tool_registry=tool_registry,
        custom_prompt=research_prompt,
        max_steps=3,
    )

    task2 = "搜索一下最新的人工智能发展趋势"
    print(f"\n🎯 任务: {task2}")
    try:
        response = asyncio.run(research_agent.run(task2))
        print(f"\n✅ 研究助手结果: {response}")
    except Exception as e:
        print(f"❌ 错误: {e}")


# 2. ReActAgent演示（默认 + 自定义）
demo_react_agent()
