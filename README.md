# tic-tac-toe-ai

Using the **Minimax algorithm**, **I implemented an AI to play Tic-Tac-Toe optimally**.

Starter code was provided for this project, which I completed in the context of Harvard UniversityX's [CS50 Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/) course. 

There are two main files in this project: 
- *runner.py*, which contains all of the code to run the graphical interface for the game.
- *tictactoe.py*, which contains all of the logic for playing the game.

The tic tac toe board is represented as a list of three lists (representing the three rows of the board), where each internal list contains three values that are either X, O, or EMPTY. 

## Implementation
I implemented the following functions in *tictactoe.py*:
- *player*, 
- *actions*, 
- *result*, 
- *winner*, 
- *terminal*, 
- *utility*, and 
- *minimax*
functions.

## Specification
Run **python runner.py** to play against the AI. Since Tic-Tac-Toe is a tie given optimal play by both sides, you should never be able to beat the AI (though if you don’t play optimally as well, it may beat you!)

Visit the [Harvard CS50AI](https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/) for more information about the specifications for the project. Please **do not** directly use the source code as it is **only** for reference. Plagiarism is strictly prohibited by both Harvard University and the edX platform. See [academic honesty](https://cs50.harvard.edu/ai/2020/honesty/) for details.

## About Minimax
A type of algorithm in adversarial search, Minimax represents winning conditions as (-1) for one side and (+1) for the other side. Further actions will be driven by these conditions, with the minimizing side trying to get the lowest score, and the maximizer trying to get the highest score. 

Recursively, the algorithm simulates all possible games that can take place beginning at the current state and until a terminal state is reached. Each terminal state is valued as either (-1), 0, or (+1).

Knowing based on the state whose turn it is, the algorithm can know whether the current player, when playing optimally, will pick the action that leads to a state with a lower or a higher value. This way, alternating between minimizing and maximizing, the algorithm creates values for the state that would result from each possible action. 
