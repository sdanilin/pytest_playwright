from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, devtools=True, slow_mo=500)
    context = browser.new_context()
    context = browser.new_context(viewport={"width": 1920, "height": 1080})

    # Open new page
    page = context.new_page()
    # Go to http://127.0.0.1:8000/login/?next=/
    page.goto("http://127.0.0.1:8000/login/?next=/")
    # Click input[name="username"]
    page.locator("input[name=\"username\"]").click()
    # Fill input[name="username"]
    page.locator("input[name=\"username\"]").fill("alice")
    # Press Tab
    page.locator("input[name=\"username\"]").press("Tab")
    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill("Qamania123")
    # Click text=Login
    page.locator("text=Login").click()
    page.wait_for_url("http://127.0.0.1:8000/")
    # Click text=Create new test
    page.locator("text=Create new test").click()
    page.wait_for_url("http://127.0.0.1:8000/test/new")
    # Click input[name="name"]
    page.locator("input[name=\"name\"]").click()
    # Fill input[name="name"]
    page.locator("input[name=\"name\"]").fill("hello")
    # Press Tab
    page.locator("input[name=\"name\"]").press("Tab")
    # Fill textarea[name="description"]
    page.locator("textarea[name=\"description\"]").fill("world")
    # Click input:has-text("Create")
    page.locator("input:has-text(\"Create\")").click()
    page.wait_for_url("http://127.0.0.1:8000/test/new")
    # Click text=Test Cases
    page.locator("text=Test Cases").click()
    page.wait_for_url("http://127.0.0.1:8000/tests/")

    assert page.query_selector_all('body > main > div > div > div > div.testTableBox > table > tbody > tr.testRow_42 > td:nth-child(2)') is not None

    # Click text=3 hello world alice Norun None PASS FAIL Details Delete >> button >> nth=3
    page.locator("text=42 hello world alice Norun None PASS FAIL Details Delete >> button").nth(3).click()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

def test_new_testcases():
    with sync_playwright() as playwright:
        run(playwright)
