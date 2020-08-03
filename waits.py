from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(x))))


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    browser.find_element_by_tag_name('button').click()
    ans = calc(int(browser.find_element_by_id('input_value').text))
    browser.find_element_by_tag_name('input').send_keys(ans)
    browser.find_element_by_id('solve').click()

finally:
    time.sleep(10)
    browser.quit()