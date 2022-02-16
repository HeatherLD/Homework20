### Homework20

## mapper.py
/usr/bin/env python
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
    
# reducer.py
#1/usr/bin/env python
import sys
import re

current_word = None
current_w_count = 0
w_count = 0
puncs = None
current_punc = None
current_p_count = 0
p_count = 0
words = None

#take all the words from the mapper and count them

#lines passed from the mapper
for line in sys.stdin:
    line = line.strip()

    word, w_count = line.split("\t", 1)

    w_count = int(w_count)

    #sorted values from command line are passed, and 
    # if we have multiples of the same word, we increment the count
    if current_word == word:
        current_count += count
    
    else:
        #if there is a current word and it's not None
        if current_word:
            print(current_word + "\t" + str(current_w_count))
        
        current_w_count = w_count
        current_word = word

if current_word == word:
    print(current_word + "\t" + str(current_w_count))


#take all the punctuation from the mapper and count each mark

#lines passed from the mapper
for line in sys.stdin:
    line = line.strip()

    punc, p_count = line.split("\t", 1)

    p_count = int(p_count)

    #sorted values from command line are passed, and 
    # if we have multiples of the same mark, we increment the count
    if current_punc == punc:
        current_p_count += p_count
    
    else:
        #if there is a current punctuation mark and it's not None
        if current_punc:
            print(current_punc + "\t" + str(current_p_count))
        
        current_p_count = p_count
        current_punc = punc

if current_punc == punc:
    print(current_punc + "\t" + str(current_p_count))

  
