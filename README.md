# TicTacToe
Terminal based two-player (or randomized) tic-tac-toe

This program aims to implement a game of tic-tac-toe in python. The user will 
play against the computer.Turn by turn, the user and the computer get a chance
 to fill in a 3x3 grid with their markers (either X or O), until either the player 
 wins by obtaining 3 adjacent markers (horizontally/vertically/diagonally) or a 
 tie occurs if the previous condition is not fulfilled.
 
At the beginning, the user is prompted to enter an username, which is used to 
keep track of the results of the games played (in a seperate csv file), which 
is then updated and displayed at the end of every game (history of wins and 
losses). The player with the 'X' will start each game, and the user is given
the opportunity to choose their marker (which also decides if they play first or not).
If the player chooses a marker which is not 'x' or 'o' (upper and lower case 
are both accepted), they will be prompted to choose again. In order to fill in a cell 
on the grid, the user is prompted to enter the index of the cell (integers 
between 0-8 only). If the cell is occupied, the user will be prompted to enter again.
