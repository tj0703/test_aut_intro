"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:

    # locators

    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    # URL

    URL = 'https://www.duckduckgo.com'

    # Initiator

    def __init__(self, browser):
        self.browser = browser

    # Interac tion method

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
