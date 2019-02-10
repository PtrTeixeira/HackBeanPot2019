
import json
from urllib.parse import urlparse
import os
from computervision import get_image_data
from sentence_formatter import format_sentence_dict

def get_meta_data(post_data, post_num):
    """Takes in a Python obj? of and returns a dicitonary (media_entry) of the username,
    timestamp, image_url, and caption associated with an Instagram post. It also
    contains a description of the image(s) generated using the Microsoft Computer
    Vision API"""

    # gets username and timestamp of post
    media_entry = {"username": str(post_data[post_num]["username"]), "timestamp": post_data[post_num]["taken_at_timestamp"]}

    # gets urls of image/video
    images = post_data[post_num]["urls"]

    #deals with encoding
    new_images =[]
    for image in images:
        new_image = str(image)
        new_images.append(new_image)
    media_entry.update({"image_url": new_images})

    # storing if url is video or not
    media_entry.update({"is_video": []})
    for url in media_entry["image_url"]:
        path = urlparse(url).path
        ext = os.path.splitext(path)[1]
        if ext == ".jpg":
            media_entry["is_video"].append(False)
        elif ext == ".mp4":
            media_entry["is_video"].append(True)
        else:
            media_entry["is_video"].append(None)

    # gets caption if it exists
    if post_data[post_num]["edge_media_to_caption"]:
        media_entry.update({"caption": post_data[post_num]["edge_media_to_caption"]["edges"][0]["node"]["text"]})
        # catches emojis
        try:
            str(media_entry["caption"])
        except:
            media_entry.update({"caption": None})

    # gets location name if available
    if post_data[post_num]["location"]:
        media_entry.update({"location": str(post_data[post_num]["location"]["name"])})
    else:
        media_entry.update({"location": None})


    descriptions = []
    # gets API generated descriptions for images
    for i in range(0, len(media_entry["image_url"])):
        if media_entry["is_video"][i] is False:
            result = get_image_data(media_entry["image_url"][i])
            if len(result["description"]["captions"]) > 0:
                descriptions.append(str(result["description"]["captions"][0]["text"]))
            else:
                descriptions.append(None)
        else:
            descriptions.append(None)

    # adds API-generated descriptions to dicitionary
    media_entry.update({"descriptions": descriptions})

    return media_entry

def get_all_media(json_dir):
    all_media = []

    for filename in os.listdir(json_dir):
        if filename.endswith(".json"): 
            media_list = get_media_list(os.path.join(json_dir, filename))
            all_media.extend(media_list)

    return all_media
  

def get_media_list(file_name):
    """Takes in a json file and returns a list of dictionaries containing a
    customized description of an Instagram post as the key and a list of urls
    as the value"""
    media_list = []

    with open(file_name, "r") as output_file:
        post_data = json.load(output_file)
    # loops through each post in a single user's feed, generates a media-entry dictionary that
    for i in range(len(post_data)):
        raw_entry = get_meta_data(post_data, i)

        generated_text = format_sentence_dict(raw_entry)
        media_list.append({"text": str(generated_text), "urls": raw_entry["image_url"], "is_video": raw_entry["is_video"]})
    

    return media_list


