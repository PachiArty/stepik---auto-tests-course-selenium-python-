from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
def calc(x):
    return (int(x)+int(y))


try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_xpath ("//span[@id='num1']")
    x = x_element.text
    y_element = browser.find_element_by_xpath ("//span[@id='num2']")
    y = y_element.text
    z = calc(x)
    print(z)
    select = browser.find_element_by_xpath("//select[@id='dropdown']")
    select.click()
    select = Select(browser.find_element_by_xpath("//select[@id='dropdown']"))
    select.select_by_value(str(z)) # ищем элемент с текстом "Python"
    #клик по кнопке
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
