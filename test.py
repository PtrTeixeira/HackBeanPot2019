# from instagram_scraper.app import InstagramScraper
import io
import os

from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
file_name = "/home/teixeira/Downloads/instagram_tweet_pic.jpg"

def get_image_labels(image_content):
    image = types.Image(content=image_content)
    return client.label_detection(image=image)

def get_image_text(image_content):
    image = types.Image(content=image_content)
    return client.text_detection(image=image)

def get_image_objects(image_content):
    image = types.Image(content=image_content)
    return client.object_localization(image=image)

def get_labels_from_filename(file_name):
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        return get_image_labels(content)


if __name__ == "__main__":
    print(get_labels_from_filename(file_name))

