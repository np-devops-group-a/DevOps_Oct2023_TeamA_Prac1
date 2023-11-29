Feature: Test NP website
    Background: Common Steps
        Given Edge browser is Launched
        When Open NP website
    Scenario: Find out about Overflow SIG
        Then Navigate to Overflow SIG
        And Close browser
    Scenario: Share the School of ICT on WhatsApp
        Then Click WhatsApp button in School of ICT webpage
        And Close browser