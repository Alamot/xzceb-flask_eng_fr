"""
Unit Testing For translator.py
"""
import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """
    English to French Translation Test
    """
    def test_when_null_en2fr(self):
        self.assertEqual(english_to_french(""),"")

    def test_word_hello_en2fr(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    """
    French to English Translation Test
    """
    def test_when_null_fr2en(self):
        self.assertEqual(french_to_english(""),"")

    def test_word_hello_fr2en(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')


unittest.main()
