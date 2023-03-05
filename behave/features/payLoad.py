import json


def addPetPayload(petName, petId):
    body = {
    "id": petId,
    "category": {
        "id": 1,
        "name": "cats"
    },
    "name": petName,
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
        "id": 13,
        "name": "troublemaker"
        }
    ],
    "status": "available"
    }
    return body


def addImagePayload():
    file = {'file': open('utilities/petImg.jpg', 'rb')}
    return file
