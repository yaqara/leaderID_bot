from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class User:
    global driver
    def __init__(self, tel):
        self.tel = tel
        self.driver = webdriver.Firefox()
        self.driver.get("https://leader-id.ru/")
    def autorization_by_tg(self):
        
        
        
user = User(9502181920)
user.autorization_by_tg()