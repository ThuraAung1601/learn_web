from fastapi import FastAPI, Request, Form, Cookie
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request, user: str = Cookie(None)):
    return templates.TemplateResponse("cookieForm.html", {"request": request, "user": user})

@app.post("/setcookie/")
async def setcookie(request: Request, response: Response, user: str = Form(...), pwd: str = Form(...)):
    response.set_cookie(key="user", value=user)
    return {"message": "Cookie set!"}
