import sys
import time
import tweepy
import ast
import os
import mimetypes
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.binder import bind_api
from tweepy.error import TweepError
from tweepy.parsers import ModelParser
from tweepy.utils import list_to_csv
from tweepy.api import API

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
                print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % \
                (data.text,
                data.author.screen_name,
                data.created_at,
                data.source,
                data.coordinates, 
                data.retweet_count,
                data.favorited,
                data.favorite_count,
                data.contributors,
                data.filter_level,
                data.in_reply_to_screen_name,
                data.retweeted,
                data.place)
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
    stream.filter(track=['3-D',
'ARG',
'DIY', 
'DJ VJ',
'activist',
'aesthetics',
'agency',
'algorithmic',
'animation',
'app',
'architecture',
'archive',
'art',
'science',
'artificial',
'asynchronous',
'audio',
'audio visual',
'augmented reality',
'avatar',
'bioart',
'biopolitics',
'biotechnology',
'booty calls',
'opps',
'censorship',
'chance',
'cinema',
'city',
'code',
'collaboration',
'collective community',
'conference',
'convergence',
'conversation',
'copyright',
'culture',
'cyberreality',
'dance',
'data',
'distributed',
'e-literature',
'ecology',
'education',
'emergence',
'environment',
'event',
'exhibition',
'fabbing',
'festival',
'film',
'forking',
'free',
'libre',
'software',
'games',
'generative',
'gesture',
'gift',
'economy',
'glitch',
'globalization',
'hacktivism',
'history',
'hybrid',
'hypermedia',
'identity',
'immaterial',
'image',
'immersive',
'installation',
'interactive',
'interdisciplinary',
'interface',
'intermedia',
'intervention',
'interview',
'labor',
'language',
'lecture',
'light',
'live',
'live cinema',
'livestage',
'locative',
'media',
'machinima',
'mapping',
'mashup',
'mobile media',
'motion tracking',
'multimedia',
'music',
'narrative',
'nature',
'net art',
'networked',
'new media',
'news',
'nonlinear',
'object',
'open source',
'p2p',
'participatory',
'perception',
'performance',
'physical place',
'place-specific',
'platform',
'play',
'political',
'presence',
'public',
'private',
'pyschogeography',
'radio',
'reblog',
'recycle',
're-enactment',
'relational',
'remix',
'research',
'responsive',
'robotic',
'second life',
'semantic web',
'simulation',
'site-specific',
'social',
'social choreography',
'social networks',
'software',
'sound',
'space',
'streaming',
'surveillance',
'synesthesia',
'synthetic',
'systems',
'tactical',
'tag',
'tangible',
'technology',
'telematic',
'text',
'theater',
'theory',
'tool',
'touch',
'transdisciplinary',
'tv',
'ubiquitous',
'unconference',
'upgrade',
'urban',
'video',
'virtual',
'visualization',
'voice',
'wearable',
'web 2.0',
'webcam',
'webcast',
'wireless',
'workshop',
'writings']) 
