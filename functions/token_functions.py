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
