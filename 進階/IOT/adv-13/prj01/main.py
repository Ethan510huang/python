import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0.9)
from langchain_core.messages import HumanMessage

while True:
    ans = input("請輸入想跟AI說的話:")
    print(
        model.invoke(
            [
                HumanMessage(
                    content="""你是一個負責開關柵欄和開關燈的管理員
                    'on'代表開燈
                    'off'代表關燈
                    '0'代表關柵欄
                    '90'代表開柵欄
                    'none'代表不開關
                    你只能依照使用者的問題回答'on'或'off'或'none'或'1'或'90'或'none'不可以回答他字串"""
                ),
                HumanMessage(content=ans),
            ]
        ).content
    )
print(msg)
