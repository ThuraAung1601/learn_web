from fastapi import FastAPI, Request, Form, Cookie
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates
from ZODB import FileStorage, DB
from models import Book
import transaction

# FastAPI app instance
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# ZODB setup
storage = FileStorage.FileStorage('data.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

@app.on_event("shutdown")
def shutdown():
    connection.close()
    db.close()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request, user: str = Cookie(None)):
    books = root.get('books', [])
    return templates.TemplateResponse("index.html", {"request": request, "books": books, "user": user})

@app.post("/add_book/")
async def add_book(title: str = Form(...), author: str = Form(...), price: float = Form(...), response: Response = None):
    new_book = Book(title, author, price)
    if 'books' not in root:
        root['books'] = []
    root['books'].append(new_book)
    transaction.commit()
    response.set_cookie(key="user", value="admin")  # Example cookie
    return {"message": "Book added!"}

@app.get("/edit_book/{index}", response_class=HTMLResponse)
async def edit_book(request: Request, index: int, user: str = Cookie(None)):
    books = root.get('books', [])
    if index >= len(books):
        return {"message": "Book not found"}
    return templates.TemplateResponse("edit.html", {"request": request, "book": books[index], "index": index, "user": user})

@app.post("/update_book/{index}/")
async def update_book(index: int, title: str = Form(...), author: str = Form(...), price: float = Form(...)):
    books = root.get('books', [])
    if index >= len(books):
        return {"message": "Book not found"}
    books[index].title = title
    books[index].author = author
    books[index].price = price
    transaction.commit()
    return {"message": "Book updated!"}

@app.post("/delete_book/{index}/")
async def delete_book(index: int):
    books = root.get('books', [])
    if index >= len(books):
        return {"message": "Book not found"}
    del books[index]
    transaction.commit()
    return {"message": "Book deleted!"}
