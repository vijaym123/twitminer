import nltk
import pickle

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
    	all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    global word_features
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def filter_tweet(tweet,tweet_type):
	words = tweet.split(" ")
	words_temp = []
	for e in words :
		word = ""
		if e.startswith("@") or e.startswith("http"):
			break;
		for i in range(len(e)):
			if e[i].isalpha() or e[i]=="'":
				word+=e[i]
			else :
				if word!="" or len(word)>2:
					words_temp.append(word)
				word=""
	filtered = [e.lower() for e in words_temp if e not in nltk.corpus.stopwords.words('english') and len(e) > 3]
	return (filtered,tweet_type)

def main():
	fin = open('tweets_politics.list',"r")
	string = fin.read()
	tweets_politics = pickle.loads(string)
	fin.close()
	fin = open('tweets_sports.list',"r")
	string = fin.read()
	tweets_sports = pickle.loads(string)
	fin.close()

	tweets_filtered = []

	for tweet, tweet_type in tweets_sports[:-15]+tweets_politics[:-15]:
		tweet_filter = filter_tweet(tweet,tweet_type)
		if tweet_filter[0]!=[]:
			tweets_filtered.append(tweet_filter)	
	global word_features
	word_features = get_word_features(get_words_in_tweets(tweets_filtered))
	training_set = nltk.classify.apply_features(extract_features, tweets_filtered)
	classifier = nltk.NaiveBayesClassifier.train(training_set)

	string = pickle.dumps(classifier)
	fout = open('classifier', 'w')
	fout.write(string)
	fout.close()

	
main()