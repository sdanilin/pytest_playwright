'''Setting global fixture'''

from pytest import fixture
from playwright.sync_api import sync_playwright
from page_objects.App import App
import settings


fixture(autouse=True, scope='session')
def precondition():
    print('hello')
    yield
    print('world')

@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='session')
def desktop_app(get_playwright):
    app = App(get_playwright, base_url=settings.BASE_URL)
    app.goto('/')
    yield app
    app.close()

@fixture(scope='session')
def desktop_app_auth(desktop_app):
    desktop_app.app.goto('/login')
    desktop_app.app.login(**settings.USER)
    yield app