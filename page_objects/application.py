from playwright.sync_api import Playwright

class App:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False, devtools=True, slow_mo=500)
        self.context = self.browser.new_context(viewport={"width": 1920, "height": 1080})
        self.page = self.context.new_page()
        self.page.goto("http://127.0.0.1:8000/login/?next=/")

    def login(self):
        self.page.locator("input[name=\"username\"]").fill("alice")
        self.page.locator("input[name=\"password\"]").fill("Qamania123")
        self.page.locator("text=Login").click()

    def create_test(self):
        self.page.locator("text=Create new test").click()
        self.page.locator("input[name=\"name\"]").fill("hello")
        self.page.locator("textarea[name=\"description\"]").fill("world")
        self.page.locator("input:has-text(\"Create\")").click()

    def open_tests(self):
        self.page.locator("text=Test Cases").click()

    def check_test_created(self):
        return self.page.query_selector_all('text=hello') is not None


    def delete_test(self):
        self.page.locator("text=hello world alice Norun None PASS FAIL Details Delete >> button").nth(3).click()

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
