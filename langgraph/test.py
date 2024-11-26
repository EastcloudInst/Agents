from langchain_community.llms.tongyi import Tongyi

import getpass 
import os 

def _set_env(var: str): 
    if not os.environ.get(var): 
        os.environ[var] = 'sk-a31a563bce7146bf8c8ab93ad5fea537'

# api key: sk-a31a563bce7146bf8c8ab93ad5fea537
_set_env("DASHSCOPE_API_KEY")

llm = Tongyi()

llm.invoke('你好')