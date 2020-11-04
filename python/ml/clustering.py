import numpy as np
import pandas as pd
from sklearn import naive_bayes
from sklearn import model_selection
from sklearn import feature_extraction
from sklearn import metrics

from sklearn.cluster import KMeans, MiniBatchKMeans
from time import time
import pandas as pd


def initialize_settings():
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.max_columns', None)


def load_data(file_name):
    data = pd.read_csv(file_name
                       , encoding="ANSI"
                       , header=0
                       , names=['target', 'id', 'date', 'flag', 'user', 'text']
                       )
    # print(data)
    return data


def preprocess_data(data):
    features = data.iloc[:, 5] \
               + data.iloc[:, 4] + data.iloc[:, 2]
    labels = data['target']
    # print(features)
    features_train, features_test, labels_train, labels_test = model_selection.train_test_split(
        features, labels
        , test_size=0.2
        # , random_state=42
        , shuffle=True
        , stratify=None
    )
    return features, labels, features_train, labels_train, features_test, labels_test


def vectorize_features(features_train, features_test):
    vectorizer = feature_extraction.text.TfidfVectorizer(
        encoding='ANSI'
        , decode_error='strict'
        , strip_accents='ascii'
        , lowercase=True
        , preprocessor=None
        , tokenizer=None
        , analyzer='word'
        , stop_words='english'
        , ngram_range=(1, 2)
        , max_df=1.0
        , min_df=1
        , max_features=None
        , vocabulary=None
        , binary=False
        , norm='l2'
        , use_idf=True
        , smooth_idf=True
        , sublinear_tf=False)

    vectorized_features_train = vectorizer.fit_transform(features_train)
    vectorized_features_test = vectorizer.transform(features_test)

    # vocabulary = vectorizer.get_feature_names()
    # print(pd.DataFrame(data=vectorized_features_train.toarray(), columns=vocabulary))
    # vocab_values_sorted = {k: v for k, v in
    #                        sorted(dict(zip(vocabulary, vectorized_features_train.toarray().mean(axis=0))).items(),
    #                               key=lambda item: item[1], reverse=True)}
    # print(f"Average of tf-idf scores across documents:\n{vocab_values_sorted}")

    return vectorizer, vectorized_features_train, vectorized_features_test


def apply_model(vectorizer, vectorized_features_train, labels_train, vectorized_features_test, labels_test):
    model = KMeans(n_clusters=10, init='k-means++', max_iter=10, n_init=1, verbose=1)

    print("Clustering sparse data with %s" % model)
    t0 = time()
    model.fit(vectorized_features_train)
    print("done in %0.3fs" % (time() - t0))
    print()

    print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, model.labels_))
    print("Completeness: %0.3f" % metrics.completeness_score(labels, model.labels_))
    print("V-measure: %0.3f" % metrics.v_measure_score(labels, model.labels_))
    print("Adjusted Rand-Index: %.3f"
          % metrics.adjusted_rand_score(labels, model.labels_))
    print("Silhouette Coefficient: %0.3f"
          % metrics.silhouette_score(vectorized_features_train, model.labels_, sample_size=1000))

    print()


    print("Top terms per cluster:")

    order_centroids = model.cluster_centers_.argsort()[:, ::-1]

    terms = vectorizer.get_feature_names()
    for i in range(10):
        print("Cluster %d:" % i, end='')
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind], end='')
        print()

if __name__ == "__main__":
    initialize_settings()
    data = load_data('training.1600000.processed.noemoticon.csv')
    features, labels, features_train, labels_train, features_test, labels_test = preprocess_data(data)
    vectorizer, vectorized_features_train, vectorized_features_test = vectorize_features(features_train, features_test)
    apply_model(vectorizer, vectorized_features_train, labels_train, vectorized_features_test, labels_test)
