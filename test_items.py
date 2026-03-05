import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(30)

    try:
        button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
        )

        assert button.is_displayed(), "Кнопка добавления в корзину не отображается на странице"

        button_text = button.text
        print(f"\nТекст на кнопке: '{button_text}'")

    except Exception as e:
        assert False, f"Кнопка добавления в корзину не найдена на странице. Ошибка: {e}"