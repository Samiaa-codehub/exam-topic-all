import rich
import asyncio
from agents import Agent,Runner,function_tool,ModelSettings
from connection import config
from dotenv import load_dotenv

load_dotenv()
@function_tool(name_override="Exam_Info",description_override="Get information about exams",is_enabled=True)
def exam_info():
    """
    this function explains about exam .
    """
    return"Exam info: Exam is the most important part of student life. It is the time when students have to show their knowledge and skills. To prepare for exams, students need to find the right topics to study. The best strategy for high scores includes understanding the syllabus, practicing past papers, and focusing on weak areas."

info_agent = Agent(
    name="Exam Topic Finder", # name is a positional argument must given because it is very import. 
    instructions="you are a helpful assistant that helps students to find exam topics.",
    tools=[exam_info],
    model_settings=ModelSettings(
        temperature=0.2,
        top_p=0.9,
        tool_choice="required",
        max_turns=2,
    )
)
async def main():
    result= await Runner.run(
        info_agent,
        "what is the best stategy fot highy score.",
        run_config=config
    )
    rich.print(result.final_output)
    rich.print(result.new_items)
if __name__ == "__main__":
    asyncio.run(main())