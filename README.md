# Mapping Road Closures using Real-Time Traffic Information

----

_By: Yichen Hu, Christopher Thompson and Rachel Koenig_

### Problem Statement:

Evacuation is of utmost importance during a natural disaster.  Often times, however, a person's usual exit route may be blocked or closed and regular mapping services could be down. Also, many of the current platforms do not rely on real-time data, so we can produce inaccurate or inefficient results.

This project will use Twitter news feeds and Here.com to identify real time road closures or damaged roads, power outages and other blocked routes that may affect traffic lights, travel time, travel safety and more.  
Our end result will allow the user (the public or rescue teams) to search by address to output latitude and longitude which will then output a searchable dataframe of tweets about nearby closed roads and a live map identifying their specific locations. 

**Prerequisites to run the included notebooks** 
 
- [Twitter API credentials:](https://developer.twitter.com/en/apps)   
Acquiring this api is a lengthy process and requires a twitter account and to provide some personal info such as a phone #.  You will also need to pip install the python [tweepy](https://www.tweepy.org/) library  to authorize api access.

- [HERE API credentials:](https://developer.here.com/)
HERE offers mapping and location services to companies such as Grab, Samsung, Bing Maps and AWS.  We 

- Geocoding API and Maps Javascript API from [google devloper console:](https://console.developers.google.com/apis/)
You will also need to pip install python [gmaps](https://jupyter-gmaps.readthedocs.io/en/latest/install.html) library to authorize access.


**This repository contains:** 

- Jupyter notebooks for live Twitter and HERE collection and parsing of road closure data
- A notebook to render a Google map with latitude & longitude point plotted for closed roads.
- Flask app 
- Unused code for future students iterations 

### Executive Summary 

Our goal was to be able to take in a user-specified location and return road closures for that location via both a Google Map and in a searchable csv file. We accomplished this by creating a Flask app that let's the user enter an address and outputs the location’s latitude and longitude. The coordinates and a number of other criteria would then pass into a function to scrape real-time Twitter and HERE data. 

### Data Collection

**HERE.com** 

The Here.com scrape notebook is set up to scrape live traffic information every time it is fun.  The site offers many options for mapping and traffic tools.  We chose to use their proximity filter which passes in a set of coordinates and searches a 40 mile radius. The output is a large nested dictionary.  Using multiple for loops, we sorted and sliced our way through to find the name of the closed road, a description of where the closure started and ended, the reason i.e. construction, mud slide, fire, etc, and the latitude and longitude. 

**Twitter** 

Using the Tweepy library we scraped the most recent (default 100) tweets from a user-specified Twitter account that has traffic info.  We programmed the function to have a default username of  @TotalTrafficLA because, we learned, after filtering through 227 Los Angeles news, traffic and weather accounts, that most tweets for relevant searches such as “road closure” don’t actually contain useful information regarding evacuation routes. We even looked at tweets specifically from the time and location of the Malibu Woolsey fire, including many from local residents, but @TotalTrafficLA was the only one that consistently provided start and end points and used predictive words like "road closed" which made it easier for our parsing to interpret the text, and therefore more efficient for extracting location information. 
In addition, Twitter’s search API is not meant to be an exhaustive list of all Tweets so using this method could cause us to miss out on relevant tweets from accounts with valuable tweets such as TotalTrafficLA. 

The output of the scraping function is a DataFrame that is saved to a csv file and loaded into the Tweet Parsing notebook. This notebook extracts the information from those tweets into a searchable csv file that can be used with Google Maps. This was mainly for usability. It’s far easier to search through a csv file using control/command + F as opposed to doing so via a dataframe and Python.

**Real-time road closure data versus historic data from a specific disaster**
Our initial goal was to output a list of road closures from November 2018 in Malibu, CA during the Woosley Fire. While we did collect the data, see Unused Code folder, wer were unable to use it in our final presenation for two reasons:
1. Twitter’s API search limits visibility to tweets of maximum 7 days old. 
2. We used GetOldTweets3 library to gather these tweets, but they were returned without the geolocation data that is provided from real-time tweets.  The historic tweets we scrapped via GetOldTweets3 only had intersection data regarding what was closed on which highway. Unfortunately, the mapping APIs we tried were unable to take an intersection involving a highway and turning that into a coordinate point.  

### Mapping Tool

Location data is loaded in from HERE and Twitter and formatted to work with gmaps, including splitting latitude and longitude into two columns, as well as converting from strings to floats.   Coordinates columns are set to variables that can be passed into the gmaps function. Red is assigned to HERE closure points and blue to Twitter closure points.

![Screenshot]("map screenshot.png")


### Workflow 

We experienced many surprises while working through this project.  Almost everyday for the first week we would make a plan and by the end of the day, something would happen to reroute us. 
One major decision was whether or not we needed a model.  We considered creating a model to classify tweets into useful and non-useful in identifying if a road is closed, and then only parsing the useful tweets for our dataframe of closures. In the process of classifying tweets for this model, we noticed that the only account that had useful tweets were TotalTrafficLA. At that point, we realized for the purposes of this project, a model was not needed.  A potential future development would be to create a model that can handle a variety of tweets, but we’d also need a better parsing function to make this a viable option.


### Future Iterations 

- Add labels to the google map: To improve the usability of our output, we would ideally like to be able to show the text of the tweet or here.com closure when you’re hovering over the point in google maps. 
- Run all notebooks through Flask: Ideally we would want our flask app to accept in the location, distance, and a designated twitter account based on city on the home page form and output the full google map with plotted closuress, plus a searchable list of the incidents to save or print from your computer.
- Better parsing function: Our Tweet parsing notebook currently relies on the very specific text patterns used by TotalTrafficLA. Ideally, we’d want to create a model that can generalize better to a broad spectrum of Twitter accounts.

## Sources 
----

Documentation 

GitHub Repos (previous DSI cohorts)

https://github.com/balak4/Optimizing-Evac-Routes

https://github.com/ariellem2/Disaster_Response_Maps


## Team
----
Rachel Koenig | https://www.linkedin.com/in/rachelmkoenig/
Yichen Hu | https://www.linkedin.com/in/yichenhu114/
Christopher Thompson | https://www.linkedin.com/in/christophercharlesthompson323/
