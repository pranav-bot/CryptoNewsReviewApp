import pandas as pd
from nltk.classify import NaiveBayesClassifier
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk import tokenize
import nltk

dataset = pd.read_csv('test-dataset.csv')

nltk.download('vader_lexicon')

n_instances = 100

subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]

train_subj_docs = subj_docs[:80]
test_subj_docs = subj_docs[80:100]
train_obj_docs = obj_docs[:80]
test_obj_docs = obj_docs[80:100]
training_docs = train_subj_docs+train_obj_docs
testing_docs = test_subj_docs+test_obj_docs
new_Words={
    'unauthorized':-0.2,
    'fixed':0.1,
    'compromised':-0.2
}
sentim_analyzer = SentimentAnalyzer()

all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])

unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)

sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

training_set = sentim_analyzer.apply_features(training_docs)

test_set = sentim_analyzer.apply_features(testing_docs)

trainer = NaiveBayesClassifier.train

classifier = sentim_analyzer.train(trainer, training_set)

#for key, value in sorted(sentim_analyzer.evaluate(test_set).items()):
 #   print('{0}: {1}'.format(key, value))

# dataset['title']=dataset['title'].astype(str)
# dataset['description']= dataset['description'].astype(str)
# for i in range(len(dataset)):
#     sentence = dataset['title'][i]
#     paragraph = dataset['description'][i]
#
# lines_list = tokenize.sent_tokenize(paragraph)
# sentence.extend(lines_list)
#
# for sentence in sentence:
#     sid = SentimentIntensityAnalyzer()
#     print(sentence)
#     ss = sid.polarity_scores(sentence)
#     for k in sorted(ss):
#         print('{0}: {1}, '.format(k, ss[k]), end='')
#         print()
SIA = SentimentIntensityAnalyzer()
SIA.lexicon.update(new_Words)

def sentimentanalysis(title, desc):
    sentence=title
    paragraph=desc
    lines_list = tokenize.sent_tokenize(paragraph)
    sentence.extend(lines_list)

    for sentence in sentence:
        sid = SIA
        print(sentence)
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]), end='')
            print()