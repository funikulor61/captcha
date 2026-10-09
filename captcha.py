from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
# открываем браузер
driver = webdriver.Chrome()

# заходим на страницу (замени на нужный URL)
driver.get("https://solvecaptcha.com/ru/demo/image-captcha")

# находим картинку по тегу img (первую на странице)
img = driver.find_element(
    By.CSS_SELECTOR,
    "div.flex.items-center.flex-col.mb-60 img[alt='image captcha']"
)

# берём у неё ссылку из атрибута src
src = img.get_attribute("src")
print("src:", src)

# качаем картинку по ссылке
data = requests.get(src).content

# сохраняем в файл
with open("image.png", "wb") as f:
    f.write(data)

print("Сохранил в image.png")
# for inp in driver.find_elements(By.TAG_NAME, 'input'):
#     print(inp.get_attribute('type'), inp.get_attribute('id'), inp.get_attribute('name'))
driver.get("https://www.prepostseo.com/ru/image-to-text")
file_path = os.path.abspath("image.png")  # получаем полный путь
upload_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
upload_input.send_keys(file_path)
time.sleep(5)
button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.extract-text"))
    )
# Нажимаем на кнопку
button.click()
time.sleep(15)
target_div = driver.find_element(By.ID, "result__text0")

# Копируем текст в переменную Python
copied_text = target_div.text

print(copied_text)
driver.get("https://solvecaptcha.com/ru/demo/image-captcha")
time.sleep(5)

input_field = driver.find_element(By.ID, "ts-box")
input_field.send_keys(copied_text)
time.sleep(3)

submit_button = driver.find_element(By.ID, "ts_submit")
submit_button.click()
time.sleep(10)