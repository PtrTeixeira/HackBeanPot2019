InstaReader
============

About
------
The user experience for the visually impaired community is unacceptable across many social media platforms. In recent years, the development of artificial intelligence technologies has grown tremendously. Technologies like sentiment analysis, facial recognition, and object detection can be used to create an improved description of media content. Our goal is to set in motion the use of these tools to increase accessibility on social media.

Instagram is a perfect example of where this technology is lacking. Current screen readers can tell the user who posted a picture and lists the image tags if there are any in the photo. Generally, it simply reads the HTML text for the page. We want to take this further by creating a story for the user. We used machine learning algorithms and data scraping to form full sentences about the media post, allowing the user to generate the best mental image possible.

We created a user interface that mimics your own Instagram feed. We used a custom text-to-speech software that describes the posts in detail. This end-to-end application is a sample of the power of artificial intelligence capabilities and how social media platforms can utilize them. As the technologies continue to evolve, we hope social media companies like Instagram will implement them to better serve the visually impaired and people with all types of disabilities.  


To get started:
---------------

(You should probably edit the filename before you run this)

```
pip install -r requirements.txt
source .env
python test.py
```

will print out the label stuff from the Google Cloud Vision 
api.


Starting the web server
----------------------

```
pip install -r requirements.txt
FLASK_APP=server.py flask run
```

