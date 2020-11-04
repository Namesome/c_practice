import pandas as pd
import textblob
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import sklearn

train = [
    ('I love this sandwich.', 'pos'),
    ('this is an amazing place!', 'pos'),
    # ('I feel very good about these beers.', 'pos'),
    # ('this is my best work.', 'pos'),
    ("what an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    # ("I can't deal with this", 'neg'),
    # ('he is my sworn enemy!', 'neg'),
    # ('my boss is horrible.', 'neg')
]
test = [
    ('the beer was good.', 'pos'),
    ('I do not enjoy my stuff', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg'),
    ("This is an amazing library!", 'pos')
]

cl = textblob.classifiers.NaiveBayesClassifier(train)

for i in test:
    print(i[0])
    print(cl.extract_features(i[0]))
    print("Verdict:", cl.classify(i[0]))
    print("Probability of positive:", cl.prob_classify(i[0]).prob('pos'))
    print("Probability of negative:", cl.prob_classify(i[0]).prob('neg'))
    print("\n")

print("\nAccuracy:", cl.accuracy(test))
print(sklearn.metrics.f1_score([i[1] for i in test], [cl.classify(i[0]) for i in test], pos_label="pos"))

# blob = TextBlob("The beer is good. But the hangover is horrible.", classifier=cl)
# print(blob.classify())
# for s in blob.sentences:
#     print(s)
#     print(s.classify())
# print(cl.accuracy(test))

cl.show_informative_features()
