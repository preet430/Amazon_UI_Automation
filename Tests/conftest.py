import time
import pytest
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def browser_setup(request) :
    global driver

    #To get the browser name from the command line
    browser_name = request.config.getoption("browser_name")

    #To maximize the window for default Chrome browser
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")

    if browser_name == "chrome" :
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox" :
        driver = webdriver.Firefox()
    elif browser_name == "edge" :
        driver = webdriver.Edge()

    driver.maximize_window() #Maximize the window before test for Firefox & Edge Browser
    driver.implicitly_wait(5) #Global wait
    driver.get("https://www.amazon.in/")
    driver.implicitly_wait(15)
    request.cls.driver = driver #By using this, We can use the driver object in another class. And this will be the class variable
    yield
    driver.close()






