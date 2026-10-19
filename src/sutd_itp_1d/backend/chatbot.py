import os
from enum import StrEnum
from typing import TypedDict

from dotenv import load_dotenv
from openai import OpenAI


class Role(StrEnum):
    User = "User"
    Assistant = "Assistant"
    Developer = "Developer"
    System = "System"


# typescript ^^ version of:
# interface Role:
#   User,
#   Developer,
#   System


# what the heck is this?
# https://typing.python.org/en/latest/spec/typeddict.html
# yes im a sucker for typescript and C i like explicit typing
class Message(TypedDict):
    role: Role
    content: str


class ChatService:
    def __init__(self, model: str = "gpt-6-luna", temp: float = 0.7):
        load_dotenv()
        # mangle, dont touch or read pls
        # https://www.geeksforgeeks.org/python/name-mangling-in-python/
        self.__apikey = os.getenv("OPENAI_API_KEY")
        if self.__apikey == None:
            raise ValueError("please init OPENAI_API_KEY in .env file")

        self.service = OpenAI(api_key=self.__apikey)
        self.model = model
        self.temp = float

    def chat(self, context: list[Message]) -> list[Message]:
        response = self.service.completions.create(
            model=self.model, messages=context, temperature=self.temp
        )
        print(response)
        response_object: Message = {
            "role": Role.Assistant,
            "content": response.choices[0].message.content or "failed",
        }
        context.append(response_object)
        return context
