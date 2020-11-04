import numpy
import pandas
from sklearn import model_selection
from sklearn import metrics
from textblob.classifiers import NaiveBayesClassifier


def data_load():
    pandas.set_option('display.max_rows', 20, 'display.max_columns', None)
    data = pandas.read_csv('labeled_product_sup_tickets_2019_to_2020.csv').iloc[:50, :]
    train_test_filter = data.dropna(subset=['PRODUCT'])
    classify_filter = data[data['PRODUCT'].isna()].dropna(subset=['SUBJECT'])
    return train_test_filter, classify_filter


def sets_prepare(train_test_filter):
    train_dataframe, test_dataframe = model_selection.train_test_split(train_test_filter, test_size=0.2)
    train_data = list(zip(train_dataframe['SUBJECT'], train_dataframe['PRODUCT']))
    test_data = list(zip(test_dataframe['SUBJECT'], test_dataframe['PRODUCT']))
    # print(train_data, '\n')
    # print(test_data, '\n')
    return train_data, test_data


def textblob_naivebayes(train_data, test_data, classify_filter):
    cl = NaiveBayesClassifier(train_data)
    print("\nF1 score:",
          metrics.classification_report([i[1] for i in test_data], [cl.classify(i[0]) for i in test_data]
                                        # , pos_label="account_api"
                                        # , average=None
                                        )
          )

    classify_data = classify_filter['SUBJECT'].unique()
    temp1 = []
    temp2 = []
    for i in classify_data:
        # print(i, cl.classify(i))
        temp1.append(i)
        temp2.append(cl.classify(i))

    classify_dataframe = pandas.DataFrame(numpy.column_stack([temp1, temp2]),
                                          columns=['subject', 'predicted_label']
                                          )

    with open('classifier.csv', 'w') as f:
        classify_dataframe.to_csv(f)


if __name__ == "__main__":
    train_test_filter, classify_filter = data_load()
    train_data, test_data = sets_prepare(train_test_filter)
    textblob_naivebayes(train_data, test_data, classify_filter)
    # scikit_mnb(train_data, test_data)
    # scikit_bnb
    # nltk_nb
    # custom? as class?
