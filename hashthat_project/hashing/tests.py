from django.test import TestCase
from selenium import webdriver

class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_homepage(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('install', self.browser.page_source)
        # assert browser.page_source.find('install')

    def tearDown(self):
        self.browser.quit()




