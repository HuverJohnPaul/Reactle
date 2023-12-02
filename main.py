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
#JP--used to navigate directories
import os

#JP
#innitilize the system
pygame.init()

#get the info about the surface the user has
surface_inf=pygame.display.Info()

#set veriable for the height and width of the surface the user has
surface_width = surface_inf.current_w
surface_height = surface_inf.current_h



#create the display surface with a height of .95 of surface height so that the x button and top of surface can be seen
surface = pygame.display.set_mode((surface_width, surface_height*.95))
#create the display name/title
pygame.display.set_caption("Reactle")

Icon=pygame.image.load('images/reactle icon.png')

pygame.display.set_icon(Icon)

#b_colour is set to an RBG colour (red)
b_colour=(0,0,0)

#b


#innitialize the running veriable to True so that the window stays till running is set to Flase
running=True


#loop till running False
while running:  
    #event in pygame is anything happening
    for event in pygame.event.get():  

        #if they click the exit button close the window
        if event.type == pygame.QUIT:  
            #set running to False
            running = False

    #change the background colour to the verable b_colour   
    surface.fill(b_colour)

    #updates the display surface
    pygame.display.flip()



