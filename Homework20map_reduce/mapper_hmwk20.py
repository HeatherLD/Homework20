#1/usr/bin/env python
import sys
import re

puncs = []
words = []
flat_list_p = []
flat_list_w = []

#goal: break up words into units

#stdin = standard input
for line in sys.stdin:

    #strip white spaces at beginning and end of line
    line = line.strip()

    #split each line up into separate items and sort them into lists
    puncs.append(re.findall("[^a-zA-Z0-9\s]", line))
    words.append(re.split("[^a-zA-Z]", line))

    #punctuation
    for punc in puncs:
        if type(punc) is list:
            # If the element is of type list, iterate through the sublist
            for item in punc:
                flat_list_p.append(item)
        else:
            flat_list_p.append(punc)
    
    puncs = flat_list_p

    #words
    for word in words:
        if type(word) is list:
            # If the element is of type list, iterate through the sublist
            for item in word:
                flat_list_w.append(item)
        else:
            flat_list_w.append(word)

    words = flat_list_w

    #split each word into itself and surrounding punc
    #for word in words:
    #    print(word + "\t" + 1)
 
    #process each word and assign a value of 1 to each word
    for word in words:
        if word != "":
            print(word + "  1")
    



  