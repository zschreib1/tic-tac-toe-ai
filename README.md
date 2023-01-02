# tic-tac-toe-ai

Using the *Minimax* algorithm, *I implemented an AI to play Tic-Tac-Toe optimally*.

Starter code was provided for this project, which I completed in the context of Harvard UniversityX's [CS50 Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/) course. 

There are two main files in this project: 
- *runner.py*, which contains all of the code to run the graphical interface for the game.
- *tictactoe.py*, which contains all of the logic for playing the game.

The tic tac toe board is represented as a list of three lists (representing the three rows of the board), where each internal list contains three values that are either X, O, or EMPTY. 

## IMPLEMENTATION
I implemented the following functions in *tictactoe.py*:
- *player, 
- *actions*, 
- *result*, 
- *winner*, 
- *terminal*, 
- *utility*, and 
- *minimax*
functions.

## SPECIFICATION
Run **python runner.py** to play against the AI. Since Tic-Tac-Toe is a tie given optimal play by both sides, you should never be able to beat the AI (though if you don’t play optimally as well, it may beat you!)

Visit the [Harvard CS50AI](https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/) for more information about the specifications for the project.
