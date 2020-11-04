import pandas as pd
import spacy


def data_load():
    data = pd.read_csv('all.csv'
                       , names=['TICKET_ID', 'BODY', 'COMMENTER']
                       ).iloc[:, :]
    parsed_data = list(data.iloc[:2, 0:2].itertuples(index=False, name=None))\
        # .dropna().str.strip()

    print(parsed_data)
    return parsed_data


def preprocessing(data):
    nlp = spacy.load('en_core_web_lg')
    # result = [[tkn.lemma_ for tkn in nlp(sentence) if
    #            (tkn.text not in nlp.Defaults.stop_words and not tkn.is_punct and tkn.lemma_ != '-PRON-')]
    #           for sentence in data]
    # result = [' '.join(i) for i in result]
    # result = nlp.pipe(data)
    # print(result)
    for doc, context in nlp.pipe(data, as_tuples=True):
        print(doc, context)


    # return result


if __name__ == "__main__":
    pd.set_option('display.max_rows', None, 'display.max_columns', None)
    data = data_load()
    preprocessed_data = preprocessing(data)
