# RealiTweet: Sentiment and user-intent analysis of real-time streamed tweets


##How to use:
1.Replace: 

&nbsp;
consumer_key='...........................'
consumer_secret='..................'
access_token='.............'
access_token_secret='...............', with the actual values for your application. 
And replace **(track=["...."])** *-in line 42 of TweetStream*  with the actual keyword to filter the stream with.

##Necessary installs:
1.tweepy
2.newlinejson
3.xmltodict

##Note:
1. Information obtained in *http://www.text-analytics101.com/2014/10/all-about-stop-words-for-text-mining.html* has been used to determine stop-words.
2. *http://www.aiaioo.com* Intention API has been used for determinig user intent (it's open-source :p)!
