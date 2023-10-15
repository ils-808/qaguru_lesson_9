import allure
import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def configure_browser():
    browser.config.driver.maximize_window()

    yield

    browser.close()
