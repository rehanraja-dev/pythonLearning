result={
  "statusCode": 200,
  "data": {
    "gender": "female",
    "name": {
      "title": "Mrs",
      "first": "Deveney",
      "last": "Van der Scheer"
    },
    "location": {
      "street": {
        "number": 8754,
        "name": "Katerveerdijk"
      },
      "city": "Schoonebeek",
      "state": "Noord-Holland",
      "country": "Netherlands",
      "postcode": "8029 OJ",
      "coordinates": {
        "latitude": "-16.1449",
        "longitude": "154.5578"
      },
      "timezone": {
        "offset": "+11:00",
        "description": "Magadan, Solomon Islands, New Caledonia"
      }
    },
    "email": "deveney.vanderscheer@example.com",
    "login": {
      "uuid": "76d0c595-05df-4f7c-b642-3c92d83b7daf",
      "username": "reddog277",
      "password": "russian",
      "salt": "XoVanszK",
      "md5": "fa900f8262f009b4b4542d33d8301589",
      "sha1": "71ad9623e47110b5716d1de87cfd250b13804ac8",
      "sha256": "c9b16524c574fa59338bd0912523524cc24a5d0b8f6b409cf2e766f0dcceb3ce"
    },
    "dob": {
      "date": "1953-11-04T20:07:40.042Z",
      "age": 69
    },
    "registered": {
      "date": "2007-01-31T08:14:23.857Z",
      "age": 16
    },
    "phone": "(017) 9412905",
    "cell": "(06) 14596090",
    "id": 444,
    "picture": {
      "large": "https://randomuser.me/api/portraits/women/91.jpg",
      "medium": "https://randomuser.me/api/portraits/med/women/91.jpg",
      "thumbnail": "https://randomuser.me/api/portraits/thumb/women/91.jpg"
    },
    "nat": "NL"
  },
  "message": "Random user fetched successfully",
  "success": True
}
res = result["data"]['name']['first']
print(res)