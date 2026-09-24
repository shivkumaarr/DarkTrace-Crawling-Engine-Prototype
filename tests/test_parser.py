import unittest
from crawler.parser import parse_html, normalize_url

class ParserTest(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize_url("https://example.com/a#test"),
                         "https://example.com/a")

    def test_links_and_title(self):
        html = '<html><title>Demo</title><a href="/a">A</a></html>'
        title, links = parse_html(html, "https://example.com/")
        self.assertEqual(title, "Demo")
        self.assertIn("https://example.com/a", links)

if __name__ == "__main__":
    unittest.main()
