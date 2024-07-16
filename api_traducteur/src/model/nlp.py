import time
from transformers import pipeline
from config.parametres import VERSIONS
from model.prompt import Prompt

def traduire(prompt: Prompt):
    start_time = time.time()
    
    if prompt.version == VERSIONS[0]:
        translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
    elif prompt.version == VERSIONS[1]:
        translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
    
    print(prompt.traduction)
    # the model returns a list containing a dictionary, we need to extract the translation
    prompt.traduction = translator(prompt.atraduire)[0]["translation_text"]
    
    end_time = time.time()
    prompt.execute_time = end_time - start_time
    
    return prompt