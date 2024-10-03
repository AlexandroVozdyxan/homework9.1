def popular_words(text, words):
    text_lower = text.lower()
    words_list = text_lower.split()

    words_count = {}

    for i in words:
        words_count[i] = words_list.count(i)

    return words_count

text = '''When I was One I had just begun When I was Two I was nearly new'''
words = ['i', 'was', 'three', 'near']
print(popular_words(text, words))