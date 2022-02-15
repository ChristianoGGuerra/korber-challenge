@web @factorial
Feature: Factorial Web Browsing
  As a web surfer,
  I want to see the factorial info,
  So I can insert an integer and calculate the factorial.


  Scenario: Go to factorial page and see title and fields
    Given the Factorial home page is displayed
    When the user can see the title is "Factoriall"
    And the user can see page information "The greatest factorial calculator!"
    Then the user can see input with placeholder "Enter an integer"
    And the user can see the "Calculate!" button