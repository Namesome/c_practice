import nltk


def word_feats(words):
    return dict([(word, True) for word in words.split()])


pos_train = [
    ('I love this sandwich.', 'pos'),
    # ('this is an amazing place!', 'pos'),
    # ('I feel very good about these beers.', 'pos'),
    # ('this is my best work.', 'pos'),
    ("what an awesome view", 'pos')
]
neg_train = [
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    # ("I can't deal with this", 'neg'),
    # ('he is my sworn enemy!', 'neg'),
    # ('my boss is horrible.', 'neg')
]
words_list = []
for (words, sentiment) in pos_train + neg_train:
    words_filtered = [e for e in words.split()]
    words_list.append((words_filtered, sentiment))

test = [
    ('the beer was good.', 'pos'),
    ('I do not enjoy my stuff', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg'),
    ("This is an amazing library!", 'pos')
]


def get_words(words_list):
    all_words = []
    for (words, sentiment) in words_list:
        all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


word_features = get_word_features(get_words(words_list))

print(word_features)


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    print(features)
    return features


training_set = nltk.classify.apply_features(extract_features, words_list)
classifier = nltk.NaiveBayesClassifier.train(training_set)

print(classifier.show_most_informative_features())

for i in test:
    print(i[0])
    print(classifier.prob_classify(extract_features(i[0].split())).prob('pos'))
    print("\n")
