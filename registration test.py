from selenium import webdriver
import time

try:
    # link = 'http://suninjuly.github.io/registration1.html'
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_css_selector('.first:required')
    name.send_keys('Anatoly')
    surname = browser.find_element_by_css_selector('.second:required')
    surname.send_keys('Masloboynikov')
    email = browser.find_element_by_css_selector('.third:required')
    email.send_keys('tolyasolnce@g.rf')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
