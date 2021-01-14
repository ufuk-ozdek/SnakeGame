
import random
import time
import pygame

pygame.init()


seconds = time.time()

purple = (255, 204, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
white = (255, 255, 255)

width = 800
height = 600

disp = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ufuk's Snake Game")

clock = pygame.time.Clock()

ssnake_block = 10
ssnake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)



def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    disp.blit(value, [0, 0])


def snake(ssnake_block, ssnake_list):
    for x in ssnake_list:
        pygame.draw.rect(disp, purple, [x[0], x[1], ssnake_block, ssnake_block])


def message(msg, colour):
    mesgg = font_style.render(msg, True, colour)
    disp.blit(mesgg, [width / 6, height / 3])

def gameLoop():
    game_ovr = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    ssnake_List = []
    Length_of_ssnake = 1

    foodx = round(random.randrange(0, width - ssnake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - ssnake_block) / 10.0) * 10.0

    while not game_ovr:

        while game_close == True:
            disp.fill(black)
            message("Press q to quit c to restart", red)
            Your_score(Length_of_ssnake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_ovr = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_ovr = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -ssnake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = ssnake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -ssnake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = ssnake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        disp.fill(red)
        pygame.draw.rect(disp, green, [foodx, foody, ssnake_block, ssnake_block])
        ssnake_Head = []
        ssnake_Head.append(x1)
        ssnake_Head.append(y1)
        ssnake_List.append(ssnake_Head)
        if len(ssnake_List) > Length_of_ssnake:
            del ssnake_List[0]

        for x in ssnake_List[:-1]:
            if x == ssnake_Head:
                game_close = True

        snake(ssnake_block, ssnake_List)
        Your_score(Length_of_ssnake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - ssnake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - ssnake_block) / 10.0) * 10.0
            Length_of_ssnake += 1

        clock.tick(ssnake_speed)

    pygame.quit()
    quit()

gameLoop()

