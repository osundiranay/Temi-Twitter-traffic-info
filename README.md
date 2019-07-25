# woolsey_fire_traffic_map

**Problem 3: Optimizing Evacuation Routes using Real-Time Traffic Information**

*Problem Statement:*

Evacution is of utmost importance during a natural disaster.  Often times, however, a person's usual exit route may be blocked or closed. 

- During disasters, search and rescue teams must be able to search for and get to survivors as fast as possible (in terms of travel time and distance)
- Current GIS and navigation systems allow responders to calculate travel time and
distance between origin and destination and propose an optimal route to the destination.
- However, many of the current platforms do not rely on real-time data (e.g. road closures, damaged roads etc.) and can produce inaccurate or inefficient results.

- This project will use Twitter news feeds and other datasets such Here.com to identify real time road closures or damaged roads, power outages and other blocked routes that may affect traffic lights, travel time, travel safety and more.

- Our end result will allow the user (the public or rescue teams) to search for any of these conditions and identify if and where they exist in a specific location (street, neighborhood, city etc.)5


STRETCH GOAL:
Use flask to create an app where user types in address and it takes them to a page that shows a map of road closures. 

*Desired Deliverables:*
- A short write-up describing the project.
- An open source code that pulls live information from social media and/or news feeds about road closures, road conditions, damaged roads, power outages etc. which may
affect travel and accessibility.
- The output can be either tabular (e.g. allow for search of names of closed roads) or geospatial (e.g. produce a map of real-time road closures).