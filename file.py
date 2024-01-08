
#Create a Python file named Midterm-Q2.py

#*** You must write a comment for every chunk of code you write from now on along with your author tag***


import time 
from urllib.request import urlopen 
import random 
import os 

print ("hello")

word = ""
while len(word) < 3 or len(word)> 7:
    # You get random word 
    txt = urlopen("https://www.mit.edu/~ecprice/wordlist.10000").read()
    WORDS = txt.spilitlines()
    word = str(random.choice(WORDS))

    word =list(word)
    del(word(0))
    del(word(0))
    del(word[len(word)-1])
    word = "".join(word)


# U gotta wait 
def say(words):
    time.sleep(0.6)
    print(words)


 
def welcome(state):
 #Welcome appears
    if state == 0:
        print ("")
        print ("")
        print ("")
    elif state == 1:
        print ("O")
        print ("")
        print ("")
    elif state == 2:
        print ("O")
        print ("|")
        print ("")
    elif state == 3:
        print ("O")
        print ("/|")
        print ("")
    elif state == 4:
        print ("o")
        print ("/|\ ")
        print ("")
    elif state == 5:
        print ("o")
        print ("/|\ ")
        print ("/")
    elif state == 5:
        print ("o")
        print ("/|\ ")
        print ("/\ ")

# U gotta wait 
def say(words):
    time.sleep(0.6)
    print(words)

state = 6
guess = []
wl = list.(word)
for x in wl
    guess += "_"
attempt = []

while "_" in guess and state >= 1:
    say("words are here")
    say(guess)
    say("and the man hanging look like")
    say (state)
    say(" you have already tried these leter")
    say(attempt )

letter = imput()[0]
attempt += letter
for x in range(len(wl)):
    if letter == wl[x]:
        guess[x] = letter
if letter not in wl:
    state -= 1 
say("it doent work ")    
attempt.sort 






      
  

 
