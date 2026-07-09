from pydantic import BaseModel
from typing import List

class UserRequest(BaseModel):
    request: str

class PlanSchema(BaseModel):
    plan_name: str
    goals: List[str]
    tasks: List[str]

class DocumentSection(BaseModel):
    heading: str
    paragraphs: List[str]

class ExecutionResult(BaseModel):
    document: List[DocumentSection]