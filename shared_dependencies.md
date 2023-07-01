1. "selenium": This is a Python library used for automating browser activities. It will be used in "main.py", "bot.py", "dispatcher.py", and "login.py" for interacting with the website.

2. "requests": This is a Python library for making HTTP requests. It will be used in "main.py", "bot.py", "dispatcher.py", and "login.py" for sending and receiving data from the website.

3. "config": This module will be used in all files to access shared configuration settings like website URL, login credentials, etc.

4. "utils": This module will contain utility functions that can be used across all other modules. Functions like "wait_for_page_load", "find_element", etc. will be defined here.

5. "BeautifulSoup": This is a Python library for parsing HTML and XML documents. It will be used in "main.py", "bot.py", "dispatcher.py", and "login.py" for parsing the website's HTML.

6. "webdriver": This is a part of the selenium library and will be used in "main.py", "bot.py", "dispatcher.py", and "login.py" for controlling the browser.

7. DOM Element IDs: These will be used in "main.py", "bot.py", "dispatcher.py", and "login.py" for identifying and interacting with specific elements on the website. Examples include "login_button", "dispatch_form", "mission_list", etc.

8. Message Names: These will be used in "main.py", "bot.py", "dispatcher.py", and "login.py" for logging and error handling. Examples include "login_success", "dispatch_error", "mission_complete", etc.

9. Function Names: These will be used across all modules for performing specific tasks. Examples include "login", "dispatch_mission", "get_mission_list", etc.