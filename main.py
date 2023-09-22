# imports
from readchar import readkey, key
from replit import clear
from termcolor import cprint, colored
from time import time, sleep
from random import randint

with open("sentences.txt", "r") as file:
  lines = file.readlines()

sentences = []
for line in lines:
  sentences.append(line.rstrip())


# get a sentence to be typed
original = list(sentences[randint(0, len(sentences)-1)])
sentence = original.copy()
# player position
cursor = 0

# helper functions
def printSentence():
  print("Current time: ", round(current_time-start_time, 2), "seconds")

  print("Percentage Correct: ", str(calcPercent()) + "%" )
  print("".join(sentence))

def setColor(index, color, flag="on_yellow"):
  sentence[index] = colored(sentence[index], color, flag)

def setCursor():
  global cursor, start_time, correct
  if cursor == 0:
    start_time = time()
    correct = 0
  sentence[cursor] = original[cursor]
  setColor(cursor, "green", "on_green")
  cursor += 1
  if cursor >= len(sentence):
    return 1
  setColor(cursor, "yellow")

  # Used as an "arcade-y" way to check accuracy
  # The player has a chance to improve accuracy for typing correctly
def calcPercent():
  return max(0, round(((sen_len+cursor)-mistakes)/(sen_len+cursor) * 100, 2))

# init cursor
setColor(0, "yellow")

k = -1
val = -1
start_time = 0
current_time = 0

sen_len = len(sentence)
mistakes = 0
correct = 1

while True:
  # handle display
  printSentence()

  # handle key input
  k = colored(readkey(), "yellow", "on_yellow")
  if k == sentence[cursor]:
    val = setCursor()
    correct+=1
  else:
    mistakes += 1
  if cursor != 0:
    current_time = time()
    
  clear()
  
  if val == 1:
    print("Congrats! Final time is:", round(current_time-start_time, 2), "seconds")
    print("Percentage Correct: ", str(calcPercent()) + "%")
    print("Mistakes: ", mistakes, "Correct: ", correct)
    sleep(1)
    print("Press any key to restart...")
    k = readkey()
    # Reset everything
    start_time = 0
    current_time = 0
    original = list(sentences[randint(0, len(sentences)-1)])
    sentence = original.copy()
    cursor = 0
    val = 0
    setColor(0, "yellow")
    mistakes = 0
    sen_len = len(sentence)
    
    clear()
