import pytest
import time

from config import URL
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path=r"../../resource/drivers/chromedriver")
    driver.maximize_window()
    yield driver
    driver.quit()


# Scenarios

scenarios('../../resource/features/positive_factorial.feature')


# Shared Given Steps

@given('the Factorial home page is displayed', target_fixture='factorial_home')
def factorial_home(browser):
    browser.get(URL)


# When Steps
@when(parsers.parse('the user enter a number "{text}"'))
def set_input_number(browser, text):
    number = browser.find_element_by_id('number')
    number.send_keys(text)


@when('the user click in Calculate button')
def set_input_number(browser):
    button = browser.find_element_by_id('getFactorial')
    button.click()
    time.sleep(2)


@then(parsers.parse('a success message is "{text}"'))
def get_success_result(browser, text):
    success = browser.find_element_by_id('resultDiv')
    assert text == success.text
