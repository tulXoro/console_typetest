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
  print("Current time: ", current_time-start_time)
  print("".join(sentence))

def setColor(index, color, flag="on_yellow"):
  sentence[index] = colored(sentence[index], color, flag)

def setCursor():
  global cursor, start_time
  if cursor == 0:
    start_time = time()
  sentence[cursor] = original[cursor]
  setColor(cursor, "green", "on_green")
  cursor += 1
  if cursor >= len(sentence):
    return 1
  setColor(cursor, "yellow")

# init cursor
setColor(0, "yellow")

k = -1
val = -1
start_time = 0
current_time = 0
while True:
  # handle display
  printSentence()

  # handle key input
  k = colored(readkey(), "yellow", "on_yellow")
  if k == sentence[cursor]:
    val = setCursor()

  if cursor != 0:
    current_time = time()
    
  clear()
  
  if val == 1:
    print("Congrats! Final time is:", current_time-start_time)
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
    
    clear()
