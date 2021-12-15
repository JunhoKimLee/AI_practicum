# 4701 AI Practicum

Run `make install` to install requirements.
Run `python3 main.py` followed two ints to play checkers. The first int determines the depth of the AI minimax controlling red. An input of 0 makes red human controlled. The second int determines the depth of the AI minimax controlling white. An input of 0 makes white human controlled.
Run `make zip` to zip the program.
To run the test file, enter the `test` directory and run `./depth_experimenter.sh`.
The `output.csv` file contains rows with 5 values. In order, they represent red depth, white depth, red wins, white wins, and draws for the number of simulations ran at that depth.