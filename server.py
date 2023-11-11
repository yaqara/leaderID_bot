from flask import Flask, render_template
import sqlite3


app = Flask(__name__,
            static_folder='static',
            template_folder='templates')
db = sqlite3.connect('idb.db')
sql = db.cursor()

@app.route('')
def mpList():
    render_template("index.html")