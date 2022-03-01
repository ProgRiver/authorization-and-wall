import time
import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

url = "https://vk.com"
post_text = "Изучаю Python, Selenium и автоматизацию тестирования"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    # авторизация на сайте
    browser.find_element(By.ID, "index_email").send_keys(config.user_email)
    browser.find_element(By.ID, "index_pass").send_keys(config.password)
    button = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.ID, "index_login_button")))
    button.click()
    time.sleep(5)

    # переход на страницу профиля
    browser.find_element(By.ID, "l_pr").click()
    time.sleep(2)

    # нажатие на поле новой публикации и ввод текста
    browser.find_element(By.ID, "post_field").send_keys(post_text)
    time.sleep(2)
    
    # нажать на кнопку, чтобы добавить фото
    browser.find_element(By.CSS_SELECTOR, "span[class='MediaSelector__mediaIcon']").click()
    time.sleep(2)

    # загрузка первого фото из списка на странице
    browser.find_element(By.CSS_SELECTOR, ".photos_choose_row_bg").click()
    time.sleep(2)
   
    # отправка публикации
    browser.find_element(By.ID, "send_post").click()

except Exception as er:
    print(f"*** Ошибка *** {er}")
finally:
    time.sleep(10)
    browser.quit()