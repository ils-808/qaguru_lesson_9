import allure
import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def configure_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    browser.config.driver_options = options

    yield

    browser.close()
