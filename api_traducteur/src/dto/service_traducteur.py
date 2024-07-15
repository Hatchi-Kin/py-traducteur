from dto.connexion import Connexion
from model.prompt import Prompt
from model.utilisateur import Utilisateur

class Service_Traducteur(Connexion):

    @classmethod
    def sauvegarder_prompt(cls, prompt:Prompt):
        cls.ouvrir_connexion()
        query = "INSERT INTO prompts (text_in, text_out, version, utilisateur) VALUES (%s, %s, %s, %s)"
        translation_text = prompt.traduction[0]['translation_text']
        values = [str(prompt.atraduire), str(translation_text), str(prompt.version), int(prompt.utilisateur)]
        cls.cursor.execute(query, values)
        cls.bdd.commit()
        cls.fermer_connexion()
    
    @classmethod
    def verifier_login(cls, utilisateur:Utilisateur):
        try:
            cls.ouvrir_connexion()
            query = "SELECT id, login, mdp FROM utilisateurs WHERE login=%s AND mdp=%s"
            values = [utilisateur.login, utilisateur.mdp]
            cls.cursor.execute(query, values)
            result = cls.cursor.fetchone()

            if result :
                utilisateur.id = result['id']
                utilisateur.authentifie = True

        except Exception as e:
                print(f"Une erreur inattendue est survenue :{e}")
        
        finally:
            cls.fermer_connexion()

    @classmethod
    def lister_prompts(cls, utilisateur:int):
        prompts=[]

        cls.ouvrir_connexion()
        query = "SELECT * FROM prompts WHERE utilisateur=%s"
        values=[utilisateur]
        cls.cursor.execute(query, values)
            
        for prompt_lu in cls.cursor :
            prompt = Prompt(atraduire=prompt_lu["text_in"], traduction=prompt_lu["text_out"], version=prompt_lu["version"], utilisateur=prompt_lu["utilisateur"])
            prompts.append(prompt)

        cls.fermer_connexion()
        
        return prompts
                  
                  


