from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
ans = calc(browser.find_element_by_id('input_value').text)
browser.find_element_by_id('answer').send_keys(ans)
check = browser.find_element_by_id('robotCheckbox')
browser.execute_script("return arguments[0].scrollIntoView(true);", check)
check.click()
browser.find_element_by_id('robotsRule').click()
button = browser.find_element_by_tag_name("button")
button.click()
assert True
