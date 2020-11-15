from django.test import TestCase
from selenium import webdriver

class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_homepage(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Enter Hash here', self.browser.page_source)
        # assert browser.page_source.find('install')

    def test_hash_of_hello(self):
        self.browser.get('http://localhost:8000')
        text = self.browser.find_element_by_id('id_text')
        text.send_keys('hello')
        self.browser.find_element_by_name('submit').click()

    def tearDown(self):
        self.browser.quit()




