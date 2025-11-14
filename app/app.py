from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import os

# Correct path
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "ukrainian_readability_model.pkl")

# Load model + encoder
with open(MODEL_PATH, "rb") as f:
    model, label_encoder = pickle.load(f)


# Input schema
class Sample(BaseModel):
    words: float
    syllables: float
    sentences: float
    letters: float
    avg_word_len: float
    avg_word_syl: float
    avg_sent_len: float


app = FastAPI(title="Ukrainian Readability API")


@app.get("/")
def root():
    return {"message": "Ukrainian Readability API. Use /docs for UI."}


@app.post("/predict/")
def predict(sample: Sample):
    df = pd.DataFrame([{
        'words': sample.words,
        'syllables': sample.syllables,
        'sentences': sample.sentences,
        'letters': sample.letters,
        'avg_word_len': sample.avg_word_len,
        'avg_word_syl': sample.avg_word_syl,
        'avg_sent_len': sample.avg_sent_len
    }])

    pred_encoded = model.predict(df)
    pred_label = label_encoder.inverse_transform(pred_encoded)[0]
    proba = model.predict_proba(df).max()

    return {
        "prediction": pred_label,
        "confidence": float(proba)
    }