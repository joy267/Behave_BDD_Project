Feature: Registration Functionality

  @register
  Scenario: Register with mandatory fields
    Given I navigated to the register page
    When I give the inputs into the mandatory fields
    And I click on continue button
    Then Account should be created


  @register
  Scenario: Register with duplicate email address
    Given I navigated to the register page
    When I give existing email account in the email fields
    And I click on continue button
    Then Proper error message should be displayed for duplicate email address

  @register
  Scenario: Register with without email address
    Given I navigated to the register page
    When I give the inputs into all the fields without email fields
    And I click on continue button
    Then Proper error message should be displayed for without email address

  @register
  Scenario: Register without giving any inputs
    Given I navigated to the register page
    When I do not give any inputs into the fields
    And I click on continue button
    Then Proper error message should be displayed