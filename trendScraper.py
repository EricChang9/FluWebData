from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#this is the node class that we will create the tree from 
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

        

PATH = "C:\Program Files (x86)\chromedriver.exe"

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://trends.google.com")

element = driver.find_element(By.XPATH, "//input[@id = 'i7']" )
element.send_keys("flu", Keys.ENTER)

time.sleep(10)
driver.close()



