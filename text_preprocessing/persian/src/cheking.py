
import hazm.normalizer
from nltk.tokenize import word_tokenize
import hazm
import nltk
nltk.download('punkt')

def tokenize_farsi_text(text):
    
    normalizer = hazm.Normalizer()
    text_normalized = normalizer.normalize(text)
    
    tokens = word_tokenize(text_normalized)
    
    return tokens


def decreace_duplicate_letters(tokens):
    normalizer = hazm.Normalizer()

    clean_tokens = []

    for token in tokens:

        cleaned_token = normalizer.decrease_repeated_chars(token)
        clean_tokens.append(cleaned_token)
    
    return clean_tokens


def remove_meaningless_token(tokens, vocabulary_dict):

    meaningfull_tokens = []

    for token in tokens:

        if token in vocabulary_dict.values():

            meaningfull_tokens.append(token) 
            
    return meaningfull_tokens



