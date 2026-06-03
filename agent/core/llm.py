"""HelloAgents统一LLM接口 - 基于OpenAI原生API"""

import os
from collections.abc import Iterator

from openai import OpenAI

from .exceptions import HelloAgentsException


class HelloAgentsLLM:
    """
    为HelloAgents定制的LLM客户端。
    它用于调用任何兼容OpenAI接口的服务，并默认使用流式响应。

    设计理念：
    - 参数优先，环境变量兜底
    - 流式响应为默认，提供更好的用户体验
    - 通过 api_key / base_url 或 LLM_* 环境变量统一配置
    """

    model: str
    temperature: float
    max_tokens: int | None
    timeout: int
    api_key: str
    base_url: str
    _client: OpenAI

    def __init__(
        self,
        model: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        temperature: float = 0.7,
        max_tokens: int | None = None,
        timeout: int | None = None,
    ):
        """
        初始化客户端。优先使用传入参数，如果未提供，则从环境变量加载。

        Args:
            model: 模型名称，如果未提供则从环境变量 LLM_MODEL_ID 读取
            api_key: API密钥，如果未提供则从环境变量读取
            base_url: 服务地址，如果未提供则从环境变量 LLM_BASE_URL 读取
            temperature: 温度参数
            max_tokens: 最大token数
            timeout: 超时时间，从环境变量 LLM_TIMEOUT 读取，默认60秒
        """
        self.model = model or os.getenv("LLM_MODEL_ID") or "gpt-3.5-turbo"
        self.api_key = api_key or os.getenv("LLM_API_KEY") or ""
        self.base_url = base_url or os.getenv("LLM_BASE_URL") or "https://api.openai.com/v1"
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout or int(os.getenv("LLM_TIMEOUT", "60"))

        if not all([self.api_key, self.base_url]):
            raise HelloAgentsException("API密钥和服务地址必须被提供或在.env文件中定义。")

        self._client = OpenAI(api_key=self.api_key, base_url=self.base_url, timeout=self.timeout)

    def think(self, messages: list[dict[str, str]], temperature: float | None = None) -> Iterator[str]:
        """
        调用大语言模型进行思考，并返回流式响应。
        这是主要的调用方法，默认使用流式响应以获得更好的用户体验。

        Args:
            messages: 消息列表
            temperature: 温度参数，如果未提供则使用初始化时的值

        Yields:
            str: 流式响应的文本片段
        """
        print(f"🧠 正在调用 {self.model} 模型...")
        try:
            response = self._client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature if temperature is not None else self.temperature,
                max_tokens=self.max_tokens,
                stream=True,
            )

            print("✅ 大语言模型响应成功:")
            for chunk in response:
                content = chunk.choices[0].delta.content or ""
                if content:
                    print(content, end="", flush=True)
                    yield content
            print()

        except Exception as e:
            print(f"❌ 调用LLM API时发生错误: {e}")
            raise HelloAgentsException(f"LLM调用失败: {str(e)}")

    def invoke(self, messages: list[dict[str, str]], temperature: float | None = None) -> str:
        """
        非流式调用LLM，返回完整响应。
        适用于不需要流式输出的场景。
        """
        try:
            response = self._client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature if temperature is not None else self.temperature,
                max_tokens=self.max_tokens,
            )
            return response.choices[0].message.content
        except Exception as e:
            raise HelloAgentsException(f"LLM调用失败: {str(e)}")

    def stream_invoke(self, messages: list[dict[str, str]], temperature: float | None = None) -> Iterator[str]:
        """
        流式调用LLM的别名方法，与think方法功能相同。
        保持向后兼容性。
        """
        yield from self.think(messages, temperature)
