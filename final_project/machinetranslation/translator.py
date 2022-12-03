"""
Main code for translation services
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-11-28',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    Translate english to french
    """
    if not english_text:
        return ""
    frenchtranslation = language_translator.translate(
                        text=english_text,
                        model_id='en-fr').get_result()
    french_text = frenchtranslation.get("translations")[0].get("translation")
    return french_text


def french_to_english(french_text):
    """
    Translate french to english
    """
    if not french_text:
        return ""
    englishtranslation = language_translator.translate(
                         text=french_text,
                         model_id='fr-en').get_result()
    english_text = englishtranslation.get("translations")[0].get("translation")
    return english_text
