from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import newlinejson as nlj
import urllib
import stopwords
import sentiment
import intention


consumer_key='...........................'
consumer_secret='..................'
access_token='.............'
access_token_secret='...............'

class listener(StreamListener):
	def on_data(self, data):
		dst=nlj.open("twitterJson.json", "w")
		all_data = json.loads(data)
		tweet = all_data["text"]
		tweet=tweet.encode('ascii',errors='ignore')
		tut=tweet.split()
		tut=tut[ :-1]
		newtut=stopwords.stop(tut)
		words=len(newtut)
		inti=" ".join(newtut)
		senti="+".join(newtut)
		intent=intention.intention(inti)
		ux=urllib.urlopen('http://www.sentiment140.com/api/classify?text='+senti+'&callback=myJsFunction')
		ru=ux.read()
		js=json.loads(ru)
		polarity=js['results']['polarity']
		sentimnt=sentiment.sentim(polarity)
		x={'coordinates':all_data['coordinates'],'WordCount':words,'tweet':tweet,'Sentiment':sentimnt,'Intent':intent}
		dst.write(x)
		print x
		exit()
	def on_error(self, status):
		print status
auth=OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["...."])