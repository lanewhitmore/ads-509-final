import pickle
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

from sklearn.decomposition import LatentDirichletAllocation

# Load fitted count vectorizer
with open('C:/Users/whitm/Documents/GitHub/ads-509-final/models/count_vect.pkl', 'rb') as file:
    count = pickle.load(file)
#with open('C:/Users/whitm/Documents/GitHub/ads-509-final/models/lda_model.pkl', 'rb') as file:
    #lda_text_model = pickle.load(file)
lda_text_model = LatentDirichletAllocation(n_components=2, random_state=33)

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
    text_count = count.transform(text)

    # Make prediction
    lda_text_model.fit_transform(text_count)
    d = {0:[], 1:[]}
    for topic, words in enumerate(lda_text_model.components_):
        total = words.sum()
        largest = words.argsort()[::-1] # invert sort order
        print("\nTopic %02d" % topic)
        for i in range(0, 10):
            d[topic].append((count.get_feature_names_out()[largest[i]], round(abs(words[largest[i]]*100.0/total), 2)))
    #lda_display = pyLDAvis.lda_model.prepare(lda_text_model, text_count, count, sort_topics=False) 
    return templates.TemplateResponse('index.html', context={'request': request, 'Topic0': d[0], 'Topic1': d[1]})


