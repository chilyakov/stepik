from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Ivan")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Petrov")
    email = browser.find_element_by_name("email")
    email.send_keys("email@mail.ru")
    file = browser.find_element_by_id("file")
    file.send_keys(file_path)
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