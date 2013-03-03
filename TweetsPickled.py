"""
Parses the tweet dataset 

tweets = [(tweets_message,tweet_type,tweet_id), ......]

tweets object is pickled later.
"""
import pickle

f1 = open("training.txt","r")
tweet = f1.next()
tweets = []
tweets_sports = []
tweets_politics = []
while tweet:
	string = tweet[tweet.index("\'")+1:-2]
	category = tweet.split(" ")[1]
	person_id = tweet.split(" ")[0]
	tweets.append( ( 
		              str( string ),
		              category,
		              person_id
		            )
	             )
	if category == "Sports":
		tweets_sports.append(
			                   (
					              str( string ),
					              category,
					              person_id
			                   )
			                )

	elif category == "Politics": 
		tweets_politics.append(
			                   (
					              str( string ),
					              category,
					              person_id
			                   )
			                )

	try : 
	    tweet = f1.next()
	except :
		tweet = False

print "Total tweets : ", len(tweets)

print "Sports tweets : ",len(tweets_sports) 

print "Politics tweets : ",len(tweets_politics) 

string = pickle.dumps(tweets)
fout = open('tweets.list', 'w')
fout.write(string)
fout.close()

string = pickle.dumps(tweets_sports)
fout = open('tweets_sports.list', 'w')
fout.write(string)
fout.close()

string = pickle.dumps(tweets_politics)
fout = open('tweets_politics.list', 'w')
fout.write(string)
fout.close()
