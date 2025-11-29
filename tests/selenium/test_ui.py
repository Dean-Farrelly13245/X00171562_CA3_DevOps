from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_add_operation():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("http://localhost:5000")

    driver.find_element(By.ID, "num1").send_keys("4")
    driver.find_element(By.ID, "num2").send_keys("6")
    driver.find_element(By.ID, "add").click()

    time.sleep(1)

    result_text = driver.find_element(By.ID, "result").text  # e.g. "Result: 10.0"
    number_part = result_text.replace("Result:", "").strip()
    assert float(number_part) == 10.0

    driver.quit()
