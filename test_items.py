import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_check_basket(browser):
    browser.get(link)
    # time.sleep(5)
    elements = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    # print(elements)
    assert len(elements) > 0, "The button 'Add to Basket' in not found"


# pytest -s -v test_section_3_language/test_items.py
# pytest -s -v --language=es --browser_name=chrome test_section_3_language/test_items.py
# pytest -s -v --language=fr --browser_name=firefox test_section_3_language/test_items.py
# pytest -s -v --language=en --browser_name=chrome test_section_3_language/test_items.py

