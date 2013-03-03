import nltk
import pickle

fin = open('tweets.list',"r")
string = fin.read()
tweets = pickle.loads(string)
fin.close()

tweets_filtered = []

for tweet, tweet_type in tweets:
    filtered = [e.lower() for e in tweet.split(" ") if len(e) >= 3]
    special_words = []
    for word in filtered:
    	if word.startswith("#") or word.startswith("@"):
    		special_words.append(word)
    if special_words :
    	tweets_filtered.append((filtered,tweet_type,special_words))
    	print (filtered,tweet_type,special_words)
    else :
    	tweets_filtered.append((filtered,tweet_type,False))

print len(tweets_filtered)
