import unittest
from unittest.mock import patch
from typing import List, Dict, Any, Optional
from src.token_generator import generate_tokens, parse_json_response
from utils.helpers import extract_json_from_markdown

class TestTokenGenerator(unittest.TestCase):
    @patch('src.token_generator.generate_text')
    def test_generate_tokens_text_only(self, mock_generate_text):
        mock_generate_text.return_value = '{"tokens": [{"name": "ArtCoin", "ticker": "ART", "description": "A token for digital artists", "visual_elements": ["palette", "brush", "canvas"]}]}'
        tokens = generate_tokens("Create a token for digital art")
        self.assertIsInstance(tokens, list)
        self.assertEqual(len(tokens), 1)
        self.assertIsInstance(tokens[0], dict)
        self.assertEqual(tokens[0].get('name'), "ArtCoin")
        self.assertEqual(tokens[0].get('ticker'), "ART")

    @patch('src.token_generator.generate_text')
    def test_generate_tokens_with_image(self, mock_generate_text):
        mock_generate_text.return_value = '{"tokens": [{"name": "NatureCoin", "ticker": "NCN", "description": "A token inspired by nature", "visual_elements": ["leaf", "tree", "sun"]}]}'
        tokens = generate_tokens("Create a nature-inspired token", "fake_image.jpg")
        self.assertIsInstance(tokens, list)
        self.assertEqual(len(tokens), 1)
        self.assertIsInstance(tokens[0], dict)
        self.assertEqual(tokens[0].get('name'), "NatureCoin")
        self.assertEqual(tokens[0].get('ticker'), "NCN")

    def test_parse_json_response_markdown(self):
        markdown_response = '```json\n{"tokens": [{"name": "TestCoin", "ticker": "TST"}]}\n```'
        parsed = parse_json_response(markdown_response)
        self.assertIsNotNone(parsed)
        self.assertIsInstance(parsed, dict)
        self.assertIn('tokens', parsed)
        self.assertIsInstance(parsed['tokens'], list)
        self.assertEqual(parsed['tokens'][0].get('name'), "TestCoin")

    def test_parse_json_response_plain(self):
        plain_response = '{"tokens": [{"name": "PlainCoin", "ticker": "PLN"}]}'
        parsed = parse_json_response(plain_response)
        self.assertIsNotNone(parsed)
        self.assertIsInstance(parsed, dict)
        self.assertIn('tokens', parsed)
        self.assertIsInstance(parsed['tokens'], list)
        self.assertEqual(parsed['tokens'][0].get('name'), "PlainCoin")

    def test_parse_json_response_invalid(self):
        invalid_response = 'Not a JSON string'
        parsed = parse_json_response(invalid_response)
        self.assertIsNone(parsed)
