import pickle
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from sklearn.decomposition import LatentDirichletAllocation
import functions.token_functions as tf

# Load fitted count vectorizer
with open('../models/count_vect.pkl', 'rb') as file:
    count = pickle.load(file)
with open('../models/lda_model.pkl', 'rb') as file:
    lda_text_model = pickle.load(file)

app = FastAPI()

templates = Jinja2Templates(directory="templates/")


@app.get("/topicmodel")
def form_start(request: Request):
    Topic0 = {0: [("empty", "empty"), ("empty", "empty"), ("empty", "empty"), ("empty", "empty"), ("empty", "empty"), ("empty", "empty"), ("empty", "empty"), ("empty", "empty"), ("empty", "empty"), ("empty", "empty")]}
    Topic1 = {1: [("empty", "empty"), ("empty", "empty"), ("empty", "empty"), ("empty", "empty"), ("empty", "empty"), ("empty", "empty"), ("empty", "empty"), ("empty", "empty"), ("empty", "empty"), ("empty", "empty")]}
    return templates.TemplateResponse("index.html", context={'request': request, 'Topic0': Topic0[0], 'Topic1': Topic1[1]})


@app.post("/topicmodel")
def topic(request: Request, reviews: str = Form(...)):
    text = [reviews]
    cleaned = text.apply(tf.clean_tokenize)
    text_count = count.transform(cleaned)

    # Make prediction
    lda_text_model.transform(text_count)
    d = {0:[], 1:[]}
    for topic, words in enumerate(lda_text_model.components_):
        total = words.sum()
        largest = words.argsort()[::-1] # invert sort order
        print("\nTopic %02d" % topic)
        for i in range(0, 10):
            d[topic].append((count.get_feature_names_out()[largest[i]], round(abs(words[largest[i]]*100.0/total), 2)))
    return templates.TemplateResponse('index.html', context={'request': request, 'Topic0': d[0], 'Topic1': d[1]})


