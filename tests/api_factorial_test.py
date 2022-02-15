import requests
import json
import math

from pathlib import Path
from config import END_POINT
from assertpy.assertpy import assert_that


def read_file(file_name):
    with Path.cwd().joinpath('..', 'resource', 'data', file_name).open(mode="r") as file:
        return json.load(file)


def factorial(number):
    if number >= 0:
        return math.factorial(number)
    else:
        return "Error 500"


def test_factorial_of_zero():
    payload = read_file('zero.json')
    response = requests.post(url=END_POINT, data=payload, verify=False)
    content = json.loads(response.content)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(content['answer']).is_equal_to(factorial(0))


def test_alphabetic_on_factorial():
    payload = read_file('alphabetic.json')
    response = requests.post(url=END_POINT, data=payload, verify=False)
    assert_that(response.status_code).is_equal_to(500)


def test_special_chars_on_factorial():
    payload = read_file('special_characters.json')
    response = requests.post(url=END_POINT, data=payload, verify=False)
    assert_that(response.status_code).is_equal_to(500)


def test_negative_number_on_factorial():
    payload = read_file('negative_number.json')
    response = requests.post(url=END_POINT, data=payload, verify=False)
    assert_that(response.status_code).is_equal_to(500)


def test_factorial_of_an_big_value():
    payload = read_file('biggest_value.json')
    response = requests.post(url=END_POINT, data=payload, verify=False)
    content = json.loads(response.content)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(content['answer']).is_equal_to(factorial(989))


def test_out_of_factorial_api():
    payload = read_file('number_out.json')
    response = requests.post(url=END_POINT, data=payload, verify=False)
    assert_that(response.status_code).is_equal_to(500)
