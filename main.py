# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game

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
    red = -1
    white = -1
    mode = ""
    while red == -1:
        print("Select controller of Red. Type P for player. Type C followed by a # that indicates depth for the minimax bot (e.g. C3 means minimax bot with depth 3).")
        mode = input("> ")
        if mode == "P":
            red = 0
        elif mode[0] == "C":
            depth = int(mode[1:])
            if depth >= 1:
                red = depth

    while white == -1:
        print("Select controller of White. Type P for player. Type C followed by a # that indicates depth for the minimax bot (e.g. C3 means minimax bot with depth 3).")
        mode = input("> ")
        if mode == "P":
            white = 0
        elif mode[0] == "C":
            depth = int(mode[1:])
            if depth >= 1:
                white = depth

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
            break

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
