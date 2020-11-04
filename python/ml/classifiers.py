import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report


def sklearn_to_df(sklearn_dataset):
    df = pd.DataFrame(sklearn_dataset.data, columns=sklearn_dataset.feature_names)
    df['target'] = pd.Series(sklearn_dataset.target)
    df['target_names'] = pd.Series(sklearn_dataset.target_names)
    return df


if __name__ == "__main__":
    data_iris = load_iris()
    df_iris = sklearn_to_df(data_iris)
    print(df_iris)
