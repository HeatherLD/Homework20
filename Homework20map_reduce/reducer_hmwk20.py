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
word = None

#goal: take all the words from the mapper and count them

#lines passed from the mapper
for line in sys.stdin:
    line = line.strip()

    word, w_count = line.split("\t", 1)
   
    w_count = int(w_count)

    #sorted values from command line are passed, and 
    # if we have multiples of the same word, we increment the count
    if current_word == word:
        current_w_count += w_count
    
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
    # if we have multiples of the same word, we increment the count
    if current_punc == punc:
        current_p_count += p_count
    
    else:
        #if there is a current word and it's not None
        if current_punc:
            print(current_punc + "\t" + str(current_p_count))
        
            current_p_count = p_count
            current_punc = punc

if current_punc == punc:
    print(current_punc + "\t" + str(current_p_count))
