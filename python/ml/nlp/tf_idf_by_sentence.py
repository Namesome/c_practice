import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy


def data_load():
    data = pd.read_csv('sup_tickets_2019.csv')
    ticket_subjects = data.iloc[:, 1].dropna().str.strip()
    print(ticket_subjects)
    return ticket_subjects


def preprocessing(data):
    nlp = spacy.load('en_core_web_lg')
    result = [[tkn.lemma_.lower() for tkn in nlp(sentence) if
               (tkn.text.lower() not in nlp.Defaults.stop_words and not tkn.is_punct and tkn.lemma_ != '-PRON-')]
              for sentence in data]
    result = [' '.join(i) for i in result]
    return result


def tfidf_pipeline(preprocessed_data):
    tfidf_vectorizer = TfidfVectorizer(use_idf=True, strip_accents='unicode')
    tfidf_vector = tfidf_vectorizer.fit_transform(preprocessed_data)

    # print(f"{type(tfidf_vector)}\n\n{tfidf_vector.todense()}\n\n\n")
    # print(tfidf_vectorizer.get_stop_words())
    print(tfidf_vectorizer.vocabulary_)

    tfidf_sentence_averages = np.array(tfidf_vector.sum(axis=1)).flatten() / tfidf_vector.getnnz(axis=1)
    print(tfidf_sentence_averages)

    sentence_and_tfidf = []
    for sentence, value in zip(preprocessed_data, tfidf_sentence_averages):
        # print(sentence, value)
        sentence_and_tfidf.append((sentence, value))

    temp_df = pd.DataFrame(sentence_and_tfidf, columns=['term', 'tf_idf'])
    temp_df = temp_df.groupby(['term']).sum().sort_values(by=['tf_idf', 'term'], ascending=False, inplace=False)
    # print(sentence_and_tfidf)
    return temp_df


def export(tf_pipeline_result):
    print(tf_pipeline_result)
    with open('tf_idf.csv', 'w', ) as f:
        tf_pipeline_result.to_csv(f)


if __name__ == "__main__":
    pd.set_option('display.max_rows', None, 'display.max_columns', None)
    data = data_load()
    preprocessed_data = preprocessing(data)
    tf_pipeline_result = tfidf_pipeline(preprocessed_data)
    export(tf_pipeline_result)
