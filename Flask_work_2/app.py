from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
import numpy as np
import pandas as pd
import tweepy
from geopy.distance import geodesic
import json
app = Flask(__name__)

json_file = open('../twitter_creds.json')
json_str = json_file.read()
json_data = json.loads(json_str)

#Code taken from http://www.dealingdata.net/2016/07/23/PoGo-Series-Tweepy/
auth = tweepy.OAuthHandler(json_data['API key'],json_data['API secret key'])
auth.set_access_token(json_data['Access token'], json_data['Access token secret'])

#Creating a twitter API wrapper using tweepy
api = tweepy.API(auth)

#Error handling
if (not api):
    print ("Problem connecting to API")

geolocator = Nominatim(user_agent = "DSI_US_8_LA")
def latlong(point):
  coord = geolocator.geocode(point)
  coordinates = coord.latitude,coord.longitude
  return coordinates

def TweetSearch(location = 0,distance = 25,user = 'TotalTrafficLA',limit = 100):
    full_text = []
    author = []
    creation_time = []
    hashtags = []
    geo = []

    for tweet in tweepy.Cursor(api.user_timeline,id=user,tweet_mode='extended').items(limit):
        if tweet.geo != None:
            if geodesic(location,tweet.geo['coordinates']).miles <= distance:
                full_text.append(tweet.full_text)
                author.append(tweet.author.screen_name)
                creation_time.append(tweet.created_at)
                hashtags.append(hashtag_process(tweet.entities['hashtags']))
                geo.append(tweet.geo['coordinates'])
    return "This is return of function"

def hashtag_process(raw):
    if len(raw)==0:
        return None
    else:
        output = []
        for x in raw:
            if x.get('text') != 'LAtraffic':
                output.append(x.get('text'))
        return output

@app.route('/send', methods=['GET', 'POST'])
def send():
  if request.method == 'POST':
    print(request.form)
    location = request.form['location']

    return render_template('location.html', location=location)

  return render_template('index.html')

@app.route('/TweetSearch', methods=['GET', 'POST'])
def tweetroute():
    location = request.form['location']
    i = latlong(location)
    a = TweetSearch(i)

    return str(a)


if __name__ == "__main__":
  app.run()
