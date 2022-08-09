from playwright.sync_api import Playwright
from .test_cases import TestCases


class App:
    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless, slow_mo=50)
        self.context = self.browser.new_context(viewport={"width": 1920, "height": 1080})
        self.page = self.context.new_page()
        self.base_url = base_url
        self.test_case = TestCases(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def navegate_to(self, menu: str):
        self.page.locator(f"css=header >> text=\"{menu}\"").click()

    def login(self, login: str, password: str):
        self.page.locator("input[name=\"username\"]").fill(login)
        self.page.locator("input[name=\"password\"]").fill(password)
        self.page.locator("text=Login").click()

    def create_test(self, test_name: str, test_desription: str):
        self.page.locator("text=Create new test").click()
        self.page.locator("input[name=\"name\"]").fill(test_name)
        self.page.locator("textarea[name=\"description\"]").fill(test_desription)
        self.page.locator("input:has-text(\"Create\")").click()

    def check_test_exists(self, test_name: str):
        return self.page.query_selector(f'css=tr >> text=\"\"{test_name}') is not None

    def delete_test_by_name(self, test_name: str):
        row = self.page.query_selector(f'*css=tr >> text=\"\"{test_name}')
        row.query_selector('.deleteBtn').click()

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
