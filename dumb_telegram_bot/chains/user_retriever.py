"""
Small rag over a list of usernames
"""

from langchain_core.prompts import PromptTemplate

from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

RETRIEVER_PROMPT_TEMPLATE="What's {user}'s nickname?"
PROMPT_INPUT_VARIALE=["user"]


class UserRetrieverRagChain:
    """
    Implements a ridiculously small chain to retrieve the
    Telegram user name in a given list, given a similar name/nickname
    """

    def __init__(self, list_users: list):

        self.prompt_finder_template = PromptTemplate.from_template(template=RETRIEVER_PROMPT_TEMPLATE, input_variable=PROMPT_INPUT_VARIALE)
        
        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-large",
            dimensions=500
        )
        vectorstore = InMemoryVectorStore.from_texts(
            list_users,
            embedding=embeddings,
        )

        self.retriever = vectorstore.as_retriever()


    def get_telegram_username(self, user: str):
        
        formatted_prompt = self.prompt_finder_template.format(user=user)
        return self.retriever.invoke(formatted_prompt)[0].page_content