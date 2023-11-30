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