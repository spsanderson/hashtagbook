import sys
import time
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=""
access_token_secret=""

class StdOutListener(StreamListener):
        """ A listener handles tweets are the received from the stream.
        This is a basic listener that just prints received tweets to stdout.

        """
        def on_status(self, data):
            try:
                print '%s , %s , %s , %s , %s' % (data.text,\
                data.author.screen_name,data.created_at,data.source,\
                data.coordinates)
                return True
            except Exception, e:
                print >> sys.stderr, 'Encountered Exception:', e
                pass

        def on_error(self, status):
            return True

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)	
    stream.filter(track=['']) 

