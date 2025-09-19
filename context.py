import rich 
import asyncio
from agents import Agent,Runner,RunContextWrapper,function_tool
from connection import config
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()
class UserInfo(BaseModel):
    name: str
    age: int
    area: str
    profession: str
user_info = UserInfo(
    name="samia ali",
    age=20,
    area="charted accountant",
    profession="student"
)
@function_tool()
def user_details(wrapper:RunContextWrapper[UserInfo]):
    """
    this function explains about user details.
    """
    info=wrapper.context ## variable context ko used karke hum user_info ko access kar sakte hain.
    return f"User Details: Name: {info.name}, Age: {info.age}, Area: {info.area}, Profession: {info.profession}"
info_agent = Agent(
    name="User Detail Finder", # name is a positional argument must given because it is very import. 
    instructions="you are a helpful assistant that helps students to find user details.",
    tools=[user_details],
)
async def main():
    result= await Runner.run(
        info_agent,
        "what is the user details.",
        run_config=config,
        context=user_info
    )
    rich.print(result.final_output)
    rich.print(result.new_items)
if __name__ == "__main__":
    asyncio.run(main())