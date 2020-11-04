import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import spacy


def data_load():
    data = pd.read_csv('sup_tickets_2019.csv')
    ticket_subjects = data.iloc[:, 1].dropna()
    print(ticket_subjects)
    return ticket_subjects


def preprocessing(data):
    nlp = spacy.load('en_core_web_md')
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


def export(tf_pipeline_result):
    df = pd.DataFrame(tf_pipeline_result, columns=["term", "tf"])
    df.sort_values(by=["tf", "term"], ascending=False, inplace=True)
    print(df)
    with open('tf.csv', 'w', ) as f:
        df.to_csv(f)


if __name__ == "__main__":
    pd.set_option('display.max_rows', None, 'display.max_columns', None)
    data = data_load()
    preprocessed_data = preprocessing(data)
    tf_pipeline_result = tf_pipeline(preprocessed_data)
    export(tf_pipeline_result)
