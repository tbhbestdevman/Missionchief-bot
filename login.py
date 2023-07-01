```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import utils

def login(driver):
    driver.get(config.URL)

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    username.send_keys(config.USERNAME)
    password.send_keys(config.PASSWORD)

    login_button = driver.find_element(By.ID, "login_button")
    login_button.click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mission_list"))
        )
        print("login_success")
    except:
        print("login_error")
        driver.quit()

    return driver
```