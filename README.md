# 4701 AI Practicum

Welcome to the Practicum Repo for the Fall 2021 AI 4701 Course. Authored by Yoona Chang, Junho Kim-Lee and Ashley Park.

This repo contains an AI checkers program that supports player v player, player v computer and computer v computer game modes. The computer can utilize either a minimax algorithm with customizable depth or a different minimax algorithm with custom-buitl heuristics, designed to make it smarter with less computational time.

### How to Play

Run `make install` to install requirements.


Run `python3 main.py` to play the game. This command requires 2 input args and optionally 5 additional input args. For example, both commands are valid:

`python3 main.py a b`

`python3 main.py a b c d e f g`

##### Explanation of input args

* `a` can be any int between 0 and 19. This arg determines the type of player controlling the red pieces. 0 indicates that red will be a human player. Any int between 1 and 9 inclusive indicates that red will be a computer player utilizing the base minimax algorithm with a depth of `a`. Any int between 10 and 19 inclusive indicates that red will be a computer play utilizing the minimax algorithm with custom heuristics at a depth equal to the second digit of `a`. So, a value of `a`=14 will represent the minimax algorithm with custom heuristics at a depth of 4.
* `b` can be any int between 0 and 19. This arg determines the type of player controlling the white pieces. The input arg is interpreted the same as `a` but for white.
* `c` can be any int. This arg determines how the king advantage factor is weighted in the board evaluation for the custom heuristic minimax algorithm. The formula for converting `c` to a weight is `c`/4. That means that if `c`=3, then the king advantage factor is multiplied by 3/4.
* `d` can be any int. This is the same as for `c` but it weights the move advantage factor.
* `e` can be any int. This is the same as for `c` but it weights the board control factor.
* `f` can be any int. This is the same as for `c` but it weights the vulnerability factor.
* `g` can be any int. This is the same as for `c` but it weights the home row control factor.

##### Custom heuristic information

The base heuristic takes into account the following factors when evaluating the board state:

* Piece advantage - how many pieces each player has
* King advantage - how many kings each player has

---

The custom heuristic additionally takes into account the following factors:

* Move advantage - how many valid moves are available to each player
* Board control - how many squares are in range of each player's pieces
* Vulnerability - how many of each player's pieces are presently vulnerable to capture on the next move
* Home row control - how many squares on each player's home row are occupied by that player's piece


### Other commands

Run `make zip` to zip the program.

`depth_experimenter.sh` is a program that simulates games at different depth values and heuristic parameters. It outputs the results to a CSV called `output.csv`. To run the test file, enter the `test` directory and run `./depth_experimenter.sh`. The output file contains rows of data. Each row possesses 7 values. In order, they represent:

1. Red depth
2. Red heuristic #
3. White depth
4. White heuristic #
5. Number of red wins
6. Number of white wins
7. Number of draws.

`parameter_finder.sh` is used to calculate optimal tuning parameters for the AI minimax algorithm with custom heuristics. To run the test file, enter the `test` directory and run `./parameter_finder.sh`. The `output.csv` file it produces contains rows where each row corresponds to the 5 heuristic parameters in order followed by an integer score that represents how successful those parameter weights were. The last line repeats the row of data that contains the highest score. The 5 heuristic parameters in order are the last 5 parameters listed above, in that order (starting with king advantage).