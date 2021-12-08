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

    mode = input("Select Game Mode (PvC or CvC): ")
    if mode == "PvC":
        pvc(run, clock, game)    # 0 represents PvC
    else:
        cvc(run, clock, game)    # 1 represents CvC

    pygame.quit()


def pvc(run, clock, game):
    while run:
        clock.tick(FPS)

        if game.winner() != None:
            if game.winner == WHITE:
                winner = "White"
            else:
                winner = "Red"
            print("The game was won by " + winner + "!")
            run = False
            break

        if game.turn == WHITE:
            game.computer_move(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()


def cvc(run, clock, game):
    pass


main()
