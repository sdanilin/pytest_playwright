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
def desktop_app(get_playwright, request):
    base_url = request.config.getini('base_url')
    app = App(get_playwright, base_url=base_url)
    app.goto('/')
    yield app
    app.close()

@fixture(scope='session')
def desktop_app_auth(desktop_app):
    desktop_app.app.goto('/login')
    desktop_app.app.login(**settings.USER)
    yield app

def pytest_addoption(parser):
    # parser.addoption('--base_url', action='store', default='http://127.0.0.1:8000')
    parser.addini('base_url', help='base url of site under test', default='http://127.0.0.1:8000')