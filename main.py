#Reactle
#Main document that runs the main functions of the game: Reactle
"""
Created on Sat Nov 25 17:47:22 2023

@authors: John-Paul Huver, Agnese, Feyi,Madeline
"""
#JP--sys is used to manage the program and windows so that it can all be closed and exited properly
import sys
#JP--pygame used for windows and surfaces mostly
import pygame


#JP
#innitialize the running veriable to True so that the window stays till running is set to Flase
running=True
#never stop this loop
while running:  
    #event in pygame is anything happening
    for event in pygame.event.get():  
        #if they click the exit button
        if event.type == pygame.QUIT:  
           running = False



