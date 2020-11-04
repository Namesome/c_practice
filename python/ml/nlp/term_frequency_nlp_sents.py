import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import spacy


def data_load():
    data = pd.read_csv('all_sup_groups_tickets_oct_2019.csv')
    ticket_subjects = data.iloc[:, 2].dropna()
    final_data = []
    for i in ticket_subjects:
        final_data.append(i)
    final_data = '. '.join(final_data)
    # print(f"{final_data}\n")
    return final_data


def preprocessing_sents(data):
    nlp = spacy.load('en_core_web_lg')
    # print(len(data))
    nlp.max_length = 25000000
    data_nlp = nlp(data)

    # for i in data_nlp:
    #     print(i)
    result = [[tkn.lemma_ for tkn in sent if
               (tkn.lower_ not in nlp.Defaults.stop_words and not tkn.is_punct
                and tkn.lemma_ != '-PRON-'
                )]
              for sent in data_nlp.sents]
    # print(result)
    result = [' '.join(i) for i in result]
    # print(result)
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
    with open('tf_experiment.csv', 'w', ) as f:
        df.to_csv(f)


if __name__ == "__main__":
    pd.set_option('display.max_rows', None, 'display.max_columns', None)
    data = data_load()
    preprocessed_data = preprocessing_sents(data)
    tf_pipeline_result = tf_pipeline(preprocessed_data)
    export(tf_pipeline_result)
