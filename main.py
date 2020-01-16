# coding: utf-8
import json
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

TIMEOUT_SEC = 30

with open('settings.json') as f:
    settings = json.load(f)

chrome_driver_path = settings['chromeDriverPath']
apple_ID = settings['appleID']
password = settings['password']
slack_incoming_webhook_url = settings['slackIncomingWebhookUrl']

browser = webdriver.Chrome(executable_path=chrome_driver_path)
browser.get('https://appstoreconnect.apple.com/')

# Wait a bit, because sometimes the account name text field cannot be focused
sleep(10)

WebDriverWait(browser, TIMEOUT_SEC).until(
    EC.presence_of_element_located((By.ID, 'aid-auth-widget-iFrame')))
browser.switch_to_frame(browser.find_element_by_id('aid-auth-widget-iFrame'))

WebDriverWait(browser, TIMEOUT_SEC).until(
    EC.element_to_be_clickable((By.ID, 'account_name_text_field')))
browser.find_element_by_id('account_name_text_field').send_keys(apple_ID)

WebDriverWait(browser, TIMEOUT_SEC).until(
    EC.element_to_be_clickable((By.ID, 'sign-in')))
browser.find_element_by_id('sign-in').click()

WebDriverWait(browser, TIMEOUT_SEC).until(
    EC.element_to_be_clickable((By.ID, 'password_text_field')))
browser.find_element_by_id('password_text_field').send_keys(password)

WebDriverWait(browser, TIMEOUT_SEC).until(
    EC.element_to_be_clickable((By.ID, 'sign-in')))
browser.find_element_by_id('sign-in').click()

try:
    # Repeat several times, as it may not be possible to retrieve the message
    # in one attempt
    for i in range(5):
        WebDriverWait(browser, TIMEOUT_SEC).until(
            EC.presence_of_element_located((By.ID, 'alerts')))
        alert_container = browser.find_element_by_id('alerts')

        WebDriverWait(browser, TIMEOUT_SEC).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[contains(@class,\'alertMsg\')]')))
        alert_contents = browser.find_element_by_xpath(
            '//*[contains(@class,\'alertMsg\')]')

        alert_message = alert_contents.text

        if alert_message == '':
            sleep(1)
            continue

        payload = {
            'text': alert_message,
        }
        requests.put(slack_incoming_webhook_url, json=payload)
        break
except Exception as e:
    print(e)

browser.quit()
