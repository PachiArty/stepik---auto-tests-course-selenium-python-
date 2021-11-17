from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "$100"))
    
    button1 = browser.find_element_by_xpath ("//button[@id='book']")
    button1.click()

    x_element = browser.find_element_by_xpath ("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_xpath ("//input[@id='answer']")
    input.send_keys(y)
    button = browser.find_element_by_xpath("//button[@id='solve']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
