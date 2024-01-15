import unittest

from scrape import scrape_colors_and_save_data_as_json


class TestWebScraping(unittest.TestCase):
    def test_scrape_website(self):
        self.assertEqual(scrape_colors_and_save_data_as_json(), 540)


if __name__ == '__main__':
    unittest.main()
