from fastapi import FastAPI
from textblob import TextBlob
from pydantic import BaseModel

app = FastAPI()


class ReqBody(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {"message": "Welcome to sentiment analysis open API"}


@app.post("/analysis/")
async def text_analysis(req: ReqBody):
    blob = TextBlob(req .text)
    return {
        "text": req.text,
        "sentiment": {
            "subjectivity": blob.sentiment.subjectivity,
            "polarity": blob.sentiment.polarity,
        },
        "words": blob.words,
        "sentences": blob.sentences,
        "corrected": blob.correct()
    }
