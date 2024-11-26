from swarm import Swarm, Agent
from openai import OpenAI
import datetime
from typing import Annotated
from datetime import timedelta

qwen = OpenAI(
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key='sk-a31a563bce7146bf8c8ab93ad5fea537'
)

client = Swarm(qwen)

def my_calendar():
    '''
    获取当前日期，当用户说需要请假，但却没有明确具体要从哪一天开始请，例如用户说 “我要从今天开始请三天假”，调用该函数以确定当前的日期
    
    Returns
    --------
    datetime.datetime
        返回当前时间
    '''
    return datetime.datetime.now()

def leave_func(start: Annotated[datetime.datetime, '用户请假日期的起始时间'], end: Annotated[datetime.datetime, '用户请假的截止时间']):
    '''请假逻辑执行函数，输入请假的开始与截至日期，函数将会执行请假的相关逻辑，帮助用户提交请假申请'''
    print("processing....")
    print("已提交用户请假申请！")
    print(f'start: {start}, end: {end}')
    return 'success'

def calculator_end(start: Annotated[datetime.datetime, '用户请假日期的起始时间'], lenth: Annotated[str, '用户请假时长']):
    '''
    根据用户请假的起始时间已经用户需要请假的时长，计算用户请假的截止时间。
    若用户已明确说明了请假的截止日期，则不需要调用此函数。

    Parameters
    ----------
    start ： datetime.datetime
        用户请假日期的起始时间
    lenth : str
        用户请假时长

    Returns
    ----------
    datetime.datetime
        返回计算出的用户请假截止日期
    '''
    lenth = float(lenth)
    start_datetime = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
    offset = timedelta(days=lenth)
    end = start_datetime + offset

    return end


agent_a = Agent(
    name="Agent A",
    model="qwen2.5-32b-instruct",
    instructions="You are a helpful agent.",
    functions=[my_calendar, leave_func, calculator_end],
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "你好，我想从今天开始请1.5天假"}],
)

print(response)