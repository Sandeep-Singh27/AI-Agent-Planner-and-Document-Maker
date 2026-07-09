from fastapi import FastAPI, HTTPException, status
from src.schema import UserRequest
from src.llm import plan,execute
from src.generate_document import generate_docx
from fastapi.responses import FileResponse
import traceback

app = FastAPI()

@app.post("/agent")
def handle_request(user_request:UserRequest):
    try:
        planning = plan(user_request.request)
        execution_result = execute(plan=planning)
        file_name = planning.plan_name + ".docx"
        file_path = generate_docx(execution_result,file_name)
        return FileResponse(file_path)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Server Side Error")
    