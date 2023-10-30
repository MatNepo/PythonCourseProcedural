def get_sentences_list(list_):
    sentences = list_.split(".")
    strip_sentence = [sentence.strip() for sentence in sentences if sentence.strip()]
    return strip_sentence


print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
