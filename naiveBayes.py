import nltk
import pickle

fin = open('tweets.list',"r")
string = fin.read()
tweets = pickle.loads(string)
fin.close()

tweets_filtered = []

for tweet, tweet_type in tweets:
    filtered = [e.lower() for e in tweet.split(" ") if e not in nltk.corpus.stopwords.words('english')]
    special_words = []
    for word in filtered:
    	if word.startswith("#") or word.startswith("@"):
    		special_words.append(word)
    if special_words :
    	tweets_filtered.append((filtered,tweet_type,special_words))
    else :
    	tweets_filtered.append((filtered,tweet_type,False))

string = pickle.dumps(tweets_filtered)
fout = open('tweets_filtered.list', 'w')
fout.write(string)
fout.close()