import pygame
from checkers.constants import WIDTH, HEIGHT, RED, WHITE
from checkers.game import Game


def cvc(run, clock, game, FPS):
    while run:
        clock.tick(FPS)

        if game.winner() != None:
            if game.winner() == WHITE:
                winner = "White"
            else:
                winner = "Red"
            print("The game was won by " + winner + "!")
            run = False
            return winner

        if game.turn == WHITE:
            game.computer_move(WHITE)
        else:
            game.computer_move(RED)

        game.update()


def dev_tester(FPS, WIN):
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    while run:
        clock.tick(FPS)

        if game.winner() != None:
            if game.winner() == WHITE:
                winner = "White"
            elif game.winner() == RED:
                winner = "Red"
            else:
                winner = "Draw"
            print("The game was won by " + winner + "!")
            run = False
            break

        if game.turn == WHITE:
            game.computer_move(WHITE)
        else:
            game.computer_move(RED)

        game.update()
    pygame.quit()
    return winner


def test():
    test_num = 4
    red_wins = 0
    white_wins = 0

    for i in range(test_num):
        FPS = 60
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Checkers')

        winner = dev_tester(FPS, WIN)
        if winner == "Red":
            red_wins += 1
        elif winner == "White":
            white_wins += 1

    print("Testing complete.")
    print(str(test_num) + " tests run in total.")
    print(str(red_wins) + " Red wins.")
    print(str(white_wins) + " White wins.")


test()
