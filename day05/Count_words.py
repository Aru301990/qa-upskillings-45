from pygments.lexer import words


def count_words():
    sentence="Hello I am Aruna"
    words=sentence.split()
    count=0
    for word in words:
       count+=1
    print(count)



count_words()