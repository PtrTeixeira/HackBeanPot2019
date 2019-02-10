import time
import requests

# Variables
_region = 'westcentralus'  # region of your subscription
_params = {'visualFeatures': 'Categories, Tags, Description, Faces, ImageType, Color'}
_default_oper = 'analyze'
_root_url = 'https://{}.api.cognitive.microsoft.com/vision/v2.0/'.format(_region)
_key = '719bd8feb67f4b5185f4e18108c71fde'  # primary API key
_maxNumRetries = 10


def process_request(json, data, headers, params, url):
    """
    Parameters:
    json: Used when processing images from its URL. See API Documentation
    data: Used when processing image read from disk. See API Documentation
    headers: Used to pass the key information and the data type request
    """
    retries = 0
    result = None
    is_requesting = True

    while is_requesting:
        response = requests.request('post', url, json=json, data=data, headers=headers, params=params)
        if response.status_code == 429:
            print("Message: %s" % (response.json()))

            if retries <= _maxNumRetries:
                time.sleep(1)
                retries += 1
            else:
                print('Error: failed after retrying!')
                is_requesting = False

        elif response.status_code == 200 or response.status_code == 201:
            if 'content-length' in response.headers and int(response.headers['content-length']) == 0:
                result = None
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str):
                if 'application/json' in response.headers['content-type'].lower():
                    result = response.json() if response.content else None
                elif 'image' in response.headers['content-type'].lower():
                    result = response.content
            is_requesting = False
        else:
            print("Error code: %d" % response.status_code)
            print("Message: %s" % (response.json()))
            is_requesting = False

    return result


def get_image_data(image_url, oper=_default_oper, params=_params):
    # Computer Vision parameters
    # 'post', _url, json = json, data = data, headers = headers, params = params

    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = _key
    headers['Content-Type'] = 'application/json'

    json = {'url': image_url}
    data = None

    request_url = _root_url + oper

    result = process_request(json, data, headers, params, request_url)
    return result


# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fe

urlImage = 'https://scontent-ort2-1.cdninstagram.com/vp/909bbe8b1f2b02d0a3cec614a6eeb349/5CDDF593/t51.2885-15/e35/51014235_482944698906498_4517306961788104271_n.jpg?_nc_ht=scontent-ort2-1.cdninstagram.com'
urlImage2 = 'https://scontent-ort2-1.cdninstagram.com/vp/109bc359aca6f368e83cb032c3d423c0/5CFA4182/t51.2885-15/e35/51126627_154833935510698_1555794752472783237_n.jpg?_nc_ht=scontent-ort2-1.cdninstagram.com'

# this is the JSON for image analysis
image_data = get_image_data(urlImage)
# this is the JSON for image descriptions
image_data2 = get_image_data(urlImage, 'describe', {'maxCandidates': 10, 'language': 'en'})

if __name__ == "__main__":
    for k, v in image_data.items():
        print(str(k) + ": " + str(v))
