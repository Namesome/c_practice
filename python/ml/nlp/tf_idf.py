import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy


def data_load():
    data = pd.read_csv('sup_tickets_2019.csv')
    ticket_subjects = data.iloc[:, 1].dropna().str.strip()
    # print(ticket_subjects)
    return ticket_subjects


def preprocessing(data):
    nlp = spacy.load('en_core_web_lg')
    result = [[tkn.lemma_ for tkn in nlp(sentence) if
               (tkn.text not in nlp.Defaults.stop_words and not tkn.is_punct and tkn.lemma_ != '-PRON-')]
              for sentence in data]
    result = [' '.join(i) for i in result]
    return result


def tfidf_pipeline(preprocessed_data):
    tfidf_vectorizer = TfidfVectorizer(use_idf=True, stop_words='english', max_features=500, ngram_range=(4, 5))
    tfidf_vector = tfidf_vectorizer.fit_transform(preprocessed_data)

    # print(f"{tfidf_vectorizer_vectors}\n\n{tfidf_vectorizer_vectors.todense()}\n\n\n")
    # print(tfidf_vectorizer.get_stop_words())
    # print(tfidf_vectorizer.vocabulary_)

    tfidf_sums = np.array(tfidf_vector.sum(axis=0)).flatten()

    word_and_tfidf = []
    for word, val in zip(tfidf_vectorizer.get_feature_names(), tfidf_sums):
        word_and_tfidf.append((word, val))
    return word_and_tfidf


def export(tf_pipeline_result):
    df = pd.DataFrame(tf_pipeline_result, columns=["term", "tf_idf"])
    df.sort_values(by=["tf_idf", "term"], ascending=False, inplace=True)
    print(df)
    with open('tf_idf.csv', 'w', ) as f:
        df.to_csv(f)


if __name__ == "__main__":
    pd.set_option('display.max_rows', None, 'display.max_columns', None)
    data = data_load()
    preprocessed_data = preprocessing(data)
    tf_pipeline_result = tfidf_pipeline(preprocessed_data)
    export(tf_pipeline_result)
