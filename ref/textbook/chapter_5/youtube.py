from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import re

app = FastAPI()

# Set up templates directory
templates = Jinja2Templates(directory="templates")

# Helper function to extract YouTube video ID from the URL
def extract_video_id(youtube_url: str):
    # Regular expression to match YouTube video URLs
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", youtube_url)
    return match.group(1) if match else None

# GET route to display the form
@app.get("/video", response_class=HTMLResponse)
async def get_video_form(request: Request):
    return templates.TemplateResponse("video.html", {"request": request, "video_id": None})

# POST route to handle form submission and display the video
@app.post("/video", response_class=HTMLResponse)
async def stream_video(request: Request, youtube_url: str = Form(...)):
    video_id = extract_video_id(youtube_url)
    return templates.TemplateResponse("video.html", {"request": request, "video_id": video_id})
