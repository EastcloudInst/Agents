from autogen import AssistantAgent, UserProxyAgent

config_list_tongyi = [
    {
        "modle": "qwen-max",
        "api_base": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "api_type": "open_ai",
        "api_key": "sk-a31a563bce7146bf8c8ab93ad5fea537"
    }
]

tongyi_config = {
    "seed": 42,
    "temperature": 0,
    "config_list":  config_list_tongyi
}

async def get_weather(city: str) -> str:
    return f"{city}天气晴，温度2℃。"

assistant = AssistantAgent(
    name="weather_agent",
    llm_config=tongyi_config,
)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

user_proxy.initiate_chat(
    assistant,
    message="Tell me a joke about Huawei."
)