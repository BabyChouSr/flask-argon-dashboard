## Inspiration
1. Inability to predict wildfire: many current news sources such as ca.fire.gov and latimes.com currently show recent news about wildfire; however, that does not provide sufficient time for California residents to evacuate. Thus, we need a system that can predict wildfire movements, impact and spreading speed
2. Lack of knowledge of wildfire severity: current wildfire news sources also do not provide clear information about the severity of the fire, so users often do not know whether they need to evacuate or not. 
3. Unable to evacuate accordingly: current news sources do not give enough understanding about where wildfires are and where to evacuate to.

## What it does
Our application uses EazyML's model built on training data found on Kaggle's California wildfire dataset ranging from 2013-2019 in order to predict the likelihood and severity of wildfires in California. It also shows the timeline of wildfire severity across California, and the greatest causes for wildfire severity: acres burned, longitude, latitude, and crews involved.

## How we built it
Frontend: Bootstrap for HTML, JS, CSS
Backend: Flask, EazyML, Folium 

## Challenges we ran into
It was a slight challenge to get used to the EazyML's API calls instead of just using the normal sklearn or Keras, but after reading the documentation more thoroughly, the process was extremely easy. 

## Accomplishments that I'm proud of
We are proud of being able to provide users with significant information about wildfires in California and are able to act accordingly.

## What we learned
We learned how to pair EazyML with Flask. It was also a very good collaborative coding experience, which taught us about the importance of prioritizing tasks and modularizing jobs to get the application completed in time.

## What's next for Extinguish
We plan on licensing our application to government officials, which will allow us to provide the application free of cost to all California residents. We also plan to make a mobile version of the app to enable easy access.
