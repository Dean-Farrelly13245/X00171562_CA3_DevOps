from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def _get_driver():
    """Helper function to create and configure Chrome driver"""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def test_add_operation():
    driver = _get_driver()
    driver.get("http://localhost:5000")

    driver.find_element(By.ID, "num1").send_keys("4")
    driver.find_element(By.ID, "num2").send_keys("6")
    driver.find_element(By.ID, "add").click()

    time.sleep(1)

    result_text = driver.find_element(By.ID, "result").text
    number_part = result_text.replace("Result:", "").strip()
    assert float(number_part) == 10.0

    driver.quit()

def test_subtract_operation():
    driver = _get_driver()
    driver.get("http://localhost:5000")

    driver.find_element(By.ID, "num1").send_keys("10")
    driver.find_element(By.ID, "num2").send_keys("3")
    driver.find_element(By.ID, "subtract").click()

    time.sleep(1)

    result_text = driver.find_element(By.ID, "result").text
    number_part = result_text.replace("Result:", "").strip()
    assert float(number_part) == 7.0

    driver.quit()

def test_multiply_operation():
    driver = _get_driver()
    driver.get("http://localhost:5000")

    driver.find_element(By.ID, "num1").send_keys("5")
    driver.find_element(By.ID, "num2").send_keys("4")
    driver.find_element(By.ID, "multiply").click()

    time.sleep(1)

    result_text = driver.find_element(By.ID, "result").text
    number_part = result_text.replace("Result:", "").strip()
    assert float(number_part) == 20.0

    driver.quit()

def test_divide_operation():
    driver = _get_driver()
    driver.get("http://localhost:5000")

    driver.find_element(By.ID, "num1").send_keys("20")
    driver.find_element(By.ID, "num2").send_keys("4")
    driver.find_element(By.ID, "divide").click()

    time.sleep(1)

    result_text = driver.find_element(By.ID, "result").text
    number_part = result_text.replace("Result:", "").strip()
    assert float(number_part) == 5.0

    driver.quit()
