from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from src.schema import PlanSchema, ExecutionResult
from src.prompts import planner_prompt, task_execution_prompt
import os

load_dotenv()

API_KEY = os.getenv("MISTRAL_API_KEY")


llm = ChatMistralAI(
    model="mistral-small-latest",
    api_key=API_KEY,
    temperature=0.2
)

#Planner Layer
plan_output = llm.with_structured_output(PlanSchema)
planner_chain = planner_prompt | plan_output

def plan(request:str):
    response = planner_chain.invoke(
        {"request":request}
    )
    return response

#Execution Layer
execution_output = llm.with_structured_output(ExecutionResult)
execution_chain = task_execution_prompt | execution_output

def execute(plan: PlanSchema):
    print(f"Executing: {plan.tasks[0]}")
    initial_response = execution_chain.invoke(
        {
            "plan_name": plan.plan_name,
            "goals": plan.goals,
            "tasks":plan.tasks,
            "task":plan.tasks[0],
            "document": "Initally there is no document, you must create the template for the document required that will be edited by the further task",
        }
    )

    if len(plan.tasks)>1:
        context = initial_response
        for i in range(1,len(plan.tasks)):
            print(f"Executing: {plan.tasks[i]}")
            response = execution_chain.invoke(
                {
                "plan_name": plan.plan_name,
                "goals": plan.goals,
                "tasks":plan.tasks,
                "task":plan.tasks[i],
                "document": context,
                }           
            )
            context = response

    return response







