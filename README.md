# tictactoe
name: FATIMAH ZAHRAU WAMBAI
pathway: intro to generative ai (beginner)

i created a tic-tac-toe game where a user can play the game against an AI agent name 'larry the robot'. the ai learns by playing thousands of practice games.

FEATURES
1. ai is built with Q-learning
2. user can enter their name
3. program has the ability to reject input of already chosen squares
4. after game user will be asked if they want to play again

TOOLS USED
IDLE PYTHON 3.12

HOW TO RUN
1. open command prompt and navigate to where file is saved using 'cd'
2. run using: 'python tictactoe.py'

HOW IT WORKS
1. the game board is made up of 9 squares, and the function '_checkwinner()" checks the 8 winning lines in the function_ _winlinrs after each move to see if thier is a winner .
2. The function train() trains the AI by playing thousands of games against a random player, where a win is scored as +1, a draw +0.5, and a loss as -1.
3. the function _humanmove() continuous to ask user to enter a valid square from 1 to 9.
