import numpy
import pandas
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import sklearn.metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import sys


def data_load():
    pandas.set_option('display.max_rows', 2000, 'display.max_columns', None)
    data = pandas.read_csv('all_sup_tickets_merged.csv'
                           , names=['ID', 'SUBJECT', 'DESCRIPTION', 'PRODUCT', 'COUNTRY', 'GROUP_NAME', 'PRODUCT_GROUP']
                           ).iloc[:, :]
    return data


def sets_prepare(data):
    train_test_filter = data.dropna(subset=['PRODUCT_GROUP', 'SUBJECT'
                                            # , 'DESCRIPTION'
                                            ])
    classify_filter = data[data['PRODUCT_GROUP'].isna()].dropna(subset=['SUBJECT'
                                                                        # , 'DESCRIPTION'
                                                                        ])

    return train_test_filter, classify_filter


def features_prepare(train_test_filter, classify_filter, **kwargs):
    features = train_test_filter['SUBJECT']
    labels = train_test_filter['PRODUCT_GROUP']
    unclassified_data = classify_filter['SUBJECT']

    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2
                                                                                , random_state=5
                                                                                )

    return features, labels, features_train, labels_train, features_test, labels_test, unclassified_data


def scikit_mnb(features, labels, features_train, labels_train, features_test, labels_test, unclassified_data):
    vectorizer = TfidfVectorizer(
        # input='content',
        encoding='utf-8',
        decode_error='strict',
        strip_accents=None,
        lowercase=True,
        preprocessor=None,
        tokenizer=None,
        # analyzer='word',
        stop_words=None,
        # token_pattern='(?u)\b\w\w+\b',
        ngram_range=(1, 1),
        # max_df=1.0,
        # min_df=1,
        max_features=None,
        # vocabulary=None,
        binary=False,
        norm='l2',
        use_idf=True,
        smooth_idf=False,
        sublinear_tf=False
    )
    classifier = MultinomialNB(alpha=0.01, fit_prior=True, class_prior=None)
    pipeline = Pipeline([('vectorizer', vectorizer), ('classifier', classifier)])

    # fit classifier
    pipeline.fit(features_train, labels_train)

    # # cross-validate on whole featureset
    # scores = cross_val_score(classifier, features_transformed, labels, cv=10, scoring='f1_micro')
    # print(scores)
    # print("F1_micro: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    # hyper parameter grid search
    parameters = {'classifier__alpha': numpy.arange(0.01, 1.01, 0.05)}
    gscv = GridSearchCV(estimator=pipeline
                        , param_grid=parameters
                        , scoring=None
                        , n_jobs=-1
                        , cv=5
                        , refit=True
                        , verbose=1
                        , return_train_score=False
                        )

    gscv.fit(features_train, labels_train)
    print(gscv.best_estimator_)
    # print(gscv.best_score_)
    # gscv_df = pandas.DataFrame(gscv.cv_results_)
    # print(gscv_df)

    # predictions
    labels_test_predict = pipeline.predict(features_test)
    labels_predict = gscv.predict(unclassified_data)

    gs_labels_test_predict = gscv.predict(features_test)

    # print(sklearn.metrics.accuracy_score(labels_test, labels_test_predict, normalize=False))
    print(f"MCC: {sklearn.metrics.matthews_corrcoef(labels_test, labels_test_predict)}")
    print(f"MCC: {sklearn.metrics.matthews_corrcoef(labels_test, gs_labels_test_predict)}")
    # print(sklearn.metrics.confusion_matrix(labels_test, labels_test_predict))
    # print(sklearn.metrics.multilabel_confusion_matrix(labels_test, labels_test_predict))
    print(sklearn.metrics.classification_report(labels_test, labels_test_predict))
    print(sklearn.metrics.classification_report(labels_test, gs_labels_test_predict))

    return labels_predict


def export_csv(classify_filter, labels_predict):
    frame = {
        # 'TICKET_ID': classify_filter['ID'],
        'SUBJECT': classify_filter['SUBJECT'],
        'LABELS_PREDICT': labels_predict}
    df = pandas.DataFrame(frame).drop_duplicates(keep='first').iloc[:, :]

    with open('scikit_mnb.csv', 'w') as f:
        df.to_csv(f)


if __name__ == "__main__":
    data = data_load()
    train_test_filter, classify_filter = sets_prepare(data)
    features, labels, features_train, labels_train, features_test, labels_test, unclassified_data = features_prepare(
        train_test_filter, classify_filter, tfidf='tfidf')
    # preprocessor function for mnb - lower, stem, norm
    labels_predict = scikit_mnb(features, labels, features_train, labels_train, features_test, labels_test,
                                unclassified_data)
    export_csv(classify_filter, labels_predict)
