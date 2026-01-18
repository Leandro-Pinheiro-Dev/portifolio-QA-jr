from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

def get_driver():
    # caminho absoluto até o chromedriver
    driver_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "frontend",
            "chromedriver.exe"
        )
    )

    service = Service(executable_path=driver_path)

    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver
