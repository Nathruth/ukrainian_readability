import pickle
import pandas as pd

with open("../model/ukrainian_readability_model.pkl", "rb") as f:
    model, le = pickle.load(f)

sample = {
    'words': [300],
    'sentences': [8],
    'letters': [580],
    'avg_word_len': [10],
    'avg_sent_len': [35.0],
    'syllables': [8],
    'avg_word_syl': [35.0],

}

df = pd.DataFrame(sample)


pred = model.predict(df)
label = le.inverse_transform(pred)

print(f"Predicted Level: {label[0]}")