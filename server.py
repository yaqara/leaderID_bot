from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sqlite3


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

db = sqlite3.connect('my_database.db')
sql = db.cursor()
data = sql.execute("""SELECT * FROM events""").fetchall()

@app.get('/')
def mpList(request: Request):
    global data
    context = {
        "request": request,
        "data": data
        }
    return templates.TemplateResponse(name="index.html", context=context)