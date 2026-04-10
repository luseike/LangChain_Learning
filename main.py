
from typing import Optional

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from models import openai_model

from pydantic import BaseModel, Field
    
    
class Joke(BaseModel):
    """要告诉用户的笑话"""
    setup: str = Field(description="笑话的设置部分")
    punchline: str = Field(description="笑话的结尾部分")
    rating: Optional[int] = Field(description="笑话的评分，范围从1到10")


def main():

    # agent = create_agent(model=qwen)
    # respone = openai_model.invoke("请介绍一下你自己")
    # print(respone.content)

    response = openai_model.with_structured_output(Joke).invoke("请讲一个笑话，并给它一个评分，范围从1到10")
    print(response)



if __name__ == "__main__":
    main()
