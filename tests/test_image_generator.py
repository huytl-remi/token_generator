import unittest
from unittest.mock import patch
from src.image_generator import generate_image

class TestImageGenerator(unittest.TestCase):

    @patch('src.image_generator.generate_image_url')
    def test_generate_image(self, mock_generate_image_url):
        mock_generate_image_url.return_value = 'http://fake-image-url.com/image.png'
        token = {
            "name": "ArtCoin",
            "description": "A token for digital art enthusiasts",
            "visual_elements": ["palette", "brush", "canvas"]
        }
        image_url = generate_image(token)
        self.assertIsNotNone(image_url)
        self.assertIsInstance(image_url, str)
        self.assertTrue(image_url.startswith('http'))
        mock_generate_image_url.assert_called_once()

    @patch('src.image_generator.generate_image_url')
    def test_generate_image_failure(self, mock_generate_image_url):
        mock_generate_image_url.return_value = None
        token = {
            "name": "FailCoin",
            "description": "A token that fails to generate an image",
            "visual_elements": ["error", "bug", "glitch"]
        }
        image_url = generate_image(token)
        self.assertIsNone(image_url)
