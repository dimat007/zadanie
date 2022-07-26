from selenium.webdriver.common.by import By

def test_guest_should_see_login_link(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket")