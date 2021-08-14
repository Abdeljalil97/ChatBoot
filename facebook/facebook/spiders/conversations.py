import time
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConversationsSpider(scrapy.Spider):
    name = 'conversations'
  
    def start_requests(self):
        yield SeleniumRequest(url='https://www.facebook.com/login', callback=self.login)


    def login(self, response):
        driver = response.meta['driver']
        email  = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
    )
        email.send_keys('')
        password  = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='pass']"))
    )
        password.send_keys('')
        submit  = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='loginbutton']"))
    )
        submit.click()
        time.sleep(3)
        print(driver.current_url)