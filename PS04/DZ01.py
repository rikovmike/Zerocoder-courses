from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def search_wikipedia(driver, query):
    driver.get("https://www.wikipedia.org/")
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(query + Keys.RETURN)
    time.sleep(2)


def list_paragraphs(driver):
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for i, para in enumerate(paragraphs):
        print(f"Параграф {i + 1}:")
        print(para.text)
        print("-" * 80)
        if i < len(paragraphs) - 1:
            cont = input("Нажмите Enter, чтобы увидеть следующий абзац, или введите 'exit', чтобы остановиться: ")
            if cont.lower() == 'exit':
                break


def choose_link(driver):
    links = driver.find_elements(By.XPATH,
                                 "//a[@href and not(contains(@href, '#')) and not(contains(@href, 'redlink'))]")
    for i, link in enumerate(links):
        print(f"[{i + 1}] {link.text} ({link.get_attribute('href')})")

    choice = int(input("Введите номер ссылки, по которой вы хотите перейти, или введите 0 для отмены: "))
    if 0 < choice <= len(links):
        link_to_follow = links[choice - 1]
        link_to_follow.click()
        time.sleep(2)
    else:
        print("Неверный выбор или отменено.")


def main():
    driver = webdriver.Chrome()  # Make sure the path to your ChromeDriver is correctly set
    driver.implicitly_wait(10)

    try:
        while True:
            query = input("Введите ваш поисковый запрос для Википедии (или введите 'exit' для завершения): ")
            if query.lower() == 'exit':
                break

            search_wikipedia(driver, query)

            while True:
                print("Выберите действие:")
                print("1. Список абзацев текущей статьи.")
                print("2. Перейти по ссылке к другой статье.")
                print("3. Выйти к основному поиску.")
                action = input("Введите номер вашего выбора: ")

                if action == '1':
                    list_paragraphs(driver)
                elif action == '2':
                    choose_link(driver)
                elif action == '3':
                    break
                else:
                    print("Неверный вариант. Пожалуйста, попробуйте снова.")

    finally:
        driver.quit()

if __name__ == '__main__':
    main()