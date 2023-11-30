Feature: Open plagiarism policy and Navigate to Diploma in IT page

	Background:
		Given Chrome browser is launched
		When Open NP Website
		Then Maximize Window

	Scenario: Open Plagiarism Policy Page
		Then Hover over Student Life navbar item
		Then Click on Code of Conduct link
		Then Open plagiarism policy
		Then Check if plagiarism policy has been opened in new tab
		And Close browser

	Scenario: Navigate to Diploma in IT page
		Then Click on search icon
		Then Input search text and search
		Then Verify if new window with searches appeared
		Then Click on diploma link
		Then Verify is new window is diploma in IT page
		And Close Browser
		

Feature: Visit Job Opportunities Page and Financial Aid Page

    Feature Description
    Background: Common Steps
		Given Chrome browser is launched
		When Open NP page

	Scenario: Visit Internships Page
		Then Hover over Student Services at navigation bar
		Then Click on Internships
		Then Check if the page redirected to Internships
		And Close Browser

	Scenario: Visit Job Opportunities Page
		Then Hover over Connect at navigation bar
		Then Click on Job Opportunities
		Then Check if the page redirected to Job Opportunities
        Then Input keyword in search bar and hit ENTER
		And Close browser