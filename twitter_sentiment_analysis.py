"""
Twitter API
1. Register for the Twitter API https://apps.twitter.com/
2. Create an app  to generate various keys associated with the API. 

handles the Twitter API - tweepy library
Tweepy supports OAuth authentication. Authentication is handled by the tweepy.OAuthHandler class.An OAuthHandler instance is created by passing a consumer token and secret.On this auth instance, a function set_access_token by passing the access_token and access_token_secret.


Sentiment analysis - Textblob library
It is the process of determining the emotion of the writer, whether it is positive or negative or neutral.sentiment analysis with textblob is Lexicon-based(rule-based) method which defines a list of positive and negative words.

Textblob returns two properties polarity and subjectivity.
1. Polarity is float which lies in the range of [-1,1] where 1 means positive statement and -1 means a negative statement. 
2. subjectivity refers that mostly it is a public opinion and not a factual information.Subjectivity is also a float which lies in the range of [0,1].
"""

#pip install tweepy

#pip install textblob

import tweepy 
from tweepy import OAuthHandler 

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer # Importing the NaiveBayesAnalyzer classifier from NLTK

# keys and tokens from the Twitter Dev Console 
consumer_key = '****************************'
consumer_secret = '************************************************'
access_token = '*************************************************'
access_token_secret = '*********************************************'

# attempt authentication 
try: 
    # create OAuthHandler object 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    # set access token and secret 
    auth.set_access_token(access_token, access_token_secret)
    # create tweepy API object to fetch tweets 
    api = tweepy.API(auth)
except: 
    print("Error: Authentication Failed")

# Preparing an input sentence and working on it.
sentence = "Python is a high-level, general-purpose programming language."
# Creating a textblob object and assigning the sentiment property
analysis = TextBlob(sentence).sentiment
print("Sentiment analysis=",analysis)
analysisPol = TextBlob(sentence).polarity
analysisSub = TextBlob(sentence).subjectivity
print("polarity=",analysisPol)
print("subjectivity=",analysisSub)

import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('brown')

example = TextBlob("Python is a high-level, general-purpose programming language.")

print(example.words)
print(example.sentences)
print(example.tags)
print(example.noun_phrases)
print(example.words[2].singularize())
print(example.words[-1].pluralize())
print(example.words.pluralize())
print(example.correct())

# This command will call back 5 tweets within a “lockdown” topic
corpus_tweets = api.search("lockdown", count=5) 

positive = 0
negative = 0
neutral = 0
for tweet in corpus_tweets:
    #print(tweet)
    print(tweet.text)
    print(tweet.user.screen_name)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    
    if analysis.sentiment[0]>0:       
      print ('Positive')
      positive += 1    
    elif analysis.sentiment[0]<0:       
      print ('Negative')
      negative += 1    
    else:       
      print ('Neutral')
      neutral += 1 
    print('*'*100)

#Creating PieCart
import matplotlib.pyplot as plt
labels = ['Positive ['+str(positive)+'%]' , 'Neutral ['+str(neutral)+'%]','Negative ['+str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'blue','red']
patches, texts = plt.pie(sizes,colors=colors, startangle=90)
plt.style.use('default')
plt.legend(labels)
plt.title("Sentiment Analysis Result for keyword= lockdown")
plt.axis('equal')
plt.show()

import nltk
nltk.download('movie_reviews')

# Applying the NaiveBayesAnalyzer
blob_object = TextBlob(sentence, analyzer=NaiveBayesAnalyzer())
# Running sentiment analysis
analysis = blob_object.sentiment
print(analysis)
