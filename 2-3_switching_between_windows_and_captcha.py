from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #нажимаю первую кнопку
    option1 = browser.find_element_by_xpath("//button")
    option1.click()
    #выбираем новое окно
    new_window = browser.window_handles[1] #новая вкладка
    first_window = browser.window_handles[0] #первая вкладка
    browser.switch_to_window(new_window)
    
    #расчет формулы
    x_element = browser.find_element_by_xpath ("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    #ввод значения
    input = browser.find_element_by_xpath ("//input[@id='answer']")
    input.send_keys(y)
    #клик по кнопке
    button = browser.find_element_by_xpath("//button")
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
