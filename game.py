
import pygame, sys, os
import time
import random
# import playsound

width = 600
height = 800
white = (255,255,255)
black = (0,0,0)
clock = pygame.time.Clock()
g = 1
score = 0
fps = 13
life = 10 
fruits = ['purple', 'spaceship',  'virus', 'purple', 'bubble', 'rocket']

pygame.init()
# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("C:/Users/ak064/OneDrive/Desktop/code/Fruit-Ninja/", "background-black.png")), (600, 800))
# game display
gameDisplay = pygame.display.set_mode((width, height), pygame.RESIZABLE)
gameDisplay.blit(BG, (0,0))


font = pygame.font.Font('C:/Users/ak064/OneDrive/Desktop/code/Fruit-Ninja/comic.ttf', 32)
score_text = font.render("Score",str(score), True, white)
life_left = font.render("Lives",str(life), True, white )

def generate_random_fruits(fruit):
    path =f'C:/Users/ak064/OneDrive/Desktop/code/Fruit-Ninja/{fruit}.png'
    data[fruit] = {
        'img' : pygame.transform.scale(pygame.image.load(path),(80, 80)),
        'x' : random.randint(100, 500),
        'y' : random.randint(100, 500),
        'speed_x' : random.randint(-2, 2),
        'speed_y' : random.randint(-2, 2),
        'throw' : False,
        't' : 1,
        'hit' : False,
    }

    if(random.random() >= 0.95):
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False
# genrate random
c=1
data = {}
for fruit in fruits:
    
    generate_random_fruits(fruit)
# display update
pygame.display.update()
# infinit loop 
while True:
    if(c-score==10):
        break


    gameDisplay.blit(BG, (0,0))
    # gameDisplay.blit(score_text, (0,0))
    gameDisplay.blit(score_text, (0,0))

    for key,value in data.items():
        if value['throw']:
            value['x'] = value['x'] + value['speed_x']
            value['y'] = value['y'] + 15
            value['speed_y'] += (g*value['t'])
            value['t'] += 0.3

            if value['y'] <= 700:
                gameDisplay.blit(value['img'], (value['x'],value['y']))
            else:
                generate_random_fruits(key)

            current_position = pygame.mouse.get_pos()
            if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x']+60 and current_position[1] > value['y'] and current_position[1] < value['y']+60:
                path = os.path.join("C:/Users/ak064/OneDrive/Desktop/code/Fruit-Ninja/"+key+'.png')
                value['img'] = pygame.transform.scale(pygame.image.load(path), (0, 0))
                value['speed_x'] += 1
                score += 1
                score_text = font.render(str(score), 1, white)
                life_left = font.render(str(life), True, white )

                value['hit'] = True
                
            else:
                c+=1

        else:
            generate_random_fruits(key)
            

    pygame.display.update()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()