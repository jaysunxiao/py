"""HelloAgents统一LLM接口 - 基于OpenAI原生API"""

import os
from collections.abc import Iterator
from typing import Literal

from openai import OpenAI

from .exceptions import HelloAgentsException

# 支持的LLM提供商
SUPPORTED_PROVIDERS = Literal["openai", "deepseek", "local"]

_VALID_PROVIDERS = frozenset({"openai", "deepseek", "local"})


class HelloAgentsLLM:
    """
    为HelloAgents定制的LLM客户端。
    它用于调用任何兼容OpenAI接口的服务，并默认使用流式响应。

    设计理念：
    - 参数优先，环境变量兜底
    - 流式响应为默认，提供更好的用户体验
    - 支持 openai、deepseek、local 三种提供商
    - 统一的调用接口
    """

    def __init__(
        self,
        model: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        provider: SUPPORTED_PROVIDERS | None = None,
        temperature: float = 0.7,
        max_tokens: int | None = None,
        timeout: int | None = None,
        **kwargs
    ):
        """
        初始化客户端。优先使用传入参数，如果未提供，则从环境变量加载。
        支持自动检测 provider 或使用统一的 LLM_* 环境变量配置。

        Args:
            model: 模型名称，如果未提供则从环境变量 LLM_MODEL_ID 读取
            api_key: API密钥，如果未提供则从环境变量读取
            base_url: 服务地址，如果未提供则从环境变量 LLM_BASE_URL 读取
            provider: LLM提供商（openai / deepseek / local），如果未提供则自动检测
            temperature: 温度参数
            max_tokens: 最大token数
            timeout: 超时时间，从环境变量 LLM_TIMEOUT 读取，默认60秒
        """
        self.model = model or os.getenv("LLM_MODEL_ID")
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout or int(os.getenv("LLM_TIMEOUT", "60"))
        self.kwargs = kwargs

        if provider:
            normalized = provider.lower()
            if normalized not in _VALID_PROVIDERS:
                raise HelloAgentsException(
                    f"不支持的 provider: {provider}，仅支持 openai、deepseek、local"
                )
            self.provider = normalized
        else:
            self.provider = self._auto_detect_provider(api_key, base_url)

        self.api_key, self.base_url = self._resolve_credentials(api_key, base_url)

        if not self.model:
            self.model = self._get_default_model()
        if not all([self.api_key, self.base_url]):
            raise HelloAgentsException("API密钥和服务地址必须被提供或在.env文件中定义。")

        self._client = self._create_client()

    def _auto_detect_provider(self, api_key: str | None, base_url: str | None) -> str:
        """
        自动检测 LLM 提供商（openai / deepseek / local）

        检测逻辑：
        1. 检查特定提供商的环境变量
        2. 根据 API 密钥格式判断
        3. 根据 base_url 判断
        4. 有通用 LLM_* 配置时视为 local
        """
        if os.getenv("OPENAI_API_KEY"):
            return "openai"
        if os.getenv("DEEPSEEK_API_KEY"):
            return "deepseek"

        actual_api_key = api_key or os.getenv("LLM_API_KEY")
        if actual_api_key and actual_api_key.lower() == "local":
            return "local"

        actual_base_url = base_url or os.getenv("LLM_BASE_URL")
        if actual_base_url:
            base_url_lower = actual_base_url.lower()
            if "api.openai.com" in base_url_lower:
                return "openai"
            if "api.deepseek.com" in base_url_lower:
                return "deepseek"
            if (
                "localhost" in base_url_lower
                or "127.0.0.1" in base_url_lower
                or any(port in base_url_lower for port in [":8080", ":7860", ":5000", ":8000"])
            ):
                return "local"

        if actual_api_key or actual_base_url:
            return "local"

        return "openai"

    def _resolve_credentials(self, api_key: str | None, base_url: str | None) -> tuple[str, str]:
        """根据 provider 解析 API 密钥和 base_url"""
        if self.provider == "openai":
            resolved_api_key = api_key or os.getenv("OPENAI_API_KEY") or os.getenv("LLM_API_KEY")
            resolved_base_url = base_url or os.getenv("LLM_BASE_URL") or "https://api.openai.com/v1"
            return resolved_api_key, resolved_base_url

        if self.provider == "deepseek":
            resolved_api_key = api_key or os.getenv("DEEPSEEK_API_KEY") or os.getenv("LLM_API_KEY")
            resolved_base_url = base_url or os.getenv("LLM_BASE_URL") or "https://api.deepseek.com"
            return resolved_api_key, resolved_base_url

        # local
        resolved_api_key = api_key or os.getenv("LLM_API_KEY") or "local"
        resolved_base_url = base_url or os.getenv("LLM_BASE_URL") or "http://localhost:8000/v1"
        return resolved_api_key, resolved_base_url

    def _create_client(self) -> OpenAI:
        """创建OpenAI客户端"""
        return OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
            timeout=self.timeout
        )

    def _get_default_model(self) -> str:
        """获取默认模型"""
        if self.provider == "openai":
            return "gpt-3.5-turbo"
        if self.provider == "deepseek":
            return "deepseek-chat"
        return "local-model"

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

    def invoke(self, messages: list[dict[str, str]], **kwargs) -> str:
        """
        非流式调用LLM，返回完整响应。
        适用于不需要流式输出的场景。
        """
        try:
            response = self._client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=kwargs.get('temperature', self.temperature),
                max_tokens=kwargs.get('max_tokens', self.max_tokens),
                **{k: v for k, v in kwargs.items() if k not in ['temperature', 'max_tokens']}
            )
            return response.choices[0].message.content
        except Exception as e:
            raise HelloAgentsException(f"LLM调用失败: {str(e)}")

    def stream_invoke(self, messages: list[dict[str, str]], **kwargs) -> Iterator[str]:
        """
        流式调用LLM的别名方法，与think方法功能相同。
        保持向后兼容性。
        """
        temperature = kwargs.get('temperature')
        yield from self.think(messages, temperature)
