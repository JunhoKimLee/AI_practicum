class CheckerGame():
    # Decisions until now:
    # source: https://github.com/shtsai/checker-game
    # 1) 8*8 board for now
    # 2) player1 is the first player, player 2 is the second player
    # 3) for now both player should be human players, later we can choose agorithms to make them play against each other
    # 4) for now player1 plays with red (r) and player2 player with black (b)
    # 5) When (r) is promoted, it becomes (R) and when (b) is promoted, it becomes (B)
    def __init__(self):
        # self.grid = [[0]*8 for _ in range(8)]
        self.board = self.initBoard()
        # player1 always goes first 
        self.player1 = self.choosePlayer(1)
        self.player2 = self.choosePlayer(2)

        self.play()
        self.printBoard() # TO BE DELETED

    def initBoard(self):
        # Do we want 8*8 grid or 6*6 grid or let players choose?
        board = [[0]*8 for i in range(8)] 
        self.player1checkers = set()
        self.player2checkers = set()
        self.checkerPositions = {}

        # place 12 checkers on the board
        for i in range(12):
            self.player1checkers.add(i + 1)
            self.player2checkers.add(-(i + 1))
            if i%3 == 0:
                board[0][2*(i//3)+1] = -(i + 1)
                self.checkerPositions[-(i + 1)] = (0, 2*(i//3)+1)
                board[7][2*(i//3)] = i + 1
                self.checkerPositions[i + 1] = (7, 2*(i//3))
            elif i%3 ==1:
                board[1][2*(i//3)] = -(i + 1)
                self.checkerPositions[-(i + 1)] = (1, 2*(i//3))
                board[6][2*(i//3)+1] = i + 1
                self.checkerPositions[i + 1] = (6, 2*(i//3)+1)
            else:
                board[2][2*(i//3)+1] = -(i + 1)
                self.checkerPositions[-(i + 1)] = (2, 2*(i//3)+1)
                board[5][2*(i//3)] = i + 1 
                self.checkerPositions[i + 1] = (5, 2*(i//3))
        return board   

    def choosePlayer(self, num):
        # TO BE EXTENDED TO CHOOSE BETWEEN (HUMAN, MINIMAX, CUSTOM HEURISTICS ...) depending on ans
        ans = input(f"CHOOSE THE {num} PLAYER")

    def printBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                check = self.board[i][j]
                if (check < 0):
                    if (check <= -100):
                        print(' ' + 'B',end=' ')
                    else:
                        print(' ' + 'b',end=' ')
                elif (check > 0):
                    if (check >= 100):
                        print(' ' + 'R',end=' ')
                    else:
                        print(' ' + 'r',end=' ')
                else:
                    print(' ' + '0',end=' ')
            print()

    def checkPromote(self, row, col, player):
        old_checker = self.board[row][col]
        if player==1 and row == 0 and old_checker<100:
            self.checkerPositions.pop(old_checker)
            self.player1checkers.remove(old_checker)
            new_checker = old_checker+100
            self.checkerPositions[new_checker] = (row,col)  
            self.board[row][col] = new_checker
            self.player1checkers.add(new_checker)
        elif player==2 and row ==7 and old_checker>-100:
            self.checkerPositions.pop(old_checker)
            self.player2checkers.remove(old_checker)
            new_checker = old_checker-100
            self.checkerPositions[new_checker] = (row,col)  
            self.board[row][col] = new_checker
            self.player2checkers.add(new_checker)


    def move(self, oldrow, oldcol, row, col, player):
        if self.isValidMove(oldrow, oldcol, row, col, player):
            checker = self.board[oldrow][oldcol]

            # move the checker
            self.board[row][col] = self.board[oldrow][oldcol]
            self.board[oldrow][oldcol] = 0
            checkPromote(self, row, col, player)

            # capture move, remove captured checker
            if abs(oldrow - row) == 2:
                toRemove = self.board[(oldrow + row) // 2][(oldcol + col) // 2]
                if toRemove > 0:
                    self.player1checkers.remove(toRemove)
                else:
                    self.player2checkers.remove(toRemove)
                self.board[(oldrow + row) // 2][(oldcol + col) // 2] = 0

            # return next turn 
            if player==1:
                if row - oldrow == -2:  # capture move
                    return 1
                else:
                    return 2
            if player==2:
                if row - oldrow == 2:  # capture move
                    return 2
                else:
                    return 1

    # move command: move(oldrow, oldcol, row, col, player)
    # check if move is valid 
    def isValidMove(self, oldrow, oldcol, row, col, player):
        if self.board[oldrow][oldcol] == 0 or self.board[row][col] != 0:
            return False
        
        if oldrow < 0 or oldrow > 7 or oldcol < 0 or oldcol > 7 \
                or row < 0 or row > 7 or col < 0 or col > 7:
            return False

        checker = self.board[oldrow][oldcol]
        # player1's turn # need to update case for promoted checker
        if player==1:
            # regular checker
            if checker < 100: 
                if row - oldrow == -1:   # regular move
                    return abs(col - oldcol) == 1
                elif row - oldrow == -2:  # capture move
                    #  \ direction or / direction
                    return (col - oldcol == -2 and self.board[row+1][col+1] < 0) \
                        or (col - oldcol == 2 and self.board[row+1][col-1] < 0)
                else:
                    return False
            # promoted checker
            else:
                if abs(row - oldrow) == 1:   # regular move
                    return abs(col - oldcol) == 1
                elif abs(row - oldrow) == 2:  # capture move
                    #  \ direction or / direction
                    return (col - oldcol == -2 and self.board[row+1][col+1] < 0) \
                        or (col - oldcol == 2 and self.board[row+1][col-1] < 0)
                else:
                    return False

        # player 2's turn # need to update case for promoted checker
        elif player==2:
            # regular checker
            if checker > -100: 
                if row - oldrow == 1:   # regular move
                    return abs(col - oldcol) == 1
                elif row - oldrow == 2: # capture move
                    # / direction or \ direction
                    return (col - oldcol == -2 and self.board[row-1][col+1] > 0) \
                        or (col - oldcol == 2 and self.board[row-1][col-1] > 0)
                else:
                    return False
            # promoted checker
            else:
                if abs(row - oldrow) == 1:   # regular move
                    return abs(col - oldcol) == 1
                elif abs(row - oldrow) == 2:  # capture move
                    #  \ direction or / direction
                    return (col - oldcol == -2 and self.board[row+1][col+1] < 0) \
                        or (col - oldcol == 2 and self.board[row+1][col-1] < 0)
                else:
                    return False

        # invalid player
        else:
            return False

    # Check if the player can cantinue
    def playerCanContinue(self, player):
        directions = [[-1, -1], [-1, 1], [-2, -2], [-2, 2]]
        checkers = self.player2checkers if player==2 else self.player1checkers
        for checker in self.checkers:
            position = self.checkerPositions[checker]
            row = position[0]
            col = position[1]
            for dir in directions:
                if self.isValidMove(row, col, row + dir[0], col + dir[1], True):
                    return True
        return False

    # Neither player can can continue, thus game over
    def isGameOver(self):
        if len(self.player1checkers) == 0 or len(self.player2checkers) == 0:
            return True
        else:
            return (not self.playerCanContinue(1)) and (not self.playerCanContinue(2))

    def play(self):
        # needs to be implemented
        pass
    # take turns between player1 and player2 
        
