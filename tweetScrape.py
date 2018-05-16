import markovify
from twitter_scraper import get_tweets
tweetTest = get_tweets('realDonaldTrump', pages=1)
#for t in tweetTest:
	#print(t)
tweets = '\n'.join([t['text'] + '|' + t['time'].strftime("%Y-%m-%d|%H:%M:%S") for t in get_tweets('realDonaldTrump', pages=25)])
print("Tweets:\n" + tweets)
tweet_model = markovify.Text(tweets)

print(tweet_model.make_short_sentence(140))