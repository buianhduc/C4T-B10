import datetime
import pygame

import time

#pygame.init()

Alarm = input()
currentHour = datetime.datetime.now().strftime("%H:%M")
while currentHour !="Alarm":
    currentHour = datetime.datetime.now().strftime("%H:%M")
print("Bao thuc")
pygame.mixer.music.load("Di Du Dua Di - Bich Phuong.mp3")

pygame.mixer.music.play()


