import re
from collections import Counter

def most_occr_element(word):

    # re.findall will extract all the elements
    # from the string and make a list
    arr = re.findall(r'[0-9]+',word)

    #Store Max Frequency
    maxm = 0

    #Max Elem of Most Frequency
    max_elem = 0

    # counter will store all the number with
    # their frequencies
    # c = counter((55, 2), (2, 1), (3, 1), (4, 1))
    c = Counter(arr)
    key = c.keys()

    for x in list(key):
        if c[x] >= maxm:
            maxm = c[x]
            max_elem = int(x)

    return max_elem


word = 'geek55of55gee4ksabc3dr2x'
print(most_occr_element(word))