from time import sleep
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'Edge browser is Launched')
def launchEdgeDriver(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()

@when(u'Open NP website')
def openFormyPage(context):
    context.driver.get("https://www.np.edu.sg/home")

@then(u'Navigate to School of ICT')
def findICT(context):
    schools = context.driver.find_element(By.PARTIAL_LINK_TEXT, "Schools & Courses").click()
    school = context.driver.find_element(By.PARTIAL_LINK_TEXT, "School of InfoComm Technology").click()

@then(u'Navigate to Overflow SIG')
def findOverflow(context):
    findICT(context)
    ict_life = context.driver.find_element(By.CSS_SELECTOR, "h2#ictian-life")
    context.driver.execute_script("arguments[0].scrollIntoView();", ict_life)
    sleep(3)
    overflow = context.driver.find_element(By.XPATH, "/html/body/main/section[2]/div/div[2]/div[2]/div[11]/div[6]/div[1]").click()
    sleep(3)

@then(u'Click WhatsApp button in School of ICT webpage')
def findX(context):
    findICT(context)
    twitter = context.driver.find_element(By.CSS_SELECTOR, "#st-2 > div.st-btn.st-last").click()
    sleep(3)

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()