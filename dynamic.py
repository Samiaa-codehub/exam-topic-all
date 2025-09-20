import asyncio
import rich
from connection import config
from dotenv import load_dotenv
from agents import Agent,Runner,RunContextWrapper,trace
from pydantic import BaseModel
load_dotenv()
class DynamictripType(BaseModel):
    destination:str
    trip_type:str
    days:int
    travel_profile:str
trip_type=DynamictripType(
    destination="Paris",
    trip_type="cultural",
    days=5,
    travel_profile="husband"
)
async def dynamicinstruction(ctx:RunContextWrapper[DynamictripType],agent:Agent):
    if  ctx.context.travel_profile=="solo":
        return "You are traveling alone. Here are some recommendations for solo travelers:"
    elif ctx.context.travel_profile=="family":
        return"You are traveling with family. Here are some recommendations for family travelers:"
    else:
        return"You are traveling with friends. Here are some recommendations for group travelers:"
agent=Agent(
    name="DynmaicTripAgent",
    instructions=dynamicinstruction,
)
async def main():
    with trace ("dynamic_trip"):
        rich.print("Starting dynamic trip agent...")
        result = await Runner.run(
            agent,
            "What is the best way to spend 5 days in Paris?" ,
            run_config=config,
            context=trip_type
    )
        rich.print(result.final_output)
if __name__ == "__main__":
    asyncio.run(main()) 