### Homework20

#1/usr/bin/env python
import sys
import re

#initialize lists

puncs = []

words = []

flat_list_p = []

flat_list_w = []

#stdin = standard input
for line in sys.stdin:

    #strip white spaces at beginning and end of line
    line = line.strip()

    #split each line up into word or punctuation chunks
    #copy punctuation to a new list
    #add words to a list and allowing the punctuation to drop out
    puncs.append(re.findall("[^a-zA-Z0-9\s]", line))
    words.append(re.split("[^a-zA-Z0-9]", line))

    #function to make sure the "puncs" list is 1D
    for punc in puncs:
        if type(punc) is list:
            # If the element is of type list, iterate through the sublist
            for item in punc:
                flat_list_p.append(item)
        else:
            flat_list_p.append(punc)
    
    #reassign flattened list to original list
    puncs = flat_list_p
    
    #function to make sure the "words" list is 1D
    for word in words:
        if type(word) is list:
            # If the element is of type list, iterate through the sublist
            for item in word:
                flat_list_w.append(item)
        else:
            flat_list_w.append(word)

    #reassign flattened list to original list
    words = flat_list_w

    #process each punctuation mark and assign it a value of 1
    for punc in puncs:
        print(punc + "\t1")
 
    #process each word and assign a value of 1 to each word
    for word in words:
        if word != "":
            print(word + "\t1")
    


  
