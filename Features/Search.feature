Feature: Search Functionality

  @search
  Scenario: Search for valid product
    Given I get navigated to Home page
    When I enter a valid product in the search box field
    And I click the search button
    Then Validate the product should displayed in search result


  @search
  Scenario: Search for invalid product
    Given I get navigated to Home page
    When I enter a invalid product in the search box field
    And I click the search button
    Then Validate the proper message should displayed in search result


  @search
  Scenario: Search without entering any product
    Given I get navigated to Home page
    When I do not enter any value in the search box
    And I click the search button
    Then Validate the proper message should displayed in search result