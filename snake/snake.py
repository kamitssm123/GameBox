import pygame
import random
import os
pygame.init()


white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 900
screen_height = 500




clock = pygame.time.Clock()

gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()


# exit_game = False
# game_over = False
# snake_x = 40
# snake_y = 80
# snake_size = 10
# snake_size = 10
# food_size = 10
# velocity_x = 0
# velocity_y = 0
# score = 0
font = pygame.font.SysFont(None, 55)
font2 = pygame.font.SysFont(None, 35)

def screen_text(text, color, x, y, font):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])



def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, (x, y, snake_size, snake_size))


def first_appear():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        screen_text("Welcome to Snakes", black, 300, 200, font2)
        screen_text("Press Space Bar to Play", black, 290, 230, font2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

        pygame.display.update()
        clock.tick(60)


def game_loop():


    snake_x = 40
    snake_y = 80
    snake_size = 10
    fps = 30
    food_x = random.randint(60, screen_width-100)
    food_y = random.randint(100, screen_height-100)
    exit_game = False
    game_over = False
    snake_x = random.randint(100, screen_width-100)
    snake_y = random.randint(100, screen_height-100)
    snake_size = 20
    food_size = 20
    init_vel = 5
    score = 0

    velocity_x = 0
    velocity_y = 0

    if not os.path.exists("highscore.txt"):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("snake/highscore.txt", "r") as f:
        highscore = f.read()

    snk_length = 1
    snk_list = []

    while not exit_game:

        
        # gameWindow.fill(white)
        # screen_text("Game Over! Please tinue", red, 160, 200, font2)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         exit_game = True

        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_SPACE:

        if game_over:
            with open("snake/highscore.txt", "w") as f:
                f.write(str(highscore))

            gameWindow.fill(white)
            screen_text("Game Over! Please press enter to continue", red, 160, 200, font2)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
        
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_vel
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -(init_vel)
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -(init_vel)
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_vel
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y    

            if (abs(snake_x-food_x) < 20) and (abs(snake_y-food_y)<20):
                score += 10
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length += 1
                init_vel += 0.3
                if score > int(highscore):
                    highscore = score

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            

            temp = "Score: " + str(score) + "  " + "Highscore: " + str(highscore)
            gameWindow.fill(white)
            screen_text(temp, red, 5, 5, font)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if snake_x<0 or snake_x > screen_width or snake_y <0 or snake_y > screen_height :
                game_over = True

            if head in snk_list[:-1]:
                game_over == True


            pygame.draw.rect(gameWindow, red, (food_x, food_y, food_size, food_size))
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
    
first_appear()









