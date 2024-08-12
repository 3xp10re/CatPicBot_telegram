from selenium import webdriver
from selenium.webdriver.common.by import By


def parse(url):
    driver = webdriver.Edge()
    driver.get(url=url)
    links = []
    try:
        for i in range(10):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            catpics = driver.find_elements(By.TAG_NAME, 'img')
            for image in catpics:
                if (image.get_attribute('src')):
                    links.append(image.get_attribute('src'))
            
    except Exception as ex:
        pass

    finally:
        driver.close()
        driver.quit()
        del links [-2:]
        del links [:4]
        with open('cat_urls.txt', 'w') as file:
            for url in links:
                file.write(url + '\n')
    