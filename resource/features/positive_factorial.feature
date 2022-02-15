@web @factorial
Feature: Factorial Web Browsing
  As a web surfer,
  I want to to insert a valid inputs,
  So I can the answer.


  Scenario: Enter a lowest number
    Given the Factorial home page is displayed
    When the user enter a number "0"
    And the user click in Calculate button
    Then a success message is "The factorial of 0 is: 1"

  Scenario: Enter a biggest number
    Given the Factorial home page is displayed
    When the user enter a number "170"
    And the user click in Calculate button
    Then a success message is "The factorial of 0 is: 7.257415615307999e+306"

  Scenario: Enter a number out of front end scope
    Given the Factorial home page is displayed
    When the user enter a number "171"
    And the user click in Calculate button
    Then a success message is "The factorial of 171 is: Infinity"