import os
from pathlib import Path

from fastapi import FastAPI, File, Form, Request, UploadFile, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.api.llm_client import LLMClient
from app.modules.chat import ChatModule
from app.modules.voice import VoiceModule

# Initialize FastAPI app
app = FastAPI(title="Verbal Communication Skills Trainer")

# Set paths
BASE_DIR = Path(__file__).resolve().parent.parent  # Move up one level to project root

# Correct template directory
templates = Jinja2Templates(directory=str(BASE_DIR / "app/templates"))

# Correct static files directory
app = FastAPI(title="Verbal Communication Skills Trainer")
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "app/static")), name="static")
# Initialize modules
llm_client = LLMClient()
chat_module = ChatModule(llm_client)
voice_module = VoiceModule()


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: str = "OK"


@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    """
    ## Perform a Health Check
    Endpoint to perform a healthcheck on. This endpoint can primarily be used Docker
    to ensure a robust container orchestration and management is in place. Other
    services which rely on proper functioning of the API service will not deploy if this
    endpoint returns any other HTTP status code except 200 (OK).
    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck(status="healthy")


@app.get("/ui/chat", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "chat.html", {"request": request, "chat_modes": list(chat_module.roles.keys())}
    )


@app.post("/api/chat")
async def chat_interaction(message: str = Form(...), mode: str = Form("Coach")):
    response = await chat_module.get_response(message, mode)
    return {"response": response}

@app.post("/api/voice/analyze")
async def analyze_voice(audio: UploadFile = File(...)):
    temp_file = f"temp_{audio.filename}"
    with open(temp_file, "wb") as buffer:
        buffer.write(await audio.read())

    try:
        transcript = voice_module.transcribe_audio(temp_file)
        return {"transcript": transcript}
    finally:
        os.remove(temp_file)

@app.get("/ui/voice", response_class=HTMLResponse)
async def voice_page(request: Request):
    return templates.TemplateResponse("voice.html", {"request": request})
