# 4701 AI Practicum

Run `make install` to install requirements.
Run `python3 main.py` followed two ints to play checkers. Only two ints are accepted and any additional ints are ignored. The first int determines the type of player for red and the second int determines the type of player for white. Any int between 0 and 99 inclusive is accepted. If the int is 0, that color's piece is human-controlled. If it is a single-digit int, that color's piece is controlled by an AI minimax with base heuristics at that int's depth. If it is a double-digit int, the first digit represents the custom hueristic # of the AI and the second digit represents the depth of the minimax algorithm.
Run `make zip` to zip the program.
To run the test file, enter the `test` directory and run `./depth_experimenter.sh`.
The `output.csv` file contains rows with 5 values. In order, they represent red depth, red heuristic #, white depth, white hueristic #, red wins, white wins, and draws for the number of simulations ran at that depth.