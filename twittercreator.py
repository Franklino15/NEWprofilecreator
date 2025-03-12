import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from bot.utils import human_delay

fake = Faker()

def create_twitter_account(driver, sms_service=None):
    driver.get("https://twitter.com/i/flow/signup")
    human_delay()
    # Generate random details
    first_name = fake.first_name()
    last_name = fake.last_name()
    full_name = f"{first_name} {last_name}"
    username = (first_name + last_name + str(random.randint(100, 999))).lower()
    password = "SecureP@ssw0rd!"  # Consider generating a more random password

    # Fill in the sign-up form (selectors are placeholders)
    driver.find_element(By.NAME, "name").send_keys(full_name)
    driver.find_element(By.NAME, "email").send_keys(username + "@example.com")
    human_delay()

    # Continue with the process
    driver.find_element(By.XPATH, "//span[text()='Next']").click()
    human_delay()
    # More steps: set birthdate, etc.
    # Handle verification:
    if sms_service:
        # Integrate with the SMS service API to get a phone number and verification code
        phone_number = sms_service.get_phone_number()
        driver.find_element(By.NAME, "phone_number").send_keys(phone_number)
        human_delay()
        driver.find_element(By.XPATH, "//span[text()='Next']").click()
        # Wait for SMS code and input it
        code = sms_service.get_verification_code(phone_number)
        driver.find_element(By.NAME, "verification_code").send_keys(code)
    else:
        # If SMS is not available, attempt to bypass (or wait for email verification)
        pass

    # Submit and complete registration
    driver.find_element(By.XPATH, "//span[text()='Sign up']").click()
    time.sleep(5)
    # Return account details
    return {
        "full_name": full_name,
        "username": username,
        "password": password
    }

def create_multiple_twitter_accounts(driver, count=1, sms_service=None):
    accounts = []
    for _ in range(count):
        account = create_twitter_account(driver, sms_service=sms_service)
        accounts.append(account)
        human_delay()
    return accounts
