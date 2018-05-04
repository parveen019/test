import json
import csv
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


ckey = 'gpc6OM9wmn5EW4fvgsvagq1hd'
csecret = '6KRJKGonstTrk19m3zzDhUvylprNK4e0Exk1HEdGi8Cjgno3hp'
atoken = '3671482992-9hE6dy8okMlGCvKzaRdxbBhjQ1jkyK7KHbOQMzF'
asecret = 'ZlLcstjLDYbq1vJlm909oIMTv8Z1bkIZjJyNkZ4Fst9VH'


class Listener(StreamListener):
	def on_data(self,data):
		datanew = json.dumps(data,indent=4)
		print datanew
		return True
	def on_error(self,status):
			print status.text
			return True


auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,Listener())
twitterStream.filter(track=["modi"])