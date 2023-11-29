Feature: Check NP Logo and Navigate to Academic Calendar

  Scenario: Verify the presence of NP Logo and Navigate to Academic Calendar
    Given Chrome browser is Launched
    When Open Ngee Ann Polytechnic website
    Then NP logo should be present on the page
    When Navigate to the Academic Calendar page
    Then Verify Academic Calendar page is open
    And Close the browser