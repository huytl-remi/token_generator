import unittest
from utils.helpers import validate_ticker, sanitize_input, extract_json_from_markdown

class TestHelpers(unittest.TestCase):

    def test_validate_ticker(self):
        self.assertTrue(validate_ticker("ABC"))
        self.assertTrue(validate_ticker("ABCD"))
        self.assertTrue(validate_ticker("ABCDE"))
        self.assertFalse(validate_ticker("AB"))
        self.assertFalse(validate_ticker("ABCDEF"))
        self.assertFalse(validate_ticker("abc"))
        self.assertFalse(validate_ticker("AB3"))

    def test_sanitize_input(self):
        self.assertEqual(sanitize_input("Hello, World!"), "Hello World")
        self.assertEqual(sanitize_input("  Spaces  "), "Spaces")
        self.assertEqual(sanitize_input("No-Special@Chars"), "No-SpecialChars")

    def test_extract_json_from_markdown(self):
        markdown = '```json\n{"key": "value"}\n```'
        result = extract_json_from_markdown(markdown)
        self.assertEqual(result, '{"key": "value"}')

        plain_json = '{"key": "value"}'
        result = extract_json_from_markdown(plain_json)
        self.assertEqual(result, '{"key": "value"}')

        no_json = 'This is not JSON'
        result = extract_json_from_markdown(no_json)
        self.assertEqual(result, 'This is not JSON')

if __name__ == '__main__':
    unittest.main()
