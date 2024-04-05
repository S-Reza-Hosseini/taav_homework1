from src.text_preprocess import textPreprocess


text = "این یک متن نمونه فارسیییییی است."
textPreprocessor = textPreprocess(text)
delete_und_text = textPreprocessor.remove_non_informative_words()

reduce = textPreprocessor.reduce_duplicate_characters()
print(reduce)

