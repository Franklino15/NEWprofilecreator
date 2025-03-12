import json
from selenium import webdriver
from bot import email_creator, twitter_creator, referral_handler, utils

def main():
    # Setup Selenium driver (for example, using ChromeDriver)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    
    # Create email accounts
    print("Creating email accounts...")
    emails = email_creator.create_emails(driver, permanent_count=15, temp_count=5)
    
    # Create Twitter accounts (for example, create 5 accounts)
    print("Creating Twitter accounts...")
    twitter_accounts = twitter_creator.create_multiple_twitter_accounts(driver, count=5, sms_service=None)
    
    # Get referral link from user input
    referral_link = input("Please enter the referral link: ")
    referral_handler.process_referral(driver, referral_link)
    
    # Save account details in a JSON file
    account_data = {
        "emails": emails,
        "twitter_accounts": twitter_accounts
    }
    utils.save_account_details("account_details.json", account_data)
    print("Account details saved in account_details.json")
    
    driver.quit()

if __name__ == "__main__":
    main()
