## Homework20

### Using mapper.py and reducer.py

Step 1:

• Make sure the mapper.py and reducer.py files are together in a folder called "map_reduce", and that the text file you want to 
analyze is in the same folder as the "map_reduce" folder.

![map_reduce1](https://user-images.githubusercontent.com/91164907/154785485-51a76095-6f80-4c85-986e-ecaf3b533c8f.jpg)

Step 2:

• Enter the following line of code into your Gitbash (Windows) or Terminal (Mac):

cat ../cats.txt|Python3 ./mapper.py| sort|Python3 ./reducer.py

![map_reduce2](https://user-images.githubusercontent.com/91164907/154785486-d40b6e89-a411-4495-b76d-2ec34fb92622.jpg)


### Connections to Natural Language Processing
I think performing this kind of programming helps us imagine how libraries like NLTK and SpaCy work "under the hood" -- it definitely helps us appreciate their abilities!
