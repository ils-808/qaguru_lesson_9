import allure
from allure_commons.types import Severity
from selene import browser, be
from selene.support import by


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "qwe")
@allure.feature("Задачи в репозитории")
@allure.story("Переход в репо")
@allure.link("https://github.com", name="Testing")
def test_gihub_wihtout_allure():
    browser.open("https://github.com/")
    browser.element(".header-search-button").click()
    browser.element("[name=query-builder-test]").type("eroshenkoam/allure-example")
    browser.element("[name=query-builder-test]").press_enter()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#76")).should(be.visible)

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "qwe")
@allure.feature("Задачи в репозитории")
@allure.story("Переход в репо с with allure.step")
@allure.link("https://github.com", name="Testing")
def test_gihub_wiht_allure_step():
    with allure.step("Open https://github.com/"):
        browser.open("https://github.com/")
    with allure.step("Navigate to input, type and search"):
        browser.element(".header-search-button").click()
        browser.element("[name=query-builder-test]").type("eroshenkoam/allure-example")
        browser.element("[name=query-builder-test]").press_enter()
    with allure.step("Go into repo"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step("Go into issues"):
        browser.element("#issues-tab").click()
    with allure.step("Check #76's issue is visible"):
        browser.element(by.partial_text("#76")).should(be.visible)

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "qwe")
@allure.feature("Задачи в репозитории")
@allure.story("Переход в репо с декоратором @allure.step")
@allure.link("https://github.com", name="Testing")
def test_github_with_decorator_allure():
    open_browser("https://github.com/")
    navigate_type_search("eroshenkoam/allure-example")
    go_to_repo("eroshenkoam/allure-example")
    go_into_issue()
    issue_visible("#76")


@allure.step("Open browser with URL: {url}")
def open_browser(url):
    browser.open(url)


@allure.step("Search repo with name {reponame}")
def navigate_type_search(reponame):
    browser.element(".header-search-button").click()
    browser.element("[name=query-builder-test]").type(reponame)
    browser.element("[name=query-builder-test]").press_enter()


@allure.step("Go into repo {reponame}")
def go_to_repo(reponame):
    browser.element(by.link_text(reponame)).click()


@allure.step("Go into issues")
def go_into_issue():
    browser.element("#issues-tab").click()


@allure.step("Check {issue_id} is visible")
def issue_visible(issue_id):
    browser.element(by.partial_text(issue_id)).should(be.visible)
