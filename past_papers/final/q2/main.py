from fastapi import FastAPI, Form, Request, RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# In-memory list to store notes
notes = []

# Define the Note class
class Note:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

# Home view: List all notes
@app.get("/", response_class=HTMLResponse)
async def read_notes(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "notes": notes})

# View details of a single note
@app.get("/notes/{note_id}", response_class=HTMLResponse)
async def read_note_detail(request: Request, note_id: int):
    if note_id < 0 or note_id >= len(notes):
        return RedirectResponse(url="/")
    note = notes[note_id]
    return templates.TemplateResponse("note_detail.html", {"request": request, "note": note, "note_id": note_id})

# Form to post a new note
@app.get("/notes/new", response_class=HTMLResponse)
async def new_note_form(request: Request):
    return templates.TemplateResponse("new_note.html", {"request": request})

# Handle form submission for a new note
@app.post("/notes/new")
async def create_note(title: str = Form(...), content: str = Form(...)):
    note = Note(title=title, content=content)
    notes.append(note)
    return RedirectResponse(url="/", status_code=303)
