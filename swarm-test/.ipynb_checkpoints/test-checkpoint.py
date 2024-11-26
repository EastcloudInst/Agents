from swarm import Swarm, Agent
from openai import OpenAI

qwen = OpenAI(
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key='sk-a31a563bce7146bf8c8ab93ad5fea537'
)

client = Swarm(qwen)

def transfer_to_agent_b():
    return agent_b


agent_a = Agent(
    name="Agent A",
    model="qwen-max",
    instructions="You are a helpful agent.",
    tool_choice='auto',
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="Agent B",
    model="qwen-max",
    instructions="Only speak in Haikus.",
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to agent B."}],
)

print(response)
print(response.messages[-1]["content"])
