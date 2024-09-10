"""
Impements a llm chain that mimics a user on a given theme
"""
from typing import List

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


SYSTEM_PROMPT = """
Tu es un robot dans un chat telegram. 
Tu dois imiter la personne qui t'es demandée en te basant sur une liste d'exemple.
L'imitation doit être crédible et doit respecter la **syntaxe** et le **style de français** de la personne à imiter, étant donnée une certaine thématique.
Ne réponds pas par un texte déjà fourni, mais mélange différents textes. 
Ne dis rien d'autre que l'imitation. Ne produis qu'une seule imitation, courte, de 30 mots maximum et de plus de 5 mots.
"""


class MimickingChatBot:
    """
    Implements a ridiculously small chain to retrieve the
    Telegram user name in a given list, given a similar name/nickname
    """

    def __init__(self):
        
        prompt_mimic = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            ("system", "Voici des examples de texte de la personne à imiter: {text_samples}"),
            ("user", "Username: {person_to_mimic}, Thématique: {theme}")
        ])

        llm = ChatOpenAI(model="gpt-4o")

        parser = StrOutputParser()

        self.mimicking_chain = prompt_mimic | llm | parser

        
    def get_message(self, text_samples: List[str], person_to_mimic: str, theme: str):
        """
        Generates a message given the provided username, examples, and theme 
        """
        return self.mimicking_chain.invoke(input={"text_samples": text_samples, "person_to_mimic": person_to_mimic, "theme": theme})
