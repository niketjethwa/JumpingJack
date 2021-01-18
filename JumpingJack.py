import pygame
import math
import sys

pygame.init()

win_width = 730
win_height = 400

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

gameScreen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Jumping Jack")

walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'),
             pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'),
             pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]

walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'),
            pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'),
            pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]

background_image = pygame.image.load("images/bg.jpg")
background = pygame.transform.scale(background_image, (730, 400))

f_img = pygame.image.load("images/red_bricks.jpg")
char_img = pygame.image.load("images/R1.png")
gameover = pygame.image.load("images/gameover.jpg")


x = 25
y = 270
width = 40
height = 60
vel = 5

run = True

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

# running pipe
pipe_img = pygame.image.load("images/pipe.png")
fpsClock = pygame.time.Clock()
imageX = 700  # x coordnate of image
imageY = 250  # y coordinate of image

score = 0


def score_display():
    global score
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render(str(score), True, green, white)
    textRect = text.get_rect()
    textRect.center = (700, 30)
    gameScreen.blit(text, textRect)


def redrawgamewindow():
    global walkCount, score, left, right
    global run, imageX, imageY, x, y

    gameScreen.blit(background, (0, 0))
    gameScreen.blit(f_img, (0, 330), (30, 30, 900, 80))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        i = (walkCount // 3) % len(walkLeft)
        gameScreen.blit(walkLeft[i], (x, y))
        walkCount += 1
        print("WC :", walkCount)
        print("Hello ", "x =", x, "y =", y)

        if isJump:
            left = True
            right = True

    elif right:
        i = (walkCount // 3) % len(walkLeft)
        gameScreen.blit(walkRight[i], (x, y))
        walkCount += 1
        print("WC :", walkCount)
        print("Hie1 ", "x =", x, "y =", y)

        if isJump:
            left = True
            right = True

    else:
        gameScreen.blit(char_img, (x, y))
        walkCount += 1
        print("WC :", walkCount)
        print("Hie2 ", "x =", x, "y =", y)

        if isJump:
            left = True
            right = True


def jumpFunction():
    global walkCount, score, isJump, jumpCount
    global run, imageX, imageY, left, right, x, y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 700 - vel - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.3
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
            score += 1
            score_display()


def running_pipe():
    global walkCount, score, left, right
    global run, imageX, imageY

    if imageX <= -540 and imageY <= 250:
        imageX = 700
        imageY = 250
        imageX -= 20
        gameScreen.blit(pygame.transform.scale(pipe_img, (50, 80)), (imageX, imageY))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    else:
        imageX -= 20
        gameScreen.blit(pygame.transform.scale(pipe_img, (50, 80)), (imageX, imageY))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()
        pygame.time.delay(50)


def start():
    gameScreen.fill((0, 0, 0))
    pygame.mixer.music.load("audio/jack_theme.wav")
    pygame.mixer.music.play(-1, 0.0)
    start_img = pygame.image.load('images/start.jpg')
    start_img_rect = start_img.get_rect()
    start_img_rect.center = (win_width / 2, win_height / 2)
    gameScreen.blit(start_img, start_img_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()


def game_over():
    global x, y, imageX, imageY, score
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound("audio/"
                               ""
                               "jack_dies.wav")
    music.play()
    pygame.time.delay(700)

    gameScreen.fill((0, 0, 0))
    game_over_img = pygame.image.load("images/gameover.jpg")
    game_over_img_rect = game_over_img.get_rect()
    game_over_img_rect.center = (win_width / 2, win_height / 2)
    gameScreen.blit(game_over_img, game_over_img_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                music.stop()

                score = 0
                x = 25         # reset the values
                y = 270
                imageX = 700
                imageY = 250
                pygame.mixer.music.play(-1, 0.0)
                game_loop()
        pygame.display.update()


def game_loop():
    while True:
        score_display()
        running_pipe()

        if walkCount > 0:
            if x == 25 and imageX == 80:  # start position and char not jumping
                print("HeyElif1", imageX, imageY, y)
                # run = False
                pygame.time.delay(100)
                game_over()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

            elif (imageX == (math.ceil(x / 10.0) * 10)) and imageX < x:  # for odd  co-ordinate values
                #  or (imageX <= x + 50) and (isJump == False):
                print("Hey0", imageX, imageY, x, y)
                # run = False
                pygame.time.delay(100)
                game_over()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

            elif (imageX > x) and (imageX <= x + 50) and (isJump == False):  # collision
                print("Hey01", imageX, imageY, x, y)
                # run = False
                pygame.time.delay(100)
                game_over()
            else:
                print("GO")

        jumpFunction()
        pygame.display.update()
        gameScreen.blit(char_img, (0, 160))
        redrawgamewindow()

start()
