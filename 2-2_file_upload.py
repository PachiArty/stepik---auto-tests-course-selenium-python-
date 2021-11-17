from selenium import webdriver
import math
import time
import os
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//input[@class='form-control'][1]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@class='form-control'][2]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//input[@class='form-control'][3]")
    input3.send_keys("yandex.ru")


    
#добавление файла
    element = browser.find_element_by_xpath("//input[@id='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'hello.txt')
    element.send_keys(file_path)

    button = browser.find_element_by_xpath("//button")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
