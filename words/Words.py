try:
    JUNIOR_WORDS = set(map(str.rstrip, open("words/junior_words.txt", encoding='utf-8').readlines()))
except FileNotFoundError:
    print('junior_words.txt not found')

try:
    MIDDLE_WORDS = set(map(str.rstrip, open("words/middle_words.txt", encoding='utf-8').readlines()))
except FileNotFoundError:
    print('middle_words.txt not found')

try:
    SENIOR_WORDS = set(map(str.rstrip, open("words/senior_words.txt", encoding='utf-8').readlines()))
except FileNotFoundError:
    print('senior_words.txt not found')

try:
    VERBAL_WORDS = set(map(str.rstrip, open("words/verbal_words.txt", encoding='utf-8').readlines()))
except FileNotFoundError:
    print('verbal_words.txt not found')
