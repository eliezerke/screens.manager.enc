from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv()

with sync_playwright() as pl:
    browser = pl.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://pythonanywhere.com/login/")
    page.fill('input[name="auth-username"]', "eliezerke")
    page.fill('input[name="auth-password"]', os.getenv("PSDD"))

    page.click('button[type="submit"]')
    page.wait_for_url("**/user/eliezerke/")

    print("Successfully logged in!")
    dashboard_title = page.inner_text("h1")

    page.goto("https://www.pythonanywhere.com/user/eliezerke/webapps/")
    
    page.locator('input[value="Run until 1 month from today"]').click()
    print("Set the web app to run for 1 month!")

    sleep(2)  # Wait for the setting to take effect

    print("Reloading the web app...")
    page.locator(".btn-large").click()
    sleep(10)  # Wait for the changes to be applied
    print("Reloaded the web app successfully!")

    print(f"Dashboard Title: {dashboard_title}")
    browser.close()

