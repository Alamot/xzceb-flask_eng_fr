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
        print("Testing english_to_french for null")
        self.assertEqual(english_to_french(""),"")

    def test_word_hello_en2fr(self):
        print("Testing english_to_french with assertEqual")
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        print("Testing english_to_french with assertNotEqual")
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")

    """
    French to English Translation Test
    """
    def test_when_null_fr2en(self):
        print("Testing french_to_english for null")
        self.assertEqual(french_to_english(""),"")

    def test_word_hello_fr2en(self):
        print("Testing french_to_english with assertEqual")
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        print("Testing french_to_english with assertNotEqual")
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")


unittest.main()
