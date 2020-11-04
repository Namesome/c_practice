import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy


def data_load():
    data = pd.read_csv('cust_therm_comm.csv')
    data = data.loc[data['SATISFACTION_RATING_SCORE'] == 'bad']
    print(data)
    data = data.iloc[:, 4].dropna()
    print(data)
    return data


def preprocessing(data):
    nlp = spacy.load('en_core_web_lg')
    result = [[tkn.lemma_ for tkn in nlp(sentence) if
               (tkn.lower_ not in nlp.Defaults.stop_words and not tkn.is_punct and tkn.lemma_ != '-PRON-')]
              for sentence in data]
    result = [' '.join(i) for i in result]
    print(result)
    return result


def tf_pipeline(preprocessed_data):
    cv = CountVectorizer(stop_words='english', strip_accents='unicode', max_features=100, ngram_range=(3, 4))
    word_count_vector = cv.fit_transform(preprocessed_data)

    # print(word_count_vector)
    # print(word_count_vector.todense())
    # print(cv.vocabulary_)
    # print(cv.get_feature_names())

    tf_sums = np.array(word_count_vector.sum(axis=0)).flatten()

    word_and_tf = []
    for word, val in zip(cv.get_feature_names(), tf_sums):
        word_and_tf.append((word, val))
    return word_and_tf


def tfidf_pipeline(preprocessed_data):
    tfidf_vectorizer = TfidfVectorizer(use_idf=True, stop_words='english', max_features=50, ngram_range=(3, 5))
    tfidf_vector = tfidf_vectorizer.fit_transform(preprocessed_data)

    # print(f"{tfidf_vectorizer_vectors}\n\n{tfidf_vectorizer_vectors.todense()}\n\n\n")
    # print(tfidf_vectorizer.get_stop_words())
    # print(tfidf_vectorizer.vocabulary_)

    tfidf_sums = np.array(tfidf_vector.sum(axis=0)).flatten()

    word_and_tfidf = []
    for word, val in zip(tfidf_vectorizer.get_feature_names(), tfidf_sums):
        word_and_tfidf.append((word, val))
    return word_and_tfidf


def export_tf(tf_pipeline_result):
    df = pd.DataFrame(tf_pipeline_result, columns=["term", "tf"])
    df.sort_values(by=["tf", "term"], ascending=False, inplace=True)
    print(df)
    with open('tf.csv', 'w', ) as f:
        df.to_csv(f)


def export_tfidf(tf_pipeline_result):
    df = pd.DataFrame(tf_pipeline_result, columns=["term", "tf_idf"])
    df.sort_values(by=["tf_idf", "term"], ascending=False, inplace=True)
    print(df)
    with open('tf_idf.csv', 'w', ) as f:
        df.to_csv(f)


if __name__ == "__main__":
    pd.set_option('display.max_rows', None, 'display.max_columns', None)
    data = data_load()
    preprocessed_data = preprocessing(data)
    # tf_pipeline_result = tf_pipeline(preprocessed_data)
    tfidf_pipeline_result = tfidf_pipeline(preprocessed_data)
    # export_tf(tf_pipeline_result)
    export_tfidf(tfidf_pipeline_result)
