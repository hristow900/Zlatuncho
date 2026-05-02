from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from database import save_log

GAME_URL = os.getenv("GAME_URL")
USERNAME = os.getenv("GAME_USERNAME")
PASSWORD = os.getenv("GAME_PASSWORD")


def run_collector():
    options = Options()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(GAME_URL)

        # TODO: customize selectors
        driver.find_element(By.ID, "username").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login").click()

        # example reward click
        reward_button = driver.find_element(By.ID, "dailyReward")
        reward_button.click()

        save_log("SUCCESS")

    except Exception as e:
        save_log(f"FAILED: {str(e)}")

    finally:
        driver.quit()
