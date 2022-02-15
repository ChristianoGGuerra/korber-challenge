# korber-challenge

# Challenge - Christiano Guerra

## Technologies used

I used the technologies below:

### API Test

* [Python 3.8](https://www.python.org/): As a language used;
* [Pip3](https://pip.pypa.io): To install pytest and assertpy libraries;
* [Cucumber](https://github.com/cucumber/cucumber-js): Cucumber is a tool for running automated tests written in plain language. Because they're written in plain language, they can be read by anyone on your team. Because they can be read by anyone, you can use them to help improve communication, collaboration and trust on your team;

## Folders Structures

* ```resource ```
    * ```data ``` Folder with some json files
        * ```alphabetic.json ``` Not valid Json with alphabetic characters (ABC)
        * ```biggest_value.json ``` The last value accept by API (989)
        * ```negative_number.json ``` Not valid Json with a number negative (-2)
        * ```number_out.json ``` First number out of the API scope, the number after the biggest one (990)
        * ```special_characters.json ``` Not valid Json with special characters
        * ```zero.json ``` The first factorial number accepted by API
    * ```drivers``` Folder that all drivers should be in
    * ```features``` Folder with all cucumber features
       * ```negative_factorial.feature ``` Have a negative tests, like non numbers or negative or not integer
       * ```positive_factorial.feature``` Have all positive fields, only integer
       * ```page_stand_elements.feature``` Page components that are in the page
* ```tests``` where the test file is
    * ```end2end  ``` Folder with all test steps
       * ```negative_factorial_step.py``` Steps for the negative features
       * ```positive_factorial_step.py``` Steps for the positive features
       * ```stand_fields_steps.py``` Steps for the page components that are in the page
    * ```factorial_test.py ``` The file with six(6) tests and a math.factorial method
* ```conf.py``` This configuration tells the API url.

## Set up

It is necessary to install Python at least 3
```
pip3 install pytest
pip3 install assertpy
```

## Running the tests

- Open the terminal and go to tests folder;

- Add the command ``` pytest factorial_test.py ```
- Run end to end test Go to end2end folder
- Add the command ``` pytest file_name.py ```
