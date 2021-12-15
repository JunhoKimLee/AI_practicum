# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
import sys

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    # 0 indicates player. a postive int represents AI with depth of that val.
    try:
        red = int(sys.argv[1])
        white = int(sys.argv[2])
    except:
        print("Input var(s) is not a valid int.")
        quit()
    if red < 0 or white < 0:
        print("Input var(s) is out of range.")
        quit()

    if red == 0:
        print("Red is a human player.")
    else:
        print("Red is an AI minimax with depth " + str(red) + ".")
    if white == 0:
        print("White is a human player.")
    else:
        print("White is an AI minimax with depth " + str(white) + ".")

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            if game.winner() == WHITE:
                winner = "White"
            elif game.winner() == RED:
                winner = "Red"
            else:
                winner = "no one. It was a draw"
            print("The game was won by " + winner + "!")
            run = False
            return winner

        # uncomment this to go through AI games move by move
        # mode = input()

        if game.turn == RED:
            if red == 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        row, col = get_row_col_from_mouse(pos)
                        game.select(row, col)
            else:
                game.computer_move(RED, red)

        elif game.turn == WHITE:
            if white == 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        row, col = get_row_col_from_mouse(pos)
                        game.select(row, col)
            else:
                game.computer_move(WHITE, white)

        game.update()

    pygame.quit()


main()
