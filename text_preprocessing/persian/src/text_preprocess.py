from src.extract import extract_words, extract_verbs
from src.edit import get_pure_verbs, get_pure_words, get_modified_words, get_modified_verbs
from src.adding import adding_two_list
from src.convert import convert2dict
from src.cheking import tokenize_farsi_text, remove_meaningless_token, decreace_duplicate_letters




class textPreprocess:

    def __init__(self, text):
        
        self.text = text

    def reduce_duplicate_characters(self):
        
        tokens = tokenize_farsi_text(self.text)
        decreace_letters = decreace_duplicate_letters(tokens)

        return decreace_letters


    def remove_non_informative_words(self):
        
        words = extract_words()
        verbs = extract_verbs()

        pure_words = get_pure_words(words)
        pure_verbs = get_pure_verbs(verbs)

        clean_words = get_modified_words(pure_words)
        clean_verbs = get_modified_verbs(pure_verbs)


        vocabulary_list = adding_two_list(clean_words, clean_verbs)
        vocabulary_dict = convert2dict(vocabulary_list)


        tokens = tokenize_farsi_text(self.text)

        remove_undefined_tokens = remove_meaningless_token(tokens, vocabulary_dict)

        return remove_undefined_tokens
    
    def correct_speling_words(self):
        pass

    def convert_letter_to_digit(self):
        
        pass