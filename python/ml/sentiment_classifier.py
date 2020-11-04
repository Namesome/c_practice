import numpy as np
import pandas as pd
from sklearn import naive_bayes
from sklearn import model_selection
from sklearn import feature_extraction
from sklearn import metrics


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
    features = data.iloc[:, 5]\
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

    return vectorized_features_train, vectorized_features_test


def apply_model(vectorized_features_train, labels_train, vectorized_features_test, labels_test):
    model = naive_bayes.MultinomialNB()
    # print(sorted(metrics.SCORERS.keys()))
    parameters = {
        # 'fit_prior': ('True', 'False'),
        'alpha': np.arange(0.01, 1, 0.1)
    }
    grid = model_selection.GridSearchCV(estimator=model
                                        , param_grid=parameters
                                        , scoring='f1_micro'
                                        , n_jobs=-1
                                        , cv=5
                                        , refit=True
                                        , verbose=1
                                        , error_score='raise'
                                        , return_train_score=False
                                        )
    grid.fit(vectorized_features_train, labels_train)

    print(pd.DataFrame(grid.cv_results_))
    print(grid.best_estimator_)
    print(grid.best_score_)

    labels_predicted = grid.predict(vectorized_features_test)
    print(metrics.classification_report(labels_test, labels_predicted))
    print(metrics.confusion_matrix(labels_test, labels_predicted))

    return labels_predicted


if __name__ == "__main__":
    initialize_settings()
    data = load_data('training.1600000.processed.noemoticon.csv')
    features, labels, features_train, labels_train, features_test, labels_test = preprocess_data(data)
    vectorized_features_train, vectorized_features_test = vectorize_features(features_train, features_test)
    labels_predicted = apply_model(vectorized_features_train, labels_train, vectorized_features_test, labels_test)

    summary = pd.DataFrame(dict(actual=labels_test, pred=labels_predicted, features=features_test))
    # print(summary)
    summary.to_csv('test.csv')
