@web @factorial
Feature: Factorial Web Browsing
  As a web surfer,
  I want to to insert a not valid characters,
  So I can the error message.


  Scenario: Enter an alphabetic character
    Given the Factorial home page is displayed
    When the user enter a character "ABC"
    And the user click in Calculate button
    Then an error message "Please enter an integer" appear

  Scenario: Enter a special character
    Given the Factorial home page is displayed
    When the user enter a character "*/+"
    And the user click in Calculate button
    Then an error message "Please enter an integer" appear

  Scenario: Enter a negative number
    Given the Factorial home page is displayed
    When the user enter a number "-2"
    And the user click in Calculate button
    Then an error message "Please enter an integer" appear

  Scenario: Enter a float number
    Given the Factorial home page is displayed
    When the user enter a number "2.5"
    And the user click in Calculate button
    Then an error message "Please enter an integer" appear
