import pytest
from selenium import webdriver
import time
import math

class BasePage():
    def __init__(self, browser, url):
        self.browser=browser
        self.url=url
    def open(self):
        self.browser.get(self.url)