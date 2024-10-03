import time
from transformers import pipeline
from config.parametres import VERSIONS
from model.prompt import Prompt


def traduire(prompt: Prompt):
    start_time = time.time()
    
    try:       
        if prompt.version == VERSIONS[0]:
            translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
        elif prompt.version == VERSIONS[1]:
            translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
        
        result = translator([prompt.atraduire])[0]
        
        if not isinstance(result, dict) or "translation_text" not in result:
            raise ValueError("Translation result does not contain expected keys")
        
        if not isinstance(result["translation_text"], str):
            raise ValueError("Translation text is not a string")
        
        prompt.traduction = result["translation_text"]
    
    except Exception as e:
        prompt.traduction = f"Failed to translate: {str(e)}"
    
    finally:
        end_time = time.time()
        prompt.execute_time = end_time - start_time
    
    return prompt