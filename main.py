from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximazed")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options)

stealth(
    driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win64",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)


def check_update():
    driver.get("https://coinmarketcap.com/ru/currencies/tether/")
    time.sleep(2.5)
    price = driver.find_element(By.ID, "section-coin-chart-mobile").text
    good = float(price[13:18])
    if good == 80 or good > 80:
        return f"Прекрасная цена для продажи: {good}"



def main():
    check_update()


if __name__ == '__main__':
    main()