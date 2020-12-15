from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("num1")
    x = x_element.text

    y_element = browser.find_element_by_id("num2")
    y = y_element.text

    z = int(x) + int(y)
    print(x, y, z)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(z))
    # input1 = browser.find_element_by_id("answer")
    # input1.send_keys(y)
    #
    # option1 = browser.find_element_by_id("robotCheckbox")
    # option1.click()
    #
    # option2 = browser.find_element_by_id("robotsRule")
    # option2.click()
    # # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()