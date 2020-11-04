import requests
from bs4 import BeautifulSoup
import pandas
import nltk
from nltk.corpus import *
import pprint

# data import, narrowing down
with open('ticket_id_subject_body_since_oct.csv', 'r') as f:
    data = pandas.read_csv(f)

ticket_data = data[data['ID'] == 1167828]

ticket_subject = ticket_data.iloc[0, 1]

ticket_body = ticket_data.iloc[0, 2]

# NLP
stopw = stopwords.words('english')

# ticket_body = re.sub('[^A-Za-z .-]+', ' ', ticket_body)
# ticket_body = ' '.join([i for i in ticket_body.split() if i not in stopw])
# print(ticket_body)


sentences = nltk.sent_tokenize(ticket_body)
print(f'{sentences}\n')

tokens = [nltk.word_tokenize(i) for i in sentences]
print(f'{tokens}\n')

tokens_alt = nltk.word_tokenize(ticket_body)

tagged_tokens = [nltk.pos_tag(i) for i in tokens]
print(f'{tagged_tokens}\n')

tagged_tokens_alt = nltk.pos_tag(tokens_alt)

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = [cp.parse(i) for i in tagged_tokens]
result_alt = cp.parse(tagged_tokens_alt)
pprint.pprint(result_alt)
result_alt.draw()

# ne_chunked_tokens = [nltk.ne_chunk(i) for i in tagged_tokens]
# print(ne_chunked_tokens)

# nltk.app.chunkparser()