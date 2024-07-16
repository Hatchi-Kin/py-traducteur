from transformers import pipeline
from config.parametres import VERSIONS
from model.prompt import Prompt

def traduire(prompt:Prompt) :
    if prompt.version == VERSIONS[0] :
        translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
    elif prompt.version == VERSIONS[1] :
        translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
        
    # the model returns a list containing a dictionary, we need to extract the translation
    prompt.traduction = translator(prompt.atraduire)[0]["translation_text"]
    return prompt
