import pygame
import random

x=260
y=500
#Screen initialize
pygame.init()

screen=pygame.display.set_mode((800,800))
screen.fill((0,255,0))

pygame.display.set_caption("Stone-Paper-Scissor")

run=True

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    """p1p = 0
    cp = 0

    for i in range(0, 3):

        while (p1p != 3 and cp != 3):

            ans = input("Enter the answer")
            wordList = ["stone", "paper", "scissor", "stone", "paper", "scissor",
                        "stone", "paper", "scissor", "stone", "paper", "scissor"]
            cans = random.choice(wordList)

            if (ans == "stone" and cans == "scissor"):
                print("Player1: ", ans, "\t", "Computer: ", cans)
                print("Player1 Won")
                p1p = p1p + 1
                print("Player1 Points:", p1p, "\n")


            elif (ans == "stone" and cans == "paper"):
                print("Player1: ", ans, "\t", "Computer: ", cans)
                print("Computer Won")
                cp = cp + 1
                print("Computer Points:", cp, "\n")

            elif (ans == "stone" and cans == "stone"):
                print("Player1: ", ans, "\t", "Computer: ", cans)
                print("Tie\n")

            elif (ans == "paper" and cans == "scissor"):
                print("Player1: ", ans, "\t", "Computer: ", cans)
                print("Computer Won")
                cp = cp + 1
                print("Computer Points:", cp, "\n")


            elif (ans == "paper" and cans == "paper"):
                print("Player1: ", ans, "\t", "Computer: ", cans)
                print("Tie\n")


            elif (ans == "paper" and cans == "stone"):
                print("Player1: ", ans, "\t", "Computer: ", cans)
                print("Player1 Won")
                p1p = p1p + 1
                print("Player1 Points:", p1p, "\n")

            elif (ans == "scissor" and cans == "scissor"):
                print("Player1: ", ans, "\t", "Computer: ", cans)
                print("Tie\n")

            elif (ans == "scissor" and cans == "paper"):
                print("Player1: ", ans, "\t", "Computer: ", cans)
                print("Player1 Won")
                p1p = p1p + 1
                print("Player1 Points:", p1p, "\n")

            elif (ans == "scissor" and cans == "stone"):
                print("Player1: ", ans, "\t", "Computer: ", cans)
                print("Computer Won")
                cp = cp + 1
                print("Computer Points:", cp, "\n")"""

    play = pygame.image.load("L3.png").convert()
    play_button = pygame.draw.rect(screen, (255,255,255), [150, 450, 100, 50])

    #screen.blit(play, [350, 500])
    button(play, 150, 450, 100, 50,(0,0,20),(0,0,200))
    #button("Quit", 550, 450, 100, 50, (0,0,10),(0,0,100))

    #pygame.draw.line(screen,(0,135,0),(150,100),(150,400),20)
    pygame.display.update()
pygame.quit()
