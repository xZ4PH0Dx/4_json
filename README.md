# Prettify JSON

This program will pretty print your flat json file.

# Quickstart

You should pass a file path as an argument.
If you don't have a json file you can download it from [DEVMAN.org](https://devman.org/fshare/1502828617/1/)

Example of script launch on Linux, Python 3.5:

```bash

$ python3 pprint_json.py ~/alco_shops.json
{
    "features": [
        {
            "geometry": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
...
                "DatasetId": 1854,
                "ReleaseNumber": 2,
                "RowId": "4af7d0bb-be94-40fa-aaaa-b32ebdddc967",
                "VersionNumber": 1
            },
            "type": "Feature"
        }
    ],
    "type": "FeatureCollection"
}


```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
