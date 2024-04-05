import re


def get_pure_words(list_of_words):
    first_words_list = []

    for tup in list_of_words:

        first_element = tup[0]
        first_words_list.append(first_element)

    return first_words_list


def get_modified_words(pure_word_list):

    clean_words = []
    for word in pure_word_list:

        cleaned_word = re.sub(r'\u200c', '', word)
        clean_words.append(cleaned_word)

    return clean_words


def get_pure_verbs(list_of_verbs):

    verbs_list = []
    for verb in list_of_verbs:

        cleaned_text = re.sub(r'#.*', '', verb)
        verbs_list.append(cleaned_text)

    return verbs_list


def get_modified_verbs(pure_verbs_list):

    clean_verbs = []
    for verb in pure_verbs_list:

        cleaned_verb = re.sub(r'\u200c', '', verb)
        clean_verbs.append(cleaned_verb)

    return clean_verbs