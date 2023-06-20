from nltk.corpus import stopwords
from string import punctuation
from langdetect import detect
from collections import Counter
from lexical_diversity import lex_div as ld

sw = stopwords.words("english")
punctuation = set(punctuation)


def clean_tokenize(text, punct_set=punctuation, string_bool=False):
    """

    :param text:
    :param punct_set:
    :param string_bool:
    :return:
    """

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


def get_char_count(list_text):
    """
    # created function to get character count for each token
    :param list_text:
    :return:
    """
    i = 0
    count = 0
    while i < len(list_text):
        for _ in list_text[i]:
            count += 1
        i += 1
    return count


def descriptive_stats(tokens, freq_num=5, verbose=True):
    """
        Given a list of tokens, print number of tokens, number of unique tokens,
        number of characters, lexical diversity (https://en.wikipedia.org/wiki/Lexical_diversity),
        and num_tokens most common tokens. Return a list with the number of tokens, number
        of unique tokens, lexical diversity, and number of characters.

    """

    # Fill in the correct values here.
    num_tokens = len(tokens)
    num_unique_tokens = len(list(dict.fromkeys(tokens)))
    lexical_diversity = round(ld.ttr(tokens), 2)
    num_characters = get_char_count(tokens)

    if verbose:
        print(f"There are {num_tokens} tokens in the data.")
        print(f"There are {num_unique_tokens} unique tokens in the data.")
        print(f"There are {num_characters} characters in the data.")
        print(f"The lexical diversity is {lexical_diversity:.3f} in the data.")

        # print the five most common tokens
        print(Counter(tokens).most_common(freq_num))

    return ([num_tokens, num_unique_tokens,
             lexical_diversity,
             num_characters])


def detect_language(text):
    if text.strip() == '':
        return 'unknown'
    try:
        return detect(text)
    except:
        return 'unknown'


def sentiment_stats(x_train, x_test, y_train, y_test):
    print('Size of Training Data ', x_train.shape[0])
    print('Size of Test Data ', x_test.shape[0])
    print('Distribution of classes in Training Data :')
    print('Positive Sentiment ', str(sum(y_train == 1) / len(y_train) * 100.0))
    print('Negative Sentiment ', str(sum(y_train == 0) / len(y_train) * 100.0))
    print('Distribution of classes in Testing Data :')
    print('Positive Sentiment ', str(sum(y_test == 1) / len(y_test) * 100.0))
    print('Negative Sentiment ', str(sum(y_test == 0) / len(y_test) * 100.0))


def get_tokens(text, tokenizer, max_seq_length, add_special_tokens=True):
    input_ids = tokenizer.encode(text,
                                 add_special_tokens=add_special_tokens,
                                 max_length=max_seq_length,
                                 pad_to_max_length=True)
    attention_mask = [int(id > 0) for id in input_ids]
    assert len(input_ids) == max_seq_length
    assert len(attention_mask) == max_seq_length
    return input_ids, attention_mask