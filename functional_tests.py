from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. she does
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # she is invited to enter a to-do item straight away


if __name__ == '__main__':
    unittest.main(warnings='ignore')
