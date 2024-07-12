from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import time
from bs4 import BeautifulSoup

def validateLinks(link):
    try:
        response =requests.head(link)
        if response.status_code>= 400:
#            print(f"{link} - {response.reason} - is broken")
            print(f"\033[91m{link} - {response.reason} - is broken\033[0m")
        else:
            print(f"{link} - {response.reason} - is working")
    except Exception as e:
#       print(f"Exception Caught - {link}")
        print(f"\033[91m{link} - Exception occurred\033[0m")
        print(e)

def testLinks():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.luxunlock.com/")
    driver.implicitly_wait(10)

    links= driver.find_elements(By.TAG_NAME,"a")
    for link in links:
        link_url=link.get_attribute("href")
        validateLinks(link_url)
    
    driver.quit

if __name__=="__main__":
    testLinks()