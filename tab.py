from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(x))))


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_tag_name('button').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    ans = calc(int(browser.find_element_by_id('input_value').text))
    browser.find_element_by_tag_name('input').send_keys(ans)
    browser.find_element_by_tag_name('button').click()


finally:
    time.sleep(10)
    browser.quit()