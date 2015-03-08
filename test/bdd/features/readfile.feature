Feature: As an user, I want to read the file baby[0-9]{4}.html and get the data from the table

  Scenario: Open the file
    Given The file "baby1990.html"
    Then I read the file and get the table with the information
