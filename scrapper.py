from selenium import webdriver
import sqlite3
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get('https://leader-id.ru/events?actual=1&cityId=893&registrationActual=1&sort=date')

base = {}
db = sqlite3.connect('my_database.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS events (
    name TEXT,
    url TEXT,
    description TEXT,
    img_url TEXT)''')

count = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/section[1]/div/div[2]/div/div[2]/span").text
L = count.split()
j = 0
for i in range(1, int(L[0]) - 1):
    if i % 5 == 0:
        j += 1200
        driver.execute_script(f"window.scrollTo(0, {j})")
        sleep(1.5)

    else:
        name = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div/div[2]/div/div/section[2]/div/div[{i}]/div/h4/a ")
        url = name.get_attribute("href")
        description = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/section[2]/div/div[{i}]/div/div[2]/div[1]')
        image = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div/div[2]/div/div/section[2]/div/div[{i}]/a/div/img")
        imurl = image.get_attribute('src')  
        L = (name.text,url,description.text, imurl)    
        cursor.execute('INSERT INTO events (name, url, description, img_url) VALUES (?, ?, ?, ?)', L)
        db.commit()
details = cursor.execute("SELECT * FROM events")
for _ in details.fetchall():
    print(_)
db.close()
sleep(3)