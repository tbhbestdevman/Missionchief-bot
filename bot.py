```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
import utils
import dispatcher
import login

class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)

    def start(self):
        self.driver.get(config.URL)
        login.login(self.driver, config.USERNAME, config.PASSWORD)
        while True:
            self.run_cycle()

    def run_cycle(self):
        mission_list = self.get_mission_list()
        for mission in mission_list:
            dispatcher.dispatch_mission(self.driver, mission)
            time.sleep(config.DISPATCH_INTERVAL)

    def get_mission_list(self):
        self.driver.get(config.MISSIONS_URL)
        utils.wait_for_page_load(self.driver)
        mission_elements = self.driver.find_elements(By.CSS_SELECTOR, config.MISSION_ELEMENT_SELECTOR)
        return [self.parse_mission_element(e) for e in mission_elements]

    def parse_mission_element(self, element):
        mission = {}
        mission['id'] = element.get_attribute('id')
        mission['name'] = element.find_element(By.CSS_SELECTOR, config.MISSION_NAME_SELECTOR).text
        mission['location'] = element.find_element(By.CSS_SELECTOR, config.MISSION_LOCATION_SELECTOR).text
        return mission

if __name__ == "__main__":
    bot = Bot()
    bot.start()
```