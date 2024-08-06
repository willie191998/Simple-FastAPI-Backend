# main.py

from fastapi import FastAPI
from middleware import ProcessTimeMiddleware, log_errors  # Import the class directly
from routers import user, investor
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

# Add the process time middleware
app.add_middleware(ProcessTimeMiddleware)

# Add the error logging middleware
app.middleware('http')(log_errors)

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(investor.router, prefix="/investor", tags=["investor"])

# Define a response model using Pydantic
class ResponseModel(BaseModel):
    res: str

@app.get("/", response_model=ResponseModel)
async def read_root():
    return {"res": "Hello"}

# Global 404 handler
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "Not Found"}
    )