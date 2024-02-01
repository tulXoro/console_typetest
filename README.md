# Description
This is a simple application that mimicks a typing test in most websites. I built this to primarily help children and teens learn about the fundamentals of programming.

# Usage
You may use this project however you see fit.

# How to start
Ensure you have [Python](https://www.python.org/downloads/) installed and optionally use an IDE. If you do not have the right version of Python, you should upgrade/downgrade as necessary.
Clone the repository with `git clone <url>`.
Install the necessary dependencies `pip install .`. 
Run the game with `python3 main.py`. 

# How to play
Keep typing until you finish the sentence.

# How it works
It creates two lists. One list is used to display the sentences with colors, and the other is used as a copy of the original list. The program waits until the user types, and if the character they typed is in the same position that they are currently at, then they will change the highlighted color to green and move the cursor.
