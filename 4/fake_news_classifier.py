# -*- coding: utf-8 -*-
"""Fake News Classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mVfun8L0GEgRfXETwAefREpLxy4RrvyL
"""

import pandas as pd

df= pd.read_csv('/content/drive/MyDrive/train.csv')

df.head()

X=df[['title','author','text']]
X

y=df[['label']]
y

df=df.dropna()
df.head(10)

messages=df.copy()
messages.reset_index(inplace=True)
messages.head(10)

messages['text'][6]
messages.head()

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
ps = PorterStemmer()
corpus = []
for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['text'][i])
    review = review.lower()
    review = review.split()
    
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)

corpus

tfidf=TfidfVectorizer(max_features=1500,ngram_range=(1,3))
X=tfidf.fit_transform(corpus).toarray()

X.shape

y=messages['label']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

tfidf.get_feature_names()

df1 = pd.DataFrame(X_train, columns=tfidf.get_feature_names())

df1.head()

"""<b>Naive bayes"""

from sklearn.naive_bayes import MultinomialNB
classifier=MultinomialNB()
from sklearn import metrics
import numpy as np
import itertools
classifier.fit(X_train, y_train)
pred = classifier.predict(X_test)
score = metrics.accuracy_score(y_test, pred)
print("accuracy:   %0.6f" % score)
cm = metrics.confusion_matrix(y_test, pred)
cm

"""<b>Passive Aggressive Classifier Algorithm"""

from sklearn.linear_model import PassiveAggressiveClassifier
linear_clf = PassiveAggressiveClassifier()
linear_clf.fit(X_train, y_train)
pred = linear_clf.predict(X_test)
score = metrics.accuracy_score(y_test, pred)
print("accuracy:   %0.6f" % score)
cm = metrics.confusion_matrix(y_test, pred)
cm

"""<b>Count Vectorizer"""

count=CountVectorizer(max_features=1500,ngram_range=(1,3))
X=count.fit_transform(corpus).toarray()

y=messages['label']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

df2 = pd.DataFrame(X_train, columns=tfidf.get_feature_names())

df2.head()

from sklearn.naive_bayes import MultinomialNB
classifier=MultinomialNB()
from sklearn import metrics
import numpy as np
import itertools
classifier.fit(X_train, y_train)
pred = classifier.predict(X_test)
score = metrics.accuracy_score(y_test, pred)
print("accuracy:   %0.6f" % score)
cm = metrics.confusion_matrix(y_test, pred)
cm

from sklearn.linear_model import PassiveAggressiveClassifier
linear_clf = PassiveAggressiveClassifier()
linear_clf.fit(X_train, y_train)
pred = linear_clf.predict(X_test)
score = metrics.accuracy_score(y_test, pred)
print("accuracy:   %0.6f" % score)
cm = metrics.confusion_matrix(y_test, pred)
cm