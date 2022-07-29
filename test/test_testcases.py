from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()

    page.goto("http://127.0.0.1:8000/login/?next=/")

    page.locator("input[name=\"username\"]").fill("alice")
    page.locator("input[name=\"password\"]").fill("Qamania123")
    page.locator("input[name=\"password\"]").press("Enter")

    page.locator("text=Create new test").click()
    page.locator("input[name=\"name\"]").fill("hello")
    page.locator("textarea[name=\"description\"]").fill("world")
    page.locator("input:has-text(\"Create\")").click()

    page.locator("text=Test Cases").click()

    # assert page.query_selector_all('td[text()="hello"]') is not None

    page.locator("text=40 hello world alice Norun None PASS FAIL Details Delete >> button").nth(3).click()

    page.close()
    context.close()
    browser.close()

def test_new_testcases():
    with sync_playwright() as playwright:
        run(playwright)
