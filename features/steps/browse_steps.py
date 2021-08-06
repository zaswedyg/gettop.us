from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

@given('Open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()

@then('User sees correct categories under Browse')
def verify_browse_categories(context):
    context.app.main_page.verify_browse_categories()

@then('User clicks on categories under Browse and correct page opens')
def verify_browse_categories_open_correct_page(context):
    context.app.main_page.verify_browse_categories_open_correct_page()