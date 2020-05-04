# put your code here.
import sys

def count_words(phrase):

    file = open(sys.argv[1])

    word_count = {}

    for line in file:
        lines = line.rstrip('\r\n').split(' ')

        for word in lines:
            word_count[word] = word_count.get(word, 0) + 1

    for word, num in word_count.items():
        print(f'{word} {num}')

count_words(sys.argv)