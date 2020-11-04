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
import sys


def data_load():
    pandas.set_option('display.max_rows', 20, 'display.max_columns', None)
    data = pandas.read_csv('all_sup_tickets_body_merged.csv'
                           , names=['ID', 'SUBJECT', 'DESCRIPTION', 'PRODUCT', 'COUNTRY', 'GROUP_NAME', 'PRODUCT_GROUP',
                                    'BODY']
                           ).iloc[:, :]
    return data


def sets_prepare(data):
    train_test_filter = data.dropna(subset=['PRODUCT_GROUP', 'SUBJECT'
        , 'DESCRIPTION'
        , 'BODY'
                                            ])
    classify_filter = data[data['PRODUCT_GROUP'].isna()].dropna(subset=['SUBJECT'
        , 'DESCRIPTION'
        , 'BODY'
                                                                        ])

    return train_test_filter, classify_filter


def features_prepare(train_test_filter, classify_filter, **kwargs):
    features = train_test_filter['BODY']
    labels = train_test_filter['PRODUCT_GROUP']
    unclassified_data = classify_filter['SUBJECT']

    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2
                                                                                # , random_state=5
                                                                                )

    if 'tf' in kwargs.values():
        c_v = CountVectorizer(
            # input='content',
            encoding='utf-8',
            decode_error='strict',
            strip_accents=None,
            lowercase=True,
            preprocessor=None,
            tokenizer=None,
            stop_words='english',
            # token_pattern='(?u)\b\w\w+\b',
            ngram_range=(1, 1),
            # analyzer='word',
            # max_df=1.0,
            # min_df=1,
            max_features=None,
            # vocabulary=None,
            binary=False
        )

        features_transformed = c_v.fit_transform(features)  # for cross-validation purposes
        c_v.fit(features_train)
        features_train_transformed = c_v.transform(features_train)
        features_test_transformed = c_v.transform(features_test)
        features_unlabeled_transformed = c_v.transform(unclassified_data)

        # # check TF for train data
        # tf_sums = numpy.array(features_train_transformed.sum(axis=0)).flatten()
        # word_and_tf = []
        # for word, val in zip(c_v.get_feature_names(), tf_sums):
        #     word_and_tf.append((word, val))
        # print(word_and_tf)

    elif 'tfidf' in kwargs.values():
        tfidf_v = TfidfVectorizer(
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

        features_transformed = tfidf_v.fit_transform(features)  # for cross-validation purposes
        tfidf_v.fit(features_train)
        features_train_transformed = tfidf_v.transform(features_train)
        features_test_transformed = tfidf_v.transform(features_test)
        features_unlabeled_transformed = tfidf_v.transform(unclassified_data)

        # # check TFIDF for train data
        # tfidf_sums = numpy.array(features_train_transformed.sum(axis=0)).flatten()
        # word_and_tfidf = []
        # for word, val in zip(tfidf_v.get_feature_names(), tfidf_sums):
        #     word_and_tfidf.append((word, val))
        # print(word_and_tfidf)

    else:
        sys.exit("Wrong argument passed, try 'tf' or 'tfidf'")

    return features_transformed, labels, features_train_transformed, labels_train, features_test_transformed, labels_test, features_unlabeled_transformed


def scikit_mnb(features_transformed, labels, features_train_transformed, labels_train, features_test_transformed,
               labels_test,
               features_unlabeled_transformed):
    classifier = MultinomialNB(alpha=0.01, fit_prior=True, class_prior=None)
    classifier.fit(features_train_transformed, labels_train)

    # cross-validate on whole featureset
    scores = cross_val_score(classifier, features_transformed, labels, cv=10, scoring='f1_micro')
    print(scores)
    print("F1_micro: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    labels_test_predict = classifier.predict(features_test_transformed)
    labels_predict = classifier.predict(features_unlabeled_transformed)

    # print(classifier.score(features_test_transformed, labels_test))
    # print(sklearn.metrics.accuracy_score(labels_test, labels_test_predict, normalize=False))
    print(f"MCC: {sklearn.metrics.matthews_corrcoef(labels_test, labels_test_predict)}")
    # print(sklearn.metrics.confusion_matrix(labels_test, labels_test_predict))
    # print(sklearn.metrics.multilabel_confusion_matrix(labels_test, labels_test_predict))
    print(sklearn.metrics.classification_report(labels_test, labels_test_predict))
    # print(classifier.classes_)
    # print(classifier.predict_proba(features_test_transformed), '\n')
    # print(classifier.predict_log_proba(features_test_transformed))

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
    features_transformed, labels, features_train_transformed, labels_train, features_test_transformed, labels_test, features_unlabeled_transformed = features_prepare(
        train_test_filter, classify_filter, tfidf='tfidf')
    labels_predict = scikit_mnb(features_transformed, labels, features_train_transformed, labels_train,
                                features_test_transformed, labels_test,
                                features_unlabeled_transformed)
    export_csv(classify_filter, labels_predict)
