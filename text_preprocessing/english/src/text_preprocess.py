import nltk
from nltk.text import *
from nltk.corpus import wordnet
from nltk.corpus import words
nltk.download('words')
nltk.download('punkt')
import re
from src.regex import init_repeat_replacer
from spellchecker import SpellChecker

class TextPreprocess:

    def __init__(self):
        self.repeat_regexp, self.repl = init_repeat_replacer()
        self.meaningful_words = set(words.words())
        self.spell = SpellChecker()  # Initializing SpellChecker
        
    def replace_repeated_characters(self, word):
        if wordnet.synsets(word):
            return word
        
        repl_word = self.repeat_regexp.sub(self.repl, word)
        if repl_word != word:
            return self.replace_repeated_characters(repl_word)
        else:
            return repl_word
        

    def remove_meaningless_words(self, text):
        tokens = nltk.word_tokenize(text.lower())
        cleaned_tokens = [word for word in tokens if word in self.meaningful_words]
        cleaned_text = ' '.join(cleaned_tokens)
        return cleaned_text
    

    def correct_spellings(self, text):
        corrected_text = []
        misspelled_words = self.spell.unknown(text.split())
        for word in text.split():
            if word in misspelled_words:
                corrected_text.append(self.spell.correction(word))
            else:
                corrected_text.append(word)
        return " ".join(corrected_text)