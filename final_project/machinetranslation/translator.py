import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

#loading the variables
apikey = os.environ['apikey']
url = os.environ['url']

# Prepare the Authenticator - creating an IBM Watson instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url(url)

# Function translation English to French
def english_to_french(english_text):
    # Translate
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return french_text

# Function translation French to English
def french_to_english(french_text):
    # Translate
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return english_text

# Some tests

print(list(english_to_french('black').values())[0].pop()['translation'])