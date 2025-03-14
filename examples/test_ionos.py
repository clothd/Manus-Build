from app.llm import LLM
from app.schema import Message
import asyncio

async def test_ionos():
    llm = LLM()
    messages = [
        Message.system_message("You are a helpful assistant."),
        Message.user_message("Hello! Can you confirm you're running on IONOS AI?")
    ]
    
    response = await llm.chat(messages)
    print("Response:", response)

if __name__ == "__main__":
    asyncio.run(test_ionos())