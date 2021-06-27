from selenium import webdriver
import time

# Селекторы для заполнения обязательных полей
input_firstname = '.first_block .form-control.first[required]'
input_lastname = '.first_block .form-control.second[required]'
input_email = '.first_block .form-control.third[required]'
# Селекторы для заполнения необязательных полей
input_phone = '.second_block .form-control.first'
input_address = '.second_block .form-control.second'

# Для запуска Теста 1. для теста №2, link Теста №1 комментируем
link = "http://suninjuly.github.io/registration1.html"

# Для запуска Теста 2. Снимаем комментарий для теста №2, link Теста №1 комментируем
# link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    # Открываем страницу для теста 1 или 2
    browser.get(link)

    browser.find_element_by_css_selector(input_firstname).send_keys("Ivan")

    browser.find_element_by_css_selector(input_lastname).send_keys("Petrov")

    browser.find_element_by_css_selector(input_email).send_keys("petrov.ivan@ya.ru")

    # Необязательные к заполнению поля
    # browser.find_element_by_css_selector(input_phone).send_keys("8-800-222-22-22")

    # browser.find_element_by_css_selector(input_address).send_keys("Russia")

    # Отправляем заполненную форму
    browser.find_element_by_css_selector('.btn.btn-default').click()

    # Проверяем, что смогли зарегистрироваться ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
