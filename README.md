# 4701 AI Practicum

Run `make install` to install requirements.


Run `python3 main.py` followed two ints to play checkers. The first int determines the type of player for red and the second int determines the type of player for white. Any int between 0 and 99 inclusive is accepted. If the int is 0, that color's piece is human-controlled. If it is a single-digit int, that color's piece is controlled by an AI minimax with base heuristics at that int's depth. If it is a double-digit int, the first digit represents the custom hueristic # of the AI and the second digit represents the depth of the minimax algorithm.


List of heuristics:

#0 - Base heuristic: piece advantage, king advantage

#1 - Custom heuristic: piece advantage, king advantage, move advantage, board control, vulnerability, home row control


Additionally, `main.py` takes up to 5 additional input args (7 in total). These input args change the weights of parameters for heuristic #1. The int given as an arg is divided by 4 and used as the weight for its corresponding parameter. For example, an input arg of 3 means the weight for its corresponding parameter will be 3/4. The corresponding parameters are as follows:

Arg 3 - king advantage

Arg 4 - move advantage

Arg 5 - board control

Arg 6 - vulnerability

Arg 7 - home row control


Run `make zip` to zip the program.


To run the test file, enter the `test` directory and run `./depth_experimenter.sh`.


The `output.csv` file contains rows with 5 values. In order, they represent red depth, red heuristic #, white depth, white hueristic #, red wins, white wins, and draws for the number of simulations ran at that depth.


`parameter_finder.sh` is used to calculate optimal tuning parameters for the AI minimax algorithm with custom heuristics. The `output.csv` file it produces contains rows where each row corresponds to the 5 heuristic values in order followed by the score. The last line has the optimal heuristics and the best score that it produces.