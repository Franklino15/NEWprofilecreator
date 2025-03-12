import time
import random
import json
from selenium.webdriver import ActionChains

def human_delay(min_seconds=2, max_seconds=5):
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)

def simulate_human_movement(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element).pause(random.uniform(0.5, 1.5)).perform()

def solve_captcha(driver):
    # Placeholder for 2Captcha integration
    # You would send the captcha image to 2Captcha and retrieve the solution
    # For now, we return a dummy string
    return "dummy_captcha_solution"

def save_account_details(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
