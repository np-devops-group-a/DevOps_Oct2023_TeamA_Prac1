from behave import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'Chrome browser is launched')
def launchChrome(context):
    context.driver = webdriver.Chrome()

@when(u'Open NP Page')
def openNPPage(context):
    context.driver.get("https://www.np.edu.sg")

#Feature 1: Navigate to Internships Page, by Seng Jun    
@then(u'Hover over Student Services at navigation bar')
def hoverToStudentServices(context):
    studentServices = context.driver.find_element(By.XPATH, f"//a[text()='Student Services']")
    action = ActionChains(context.driver)
    action.move_to_element(studentServices).perform()

@then(u'Click on Internships')
def clickInternships(context):
    internships = context.driver.find_element(By.XPATH, f"//a[text()=\"Internships\"]")
    internships.click()
    sleep(3)

@then(u'Check if the page redirected to Internships')
def verifyFinancialAidPage(context):
    assert context.driver.current_url == "https://www.np.edu.sg/student-services/internships"

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()

#Feature 2: Navigate to Job Opportunities Page and search based on keyword, by Seng Jun
@then(u'Hover over Connect at navigation bar')
def hoverToConnect(context):
    connect = context.driver.find_element(By.XPATH, f"//a[text()='Connect']")
    action = ActionChains(context.driver)
    action.move_to_element(connect).perform()

@then(u'Click on Job Opportunities')
def clickJobOpportunities(context):
    jobOpportunities = context.driver.find_element(By.XPATH, f"//a[text()='Job Opportunities']")
    jobOpportunities.click()

@then(u'Check if the page redirected to Job Opportunities')
def verifyJobOpportunitiesPage(context):
    assert context.driver.current_url == "https://www.np.edu.sg/connect/alumni/job-opportunities"

@then(u'Input keyword in search bar and hit ENTER')
def inputKeyword(context):
    searchBar = WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID, 'jobSearch')))
    #To change the search keyword, simply overwrite the "Network" text.
    searchBar.send_keys("Network")
    searchBar.send_keys(Keys.ENTER)
    #For tester to view the search result.
    context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(5)

@then(u'Click on courses')
def clickCourses(context):
    courses = context.driver.find_element(By.XPATH, f"//a[text()='Courses']")
    courses.click()
    sleep(2)

@then(u'Search for Diploma in Information Technology')
def searchForDipIT(context):
    courses = context.driver.find_element(By.CSS_SELECTOR, f"#courseListingSearch")
    courses.click()
    courses.send_keys("Information Technology")
    courses.send_keys(Keys.ENTER)
    sleep(2)

@then(u'Click on Diploma in IT Card')
def clickOnDipIT(context):
    card = context.driver.find_element(By.CSS_SELECTOR, f".card-body")
    card.click()
    sleep(2)

@then(u'Check if redirected to Diploma in IT page')
def verifyDiplomaInITPage(context):
    assert context.driver.current_url == "https://www.np.edu.sg/schools-courses/academic-schools/school-of-infocomm-technology/diploma-in-information-technology"