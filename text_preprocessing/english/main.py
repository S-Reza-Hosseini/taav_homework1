from src.text_preprocess import TextPreprocess

main_object = TextPreprocess()

text = ""
repeat_word = main_object.replace_repeated_characters(text)
print(repeat_word)

meaningless_words = main_object.remove_meaningless_words(text)
print(meaningless_words)

correct_speling = main_object.correct_spellings(text)
print(correct_speling)