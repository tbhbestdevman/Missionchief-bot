```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import utils

class Dispatcher:
    def __init__(self, driver):
        self.driver = driver

    def get_mission_list(self):
        self.driver.get(config.mission_list_url)
        utils.wait_for_page_load(self.driver)
        mission_list = self.driver.find_element(By.ID, config.mission_list_id)
        return mission_list

    def dispatch_mission(self, mission_id):
        self.driver.get(config.mission_url.format(mission_id))
        utils.wait_for_page_load(self.driver)
        dispatch_form = self.driver.find_element(By.ID, config.dispatch_form_id)
        dispatch_form.submit()
        utils.wait_for_page_load(self.driver)
        return self.driver.find_element(By.ID, config.mission_complete_id).is_displayed()

    def run(self):
        while True:
            mission_list = self.get_mission_list()
            for mission in mission_list:
                if self.dispatch_mission(mission):
                    print(config.mission_complete.format(mission))
                else:
                    print(config.dispatch_error.format(mission))
```