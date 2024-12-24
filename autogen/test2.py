from autogen import oai

# create a text completion request
response = oai.Completion.create(
    config_list=[
        {
            "model": "qwen-max",
            "api_base": "https://dashscope.aliyuncs.com/compatible-mode/v1",
            "api_type": "open_ai",
            "api_key": "sk-a31a563bce7146bf8c8ab93ad5fea537", # just a placeholder
        }
    ],
    prompt="Hi",
)
print(response)