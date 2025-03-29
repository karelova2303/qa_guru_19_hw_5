import pytest
from selene import browser


@pytest.fixture(scope='function')
def browser_options():
    browser.config.window_width = '1280'
    browser.config.window_height = '720'
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()