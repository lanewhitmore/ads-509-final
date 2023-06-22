import pickle
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Union
from sklearn.decomposition import LatentDirichletAllocation
import functions.token_functions as tf

# Load fitted tfid vectorizer
with open('models/tfidf.pkl', 'rb') as file:
    tfidf = pickle.load(file)

# Load the pickled NLP model
with open('models/svc_model.pkl', 'rb') as file:
    svc_model = pickle.load(file)

# Load fitted count vectorizer
with open('models/count_vect.pkl', 'rb') as file:
    count = pickle.load(file)
lda_text_model = LatentDirichletAllocation(n_components=2, random_state=33)


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates/")


@app.get("/")
async def reviews_form(request: Request):

    return templates.TemplateResponse("index.html", {
        "request": request,
        "review_sentiments": []
    })


@app.post("/reviews")
async def analyze_reviews(request: Request, reviews: Union[str, List[str]] = Form(...)):
    if isinstance(reviews, str):
        review_list = reviews.split('---')
    else:
        review_list = reviews

    review_sentiments = []
    for review in review_list:
        review = review.strip()
        if review:
            sentiment = classify_text(review)
            if sentiment == 1:
                review_sentiments.append((review, "This is considered a good review"))
            else:
                review_sentiments.append((review, "This is considered a bad review"))

    cleaned_reviews = list()
    for review in review_list:
        cleaned_review = tf.clean_tokenize(review)
        cleaned_reviews.append(cleaned_review)

    cleaned_reviews_flat = [item for sublist in cleaned_reviews for item in sublist]
    text_count = count.transform(cleaned_reviews_flat)

    # Make prediction
    lda_text_model.fit_transform(text_count)
    topic_results = {0: [], 1: []}
    for topic, words in enumerate(lda_text_model.components_):
        total = words.sum()
        largest = words.argsort()[::-1]  # invert sort order
        print("\nTopic %02d" % topic)
        for i in range(0, 10):
            topic_results[topic].append(
                (count.get_feature_names_out()[largest[i]], round(abs(words[largest[i]] * 100.0 / total), 2)))

    return templates.TemplateResponse(
        'index.html',
        context={
            'request': request,
            'review_sentiments': review_sentiments,
            'Topic0': topic_results[0],
            'Topic1': topic_results[1]
        })


def classify_text(review_text):
    text_tfidf = tfidf.transform([review_text])
    # Make prediction
    prediction = svc_model.predict(text_tfidf)
    # Return the prediction as the API response
    return prediction
