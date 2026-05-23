"""
Author: Eliana Mugar
Date: 2/10/2021 
"""

#requires download of nltk in python
import os
import nltk
from nltk.corpus import *
import string

def main():
    # prints all corpora in NLTK
    print("\nHere are the corpora built into nltk:")
    for h in os.listdir(nltk.data.find("corpora")):
        if '.zip' not in h:
            print(h)
    print()

    # stores user's corpus choice
    chosen_corpus = input("Enter corpus name (copy the name EXACTLY as listed): ")
    function_string = "nltk.corpus." + chosen_corpus + ".fileids()"

    # shows all files within user's corpus choice
    print("\nHere are the options from", chosen_corpus + ": \n")
    for corpus in eval(function_string):
        print(str(corpus))
    print()

    # tags all words with corresponding part-of-speech in user's text file choice
    text_function = chosen_corpus + ".raw(str(input('Enter text file name (with .txt): ')))"
    text = eval(text_function)
    tokens = nltk.word_tokenize(text)
    tagged_corpus = nltk.pos_tag(tokens)
    update_corpora = ""

    # variables for adjective searching loop
    consecutive = False
    curr_consecutive_adjs = []
    consecutive_start = None
    consecutive_end = None
    punctuations = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''

    # checks each word tagged in the corpus
    for i in range(len(tagged_corpus)):
        # begin search for minimum 2 consecutive adjectives
        # searches for unlimited maximum consecutive adjectives
        if 'JJ' in tagged_corpus[i] and "such" not in tagged_corpus[i]: 
            # not looking for consecutive adjectives now, but want to start
            if not consecutive: 
              consecutive = True
              consecutive_start = i
            curr_consecutive_adjs.append(tagged_corpus[i][0])
        # checks if the "word" is actually a punctuation
        elif tagged_corpus[i][0] in punctuations:
          continue
        # reached the end of your adjectives
        else:
          if consecutive:
            consecutive = False
            consecutive_end = i - 1
            if len(curr_consecutive_adjs) > 1:
                # prints context BEFORE consecutive adjective string
              for j in range(consecutive_start - 6, consecutive_start):
                update_corpora += str(tagged_corpus[j][0]) + " "
              update_corpora += "["
              for x in range(len(curr_consecutive_adjs) - 1):
                update_corpora += curr_consecutive_adjs[x] + " "
              update_corpora += curr_consecutive_adjs[len(curr_consecutive_adjs)-1] + "]"
                # prints context AFTER consecutive adjective string
              for y in range(consecutive_end + 1, consecutive_end + 7):
                update_corpora += " " + str(tagged_corpus[y][0])
              update_corpora += "\n"
              update_corpora += "\n"
            # clears consecutive adjectives list to prep for the new iteration
            curr_consecutive_adjs = []

    # stores user's filename choice
    user_f = str(input("Enter filename for which you want the data text to be exported (with .txt): \n"))

    # opens user's file
    file = open(user_f, "r")
    counter = 0

    # reads user's file
    content = file.read()
    co_list = content.split("\n")

    # exports line count at the START of user's file
    for index in co_list:
        if index:
            counter += 1
    f = open(file, "w")
    f.write(str(counter - 1) + " lines" + "\n" + "\n")

    # exports data to a text file of user's choice of filename
    f.write(update_corpora)

    

# user input choice to run, re-run, or stop the program
while True:
    answer = input("Run the program? (y/n): ")
    if answer not in ('y', 'n'):
        print("Invalid input.")
        break
    if answer == 'y':
        main()
    else:
        print("Goodbye.")
        break

# test code
"""
text = "She had been a friend and companion such as few possessed: intelligent, \
well-informed, useful, gentle, knowing all the ways of the family, \
interested in all its concerns, and peculiarly interested in herself, \
in every pleasure, every scheme of hers--one to whom she could speak \
every thought as it arose, and who had such an affection for her \
as could never find fault."

tokenss = nltk.word_tokenize(text)
tagged_text = nltk.pos_tag(tokenss)
print(tagged_text)
"""

