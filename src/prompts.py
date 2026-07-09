from langchain_core.prompts import ChatPromptTemplate

planner_prompt = ChatPromptTemplate.from_template(
"""
You are an autonomous planning Agent

User Request:
{request}

Return:
- plan_name
- list of goals
- list of tasks to be done

All these returns items will be processed futher to create a document.
"""
)

task_execution_prompt = ChatPromptTemplate.from_template(
"""
you are a task execution agent. complete tasks and create the document. do not use markdown characters , keep it simple.

FINAL GOAL:
{plan_name}

SUB-GOALS:
{goals}

SEQUENTIAL LIST OF TASKS:
{tasks}

TASK:
{task}

Document til now:
{document}

"""
)