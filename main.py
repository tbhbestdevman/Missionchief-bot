```python
import time
from selenium import webdriver
from login import login
from dispatcher import dispatch_missions
from utils import wait_for_page_load
from config import WEBDRIVER_PATH, MISSIONCHIEF_URL

def main():
    # Initialize the webdriver
    driver = webdriver.Chrome(WEBDRIVER_PATH)

    # Navigate to the MissionChief website
    driver.get(MISSIONCHIEF_URL)

    # Wait for the page to load
    wait_for_page_load(driver)

    # Login to the website
    login(driver)

    # Wait for the page to load
    wait_for_page_load(driver)

    # Dispatch missions
    dispatch_missions(driver)

    # Close the browser after a delay
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()
```