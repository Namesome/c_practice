import pandas as pd
from textblob import TextBlob
import spacy


def load_data():
    data = pd.read_csv('cust_therm_comm.csv')
    data = data.loc[data['SATISFACTION_RATING_SCORE'] == 'good']
    data.dropna(subset=['RATING_COMMENT'], inplace=True)
    return data


def preprocess(data):
    # nlp = spacy.load('en_core_web_lg')
    # new_col = []
    # for i in data["RATING_COMMENT"][:5]:
    #     new_col.append(nlp(i))
    # print(new_col)
    return data


def sentiment(data):
    sentiment_data = data.assign(
        POLARITY=data['RATING_COMMENT'].apply(lambda x: TextBlob(x).sentiment.polarity),
        SUBJECTIVITY=data['RATING_COMMENT'].apply(lambda x: TextBlob(x).sentiment.subjectivity))

    sentiment_data.sort_values(by=['POLARITY'], ascending=True, inplace=True)
    sentiment_data['POLARITY'] = sentiment_data['POLARITY'].round(2)
    sentiment_data.drop(columns=['SATISFACTION_RATING_COMMENT'], inplace=True)
    # sentiment_data = sentiment_data.groupby(by='SATISFACTION_RATING_SCORE', as_index=False).mean()

    print(sentiment_data.nlargest(25, 'POLARITY'), '\n')
    return sentiment_data.head(30)


def export(sentiment_data):
    with open('sentiment.csv', 'w', ) as f:
        sentiment_data.to_csv(f, index=False, header=True)


if __name__ == "__main__":
    pd.set_option('display.max_rows', 30, 'display.max_columns', None)
    data = load_data()
    preprocessed_data = preprocess(data)
    sentiment_data = sentiment(preprocessed_data)
    export(sentiment_data)
