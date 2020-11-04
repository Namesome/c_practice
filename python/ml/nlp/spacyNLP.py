import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
import math
import matplotlib.pyplot as plt

text = "Hi Andy, What is the best way I can add French addresses via the Nexmo dashboard after purchasing phone" \
       " numbers via the API. Since scaling and efficiency is critical for us now, we need a programatic solution" \
       " for provisioning new phone numbers. We can go back and add addresses" \
       " after the fact if this is possible. Can you tell me how to do that? Thank you, James I'm don't gonna cos"
text2 = "Hi, The information provided by Nexmo Support is incorrect. We originally created a nexmo.com account using " \
        "the email address support@ezyb2b.com.au When we went to help.nexmo.com to create a support ticket we had to " \
        "create a user account on help.nexmo.com for support@ezyb2b.com.au also. " \
        "When we changed the email address for nexmo.com from support@ezyb2b.com.au to rah@nellerconnect.com.au the " \
        "help.nexmo.com account remained associated with the email address support@ezyb2b.com.au. " \
        "This is my third attempt to communicate this to you. Your developers will understand what is going on. " \
        "Please delegate this support ticket to somebody who understands this matter."

nlp = spacy.load('en_core_web_lg')
doc = nlp(text)
doc2 = nlp(text2)

for token in doc:
    print(token.norm_, token.vector_norm)

for sent in doc.sents:
    print(sent, sent.vector_norm)

# print(doc.vector_norm, doc2.vector_norm)
# print(doc.similarity(doc2))
print(doc.vector_norm, doc2.vector_norm)

plt.plot(doc.vector_norm, doc2.vector_norm, 'ro')
plt.ylabel('some numbers')
plt.show()


# spacy.displacy.serve(doc, style="dep")
