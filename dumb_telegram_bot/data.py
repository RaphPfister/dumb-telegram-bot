"""
Small util module to process the history of a telegram
Implements a minimalistic class-interface to fetch data from a databas
Because this is a prototype, feel free to implement your own database class
"""

from abc import ABC, abstractmethod
import json

import pandas as pd


def read_and_select_columns(path: str):
    """ """
    with open(path, "r") as f:
        data_dict = json.load(f)

    df = pd.DataFrame(data_dict["messages"])

    return df[["from", "text", "text_entities"]]


def process(df: pd.DataFrame) -> pd.DataFrame:
    """ """
    df = df[df["text"] != ""].copy()
    df["raw_text"] = df["text_entities"].apply(lambda x: dict(x[0])["text"])

    return df


class Database(ABC):

    @abstractmethod
    def get_table() -> pd.DataFrame:
        """Abstract method to read a whole table. Returns a pandas dataframe"""
        raise NotImplementedError

    @abstractmethod
    def get_sample_from_user(self, n_samples: int, username: str) -> pd.DataFrame:
        """Samples n rows from the data"""
        raise NotImplementedError

    @abstractmethod
    def get_unique_users(self) -> list:
        """Samples n rows from the data"""
        raise NotImplementedError


class LocalPandasDatabase(Database):

    def __init__(self, path: str):
        tmp_df = read_and_select_columns(path=path)
        self.df = process(tmp_df)

    def get_table(self) -> pd.DataFrame:
        return self.df

    def get_sample_from_user(self, n_samples: int, username: str) -> list:
        """
        Samples n rows from the data
        """

        df_subset = self.df[self.df["from"] == username].sample(n=n_samples).copy()

        return df_subset["raw_text"].to_list()

    def get_unique_users(self) -> list:
        """
        Returns a list of unique users
        """
        return self.df["from"].unique().tolist()
