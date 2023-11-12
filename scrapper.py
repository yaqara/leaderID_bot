import requests
from bs4 import BeautifulSoup
import sqlite3


db = sqlite3.connect('my_database.db')
links = db.cursor().execute("SELECT ")