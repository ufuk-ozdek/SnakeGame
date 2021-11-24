import pygame
import random
import time

seconds = time.time()

pygame.init()

width = 720
height = 600

snake_block = 12
clock = pygame.time.Clock()

purple = (255, 204, 255)
yellow = (250, 250, 100)
black = (0, 0, 0)
red = (210, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
white = (255, 255, 255)

snake_speed = 12

board = pygame.display.set_mode((width, height))

pygame.display.set_caption("Ufuk's Snake Game")

score_font = pygame.font.SysFont("copperplategothiclight", 35)
font_style = pygame.font.SysFont("cambodian", 30)


def snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(board, purple, [x[0], x[1], block, block])


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    board.blit(value, [0, 0])


def message(msg, colour):
    message = font_style.render(msg, True, colour)
    board.blit(message, [width / 6, height / 3])


def gameLoop():
    game_ovr = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 12.0) * 12.0
    foody = round(random.randrange(0, height - snake_block) / 12.0) * 12.0

    while not game_ovr:

        while game_close:
            board.fill(black)
            message("Press q to quit r to restart", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_ovr = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_ovr = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        board.fill(red)
        pygame.draw.rect(board, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 12.0) * 12.0
            foody = round(random.randrange(0, height - snake_block) / 12.0) * 12.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()



