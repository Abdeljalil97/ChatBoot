from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from shutil import which


path = which('geckodriver')
driver = webdriver.Firefox(executable_path=path)
driver.get('https://www.facebook.com/login')
email  = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
)
email.send_keys('')
password  = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//input[@id='pass']"))
)
password.send_keys('')
submit  = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//button[@id='loginbutton']"))
)
submit.click()

send_code  = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//*[@id='checkpointBottomBar']//a"))
)
send_code.click()
resend  = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "(//*[@role='button'])[4]"))
)
resend.click()
ferme_alert  = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "(//*[@role='button'])[4]"))
)

ferme_alert.click()
approvals_code  = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//*[@id='approvals_code']"))
)
code = input("entrez le code de confirmation : ")
email.send_keys(code)
submit  = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//*[@id='checkpointSubmitButton']"))
)
submit.click()

