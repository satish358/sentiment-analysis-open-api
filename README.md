# Sentiment analysis open api

## Setup

First install required modules

- FastAPI
- TextBlob
- BaseModel

## Run API

to the application you need to type `uvicorn main:app --reload`

## Access api

Api will start on http://127.0.0.1:8000 </br>
You need to make post request like below
http://127.0.0.1:8000/analysis

- Request Body

```
{
    "text": "Your verry good"
}
```

- Response Body

```
{
    "text": "Your verry good",
    "sentiment": {
        "subjectivity": 0.6000000000000001,
        "polarity": 0.7
    },
    "words": [
        "Your",
        "verry",
        "good"
    ],
    "sentences": [
        {
            "raw": "Your verry good",
            "string": "Your verry good",
            "stripped": "your verry good",
            "tokenizer": {},
            "np_extractor": {
                "_trained": false
            },
            "pos_tagger": {},
            "analyzer": {
                "_trained": false
            },
            "parser": {},
            "classifier": null,
            "start": 0,
            "start_index": 0,
            "end": 15,
            "end_index": 15
        }
    ],
    "corrected": {
        "raw": "Your very good",
        "string": "Your very good",
        "stripped": "your very good",
        "tokenizer": {},
        "np_extractor": {
            "_trained": false
        },
        "pos_tagger": {},
        "analyzer": {
            "_trained": false
        },
        "parser": {},
        "classifier": null
    }
}
```
