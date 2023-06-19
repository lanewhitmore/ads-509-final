import pickle
from fastapi import FastAPI
from pydantic import BaseModel


# Load fitted tfid vectorizer
with open('../models/tfidf.pkl', 'rb') as file:
    tfidf = pickle.load(file)

# Load the pickled NLP model
with open('../models/svc_model.pkl', 'rb') as file:
    svc_model = pickle.load(file)

app = FastAPI()


class TextInput(BaseModel):
    text: str

@app.post("/classifier")
def classify_text(input_data: TextInput):
    text = [input_data.text]
    text_tfidf = tfidf.transform(text)


    # Make prediction
    prediction = svc_model.predict(text_tfidf)

    # Return the prediction as the API response

    if prediction[0]:
        return {"The review provided is considered a good review!"}

    return {"The review provided is considered a bad review!"}
