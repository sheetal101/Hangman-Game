import random
def load_words():
    f=open("words.txt", 'r')
    f1=f.read()
    a=f1.split()
    return a 
def choose_word():
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word
choose_word()
