from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_xpath ("//img").get_attribute("valuex")
    x = x_element
    y = calc(x)
    input = browser.find_element_by_xpath ("//input[@id='answer']")
    input.send_keys(y)
    option1 = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_xpath("//input[@id='robotsRule']")
    option2.click()
    #клик по кнопке
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
