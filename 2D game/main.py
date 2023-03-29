import pygame
from pygame.locals import *
import random

size = width, height = (600, 600)
road_width = int(width/1.6)
roadmark_width = int(width/60)

right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4

speed = 1

pygame.init()
running = True
screen = pygame.display.set_mode((size))
pygame.display.set_caption("Car racing game")
screen.fill((60, 220, 0))

pygame.display.update()

car = pygame.image.load("yellow-car.png")
car_location = car.get_rect()
car_location.center = right_lane, height*0.8


car2 = pygame.image.load("white-car.png")
car2_location = car2.get_rect()
car2_location.center = left_lane, height*0.2

counter = 0

while running:
    counter += 1
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level up", speed)
    car2_location[1] += speed
    if car2_location[1] > height:
    
        if random.randint(0,1) == 0:
            car2_location.center = right_lane, -200
        else:
            car2_location.center = left_lane, -200

    if car_location[0] == car2_location[0] and car2_location[1] > car_location[1] - 250:
        print("Game Over! You Lost")
        break

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_location = car_location.move([-int(road_width/2), 0])

            if event.key in [K_d, K_RIGHT]:
                car_location = car_location.move([int(road_width/2), 0])

    pygame.draw.rect(screen, (50, 50, 50), (width/2- road_width/2, 0, road_width, height))
    pygame.draw.rect(screen, (255, 240, 60), (width/2- roadmark_width/2, 0, roadmark_width, height))
    pygame.draw.rect(screen, (255, 255, 255), (width/2- road_width/2 + roadmark_width*2, 0, roadmark_width, height))
    pygame.draw.rect(screen, (255, 255, 255), (width/2+ road_width/2 - roadmark_width*3, 0, roadmark_width, height))




    screen.blit(car, car_location)
    screen.blit(car2, car2_location)
    pygame.display.update()
pygame.quit()