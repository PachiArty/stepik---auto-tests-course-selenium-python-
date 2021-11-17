from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #нажимаю первую кнопку
    option1 = browser.find_element_by_xpath("//button")
    option1.click()
    #нажимаю на модальное окно
    confirm = browser.switch_to.alert
    confirm.accept()
    #расчет формулы
    x_element = browser.find_element_by_xpath ("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    #ввод значения
    input = browser.find_element_by_xpath ("//input[@id='answer']")
    input.send_keys(y)
    #клик по кнопке
    button = bbrowser.find_element_by_xpath("//button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    
