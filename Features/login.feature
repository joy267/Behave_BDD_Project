Feature: Login Functionality


  @login
  Scenario: Login with valid credentials
    Given I navigated to the login page
    When I enter the valid email and password into the fields
    And I click the login button
    Then I should get logged in

  @login
  Scenario: Login with the valid email and invalid password
    Given I navigated to the login page
    When I enter the valid email and invalid password into the fields
    And I click the login button
    Then I should get proper warning message


  @login
  Scenario: Login with the invalid email and valid password
    Given I navigated to the login page
    When I enter the invalid email and valid password into the fields
    And I click the login button
    Then I should get proper warning message


  @login
  Scenario: Login with the invalid credentials
    Given I navigated to the login page
    When I enter the invalid email and password into the fields
    And I click the login button
    Then I should get proper warning message