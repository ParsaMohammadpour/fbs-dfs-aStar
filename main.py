import pygame
import colors
from params import *
from Environment import Board
from Agent import Agent

# initialize:
FPS = 60
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Search Game")

# setting start and end point :
start = {'x': 6, 'y': 0}
end = {'x': 12, 'y': 0}

gameBoard = Board(start, end)
agent = Agent(gameBoard)


def main():
    run = True
    clock = pygame.time.Clock()
    WIN.fill(colors.black)

    agent.a_star(gameBoard)

    while run:
        clock.tick(FPS)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        gameBoard.draw_world(WIN)

    pygame.quit()


main()
