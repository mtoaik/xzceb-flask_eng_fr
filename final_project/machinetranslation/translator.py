'''Module to call the ibm translator api and translate between en-fr and fr-en'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
APIKEY = str(os.environ['apikey'])
URL = str(os.environ['url'])
#version = 2018-05-01
authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2023-01-31',
    authenticator=authenticator,
)
language_translator.set_service_url(URL)

def englishToFrench(eng_text):
    '''function to tranlate english text to french '''
    #write the code here
    translation = language_translator.translate(text=eng_text, model_id='en-fr').get_result()
    french_text = translation["translations"][0]["translation"]
    #frenchText = json.dumps(translation, indent=2, ensure_ascii=False)
    #print(str(french_text))
    return french_text

def frenchToEnglish(french_text):
    '''function to translate french text to english '''
    #write the code here
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation["translations"][0]["translation"]
    #englishText = json.dumps(translation, indent=2, ensure_ascii=False)
    #print(str(english_text))
    return english_text
