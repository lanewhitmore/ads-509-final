from nltk.corpus import stopwords
from string import punctuation
from langdetect import detect



sw = stopwords.words("english")
punctuation = set(punctuation)




def clean_tokenize(text, punct_set = punctuation, string_bool = False):

    # check for byte object and decode if true
    if isinstance(text, bytes):
        text = text.decode('utf-8')

    # change text to lower case
    text = str.lower(text)

    # remove punctuations
    text = "".join([ch for ch in text if ch not in punct_set])

    # tokenize
    tokens = text.split()

    # drop stop words
    tokens_cleaned = [token for token in tokens if token not in sw]

    if string_bool:
        tokens_string = ' '.join(tokens_cleaned)
        return tokens_string

    return tokens_cleaned

def detect_language(text):
    if text.strip() == '':
        return 'unknown'
    try:
        return detect(text)
    except:
        return 'unknown'

def sentiment_stats(x_train,x_test, y_train, y_test):
    print ('Size of Training Data ', x_train.shape[0])
    print ('Size of Test Data ', x_test.shape[0])
    print ('Distribution of classes in Training Data :')
    print ('Positive Sentiment ', str(sum(y_train == 1)/ len(y_train) * 100.0))
    print ('Negative Sentiment ', str(sum(y_train == 0)/ len(y_train) * 100.0))
    print ('Distribution of classes in Testing Data :')
    print ('Positive Sentiment ', str(sum(y_test == 1)/ len(y_test) * 100.0))
    print ('Negative Sentiment ', str(sum(y_test == 0)/ len(y_test) * 100.0))