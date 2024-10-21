from pydoc import locate
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
LOGIN_BUTTON = (By.XPATH, '//*[@id="gb"]/div/div[2]/a')
EMAIL_FIELD = (By.XPATH, '//*[@id="identifierId"]')
NEXT_BUTTON = (By.XPATH, '//*[@id="identifierNext"]/div/button')
ERROR_TEXT = (By.XPATH, '//*[text()="Не удалось найти аккаунт Google."]')


def find_element(driver,locator, time=10):
    return WebDriverWait(driver,time).until(expected_conditions.presence_of_element_located(locator))

def test_error_auth():
    driver.get("https://www.google.ru/")
    find_element(driver, LOGIN_BUTTON).click()
    find_element(driver, EMAIL_FIELD).send_keys('mail')
    find_element(driver, NEXT_BUTTON).click()
    find_element(driver, ERROR_TEXT)

    Test
