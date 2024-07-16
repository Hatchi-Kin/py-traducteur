from pydantic import BaseModel

class Prompt(BaseModel) :
    atraduire : str
    traduction : str = None
    version : str
    utilisateur : int
    execute_time : float = None
