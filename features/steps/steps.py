from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'Chrome browser is Launched')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome()

@when(u'Open Ngee Ann Polytechnic website')
def openNPWebsite(context):
    context.driver.get("https://www.np.edu.sg/home")

@then(u'NP logo should be present on the page')
def checkNpLogoPresence(context):
    # Find the NP logo image element by alt attribute
    np_logo_element = context.driver.find_element(By.XPATH, "//img[@alt='Ngee Ann Polytechnic']")
    
    # Assert that the NP logo element is present
    assert np_logo_element, "NP logo is not present on the page."

@when(u'Navigate to the Academic Calendar page')
def navigateToAcademicCalendar(context):
    # Directly navigate to the Academic Calendar page using the provided URL
    context.driver.get("https://www.np.edu.sg/admissions-enrolment/guide-for-prospective-students/academic-calendar")

@then(u'Verify Academic Calendar page is open')
def verifyAcademicCalendarPage(context):
    
    # For example, checking the title of the page
    assert "Academic Calendar" in context.driver.title, "The page is not the Academic Calendar."

@then(u'Close the browser')
def closeBrowser(context):
    context.driver.quit()