import pytest

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

scenarios('../../resource/features/page_stand_elements.feature')


# Shared Given Steps

@given('the Factorial home page is displayed', target_fixture='factorial_home')
def factorial_home(browser):
    browser.get(URL)


# When Steps

@when(parsers.parse('the user can see the title is "{text}"'))
def get_title(browser, text):
    title = browser.title
    assert text == title


@when(parsers.parse('the user can see page information "{text}"'))
def get_page_info(browser, text):
    header = browser.find_element_by_xpath('//h1').text
    assert text == header


@then(parsers.parse('the user can see input with placeholder "{text}"'))
def input_placeholder(browser, text):
    ph = browser.find_element_by_id('number').get_attribute('placeholder')
    assert text == ph


@then(parsers.parse('the user can see the "{text}" button'))
def button_name(browser, text):
    bn = browser.find_element_by_id('getFactorial').text
    assert text == bn
