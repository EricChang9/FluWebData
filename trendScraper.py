from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pytrends.request import TrendReq

PATH = "C:\Program Files (x86)\chromedriver.exe"

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://trends.google.com/trends/explore?q=flu&date=now%201-d&geo=US&hl=en")

elements = driver.find_elements(By.TAG_NAME, "span" )
print(elements)

driver.close()

