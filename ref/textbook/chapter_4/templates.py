from fastapi import FastAPI, Response, Request 
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/hello")
async def index():
    ret = ''' 
    <html>
    <body>
    <h2>Hello world</h2>
    </body>
    </html>
    '''
    return Response(content=ret, media_type="text/html")

@app.get("/hello/{name}", response_class=HTMLResponse)
async def sayHello(name: str):
    ret = ''' 
    <html>
    <body>
    <h2>Hello {}</h2>
    </body>
    </html>
    '''.format(name)
    return HTMLResponse(content=ret)

# -------- Jinja2 --------

from fastapi.templating import Jinja2Templates
# declare the directory of templates
template = Jinja2Templates(directory="templates")

# app = FastAPI()

@app.get("/hello2/{name}", response_class = HTMLResponse)
async def sayHello2(request: Request, name: str):
    return template.TemplateResponse("hello.html", {
        "request": request, "nameForHtml": name
    })

@app.get("/employee/{name}/{salary}", response_class=HTMLResponse)
async def employee(request: Request, name: str, salary: float):
    data = {
        "name": name, "salary": salary
    }
    return template.TemplateResponse("employee.html", {
        "request": request, "dataForHtml": data
    })

# -------- Jinja2 Conditionals/Loop ----------

@app.get("/party/{name}/{age}", response_class=HTMLResponse)
async def party(request: Request, name: str, age: int):
    data = {
        "guest_name" : name,
        "guest_age" : age
    }
    return template.TemplateResponse("party.html", {
        "request": request, "data": data
    })

@app.get("/programmings", response_class=HTMLResponse)
async def party(request: Request):
    languages = ["Python", "Java", "C++"]
    return template.TemplateResponse("languages.html", {
        "request": request, "languages": languages
    })

# -------- Jinja2 Statics ----------
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/testjs/{name}", response_class=HTMLResponse)
async def jsdemo(request: Request, name: str):
    data = {"name": name}
    return template.TemplateResponse("testjs.html", {
        "request": request, "data": data
    })

# -------- Jinja2 Forms ----------
from fastapi import Form
# the var names must be same with names in html
@app.post("/testForm/")
async def getform(name: str = Form(...), address: str = Form(...), position: str = Form(...)):
    return {
        "Name": name,
        "Address": address,
        "Position": position
    }
@app.get("/form/", response_class=HTMLResponse)
async def display_form(request: Request):
    return template.TemplateResponse("testForm.html", {"request": request})