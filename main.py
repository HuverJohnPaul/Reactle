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
surface_info=pygame.display.Info()

#set veriable for the height and width of the surface the user has
surface_width = surface_info.current_w
surface_height = surface_info.current_h

#initilize the clock to allow for a frame rate
clock=pygame.time.Clock()


#create the display surface with a height of .95 of surface height so that the x button and top of surface can be seen
surface = pygame.display.set_mode((surface_width, surface_height*.95))
#create the display name/title
pygame.display.set_caption("Reactle")
#create the icon for the window
Icon=pygame.image.load('images/reactle icon.png')
pygame.display.set_icon(Icon)

#AL
#load the background image
background_image=pygame.image.load("images/background.png")
#scale the image so it fits the screen
background_image_upscale=pygame.transform.scale(background_image,(surface_width, surface_height))
#add the surface of the upscalled background image to the main surface
surface.blit(background_image_upscale, (0, 0))

#load the opoque chemistry background image
background_image_chem=pygame.image.load("images/chemistry_background.png")
#scale the image to fit the surface
background_image_chem_upscale=pygame.transform.scale(background_image_chem,(surface_width, surface_height))
#made the image more opque
background_image_chem_upscale.set_alpha(15)
#blit this surface onto the main one
surface.blit(background_image_chem_upscale, (0, 0))

#create the font to be used for the title text with the size as a ratio of the width to account for differences in aspect ratios
title_font = pygame.font.SysFont("Franklin Gothic", (surface_width//15))
#create a text surface that has black text saying Reactle
#the true makes the text smoother
title_text_surface=title_font.render("Reactle",True,(0,0,0))

#creates a text box surface that is centered in the x axis, and is near the top in the y based off of propotions of the users surface
title_text_box_centered=((surface_width-title_text_surface.get_width())//2,(surface_height-title_text_surface.get_height())//8)

#add the surface onto the text box to create it on the main surface
surface.blit(title_text_surface, title_text_box_centered)

#JP
# #innitialize the running veriable to True so that the window stays till running is set to Flase
running=True




#import in the reactions from the database
from database import reactions_database
#import in the random module
import random
#create a list of the items of the rdict dictionary
items_list = list(reactions_database.rdict.items())
#randomly select an item
random_item = random.choice(items_list)
#grab the lists cosponding to the products and reactents
reaction_details = random_item[1]
#split the list into the respective lists.
reactants = reaction_details['reactants']
products = reaction_details['products']


#creates a font for the arrow symbol
arrow_font = pygame.font.SysFont("times new roman", (surface_width//10))
#create a text surface that has a black arrow
#the true makes the text smoother
arrow_text_surface=arrow_font.render("→",True,(0,0,0))
#creates a text box surface that is centered in the x axis, and is near the top in the y based off of propotions of the users screen
arrow_text_box_centered=((surface_width-arrow_text_surface.get_width())//2,(surface_height-arrow_text_surface.get_height())//4.45)

#add the surface onto the text box to create it on the main surface
surface.blit(arrow_text_surface, arrow_text_box_centered)

#creates a font for the plus sign symbols
plus_sign_font = pygame.font.SysFont("times new roman", (surface_width//14))

#create a text surface that has a black plus
#the true makes the text smoother
plus1_text_surface=plus_sign_font.render("+",True,(0,0,0))
#creates a text box surface that is on the same y level as the arrow but off towards the left
plus1_text_box_position=((surface_width-arrow_text_surface.get_width())//4.25,(surface_height-arrow_text_surface.get_height())//3.75)

#add the surface onto the text box to create it on the main surface
surface.blit(plus1_text_surface, plus1_text_box_position)




#creatse a text surface that has a black plus
#the true makes the text smoother
plus2_text_surface=plus_sign_font.render("+",True,(0,0,0))
#creates a text box surface that is near the top in line with the arrow but off to the right
plus2_text_box_position=((surface_width-arrow_text_surface.get_width())//1.217,(surface_height-arrow_text_surface.get_height())//3.75)
#add the surface onto the postion so that it appears
surface.blit(plus2_text_surface, plus2_text_box_position)


#itinilizes the necicassary number of fields for the double displacment reaction
field_text=[""]*20

#sets black as the RGB colour code for balck
black=(255,255,255)

#the font used for the input fields
field_font = pygame.font.SysFont("times new roman", 24)
#constants for the double displacment reaction
FIELD_WIDTH = 85
FIELD_HEIGHT = 60
MAX_CHARS = 2
NUM_FIELDS = 20

#intially be in the first text box
active_field=0
#loop till break
while True:
    for event in pygame.event.get():
        #if the user clicks the x button
        if event.type == pygame.QUIT:
            #exit the program
            pygame.quit()
            sys.exit()
        #if the user presses a key
        elif event.type == pygame.KEYDOWN:
                # if the key is a letter or number and the length of the text is less than the max characters
            if event.unicode.isalnum() and len(field_text[active_field]) < MAX_CHARS:
                # add unicode character to the active field
                new_char = event.unicode
                if len(field_text[active_field]) == 0:
                    new_char = new_char.upper()
                elif len(field_text[active_field]) == 1:
                    new_char = new_char.lower()
                field_text[active_field] += new_char
            # if the user presses backspace
            elif event.key == pygame.K_BACKSPACE:
                # remove the last character from the active field
                field_text[active_field] = field_text[active_field][:-1]
            # if the user presses tab
            elif event.key == pygame.K_TAB:
                # move to the next field by adding one to the active field and using the modulo to loop back to the first field if it would be the last field
                active_field = (active_field + 1) % NUM_FIELDS
            # if the user clicks the mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # get the mouse position
                mouse_x, mouse_y = event.pos
                # loop through the fields enumerated
                for i, (field_x, field_y) in enumerate(field_positions):
                    field_rect = pygame.Rect(field_x, field_y, FIELD_WIDTH, FIELD_HEIGHT)
                    # if the mouse click is within the tolerance of one of the input fields
                    if field_rect.collidepoint(mouse_x, mouse_y):
                        # set the active field to the one that was clicked on
                        active_field = i

    #innitialize the field positions list
    field_positions = []
        # Draw the text fields
    # draw the text input fields
    for i, text in enumerate(field_text):
        #changes the rectangle postitions individually to make desired pattern
        if i==0:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+20, (surface_height - FIELD_HEIGHT) //3.75, FIELD_WIDTH+5, FIELD_HEIGHT+5)
        if i==1:
            field_rect = pygame.Rect(i * (FIELD_WIDTH+5)+35, (surface_height - FIELD_HEIGHT) //3.75, FIELD_WIDTH, FIELD_HEIGHT+5)
        if i==2:
            field_rect = pygame.Rect(i * (FIELD_WIDTH+3)+35, (surface_height - FIELD_HEIGHT) //3.5, FIELD_WIDTH/2, FIELD_HEIGHT)
        if i==3:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+8, (surface_height - FIELD_HEIGHT) //3.75, FIELD_WIDTH, FIELD_HEIGHT+5)
        if i==4:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+10, (surface_height - FIELD_HEIGHT) //3.5, FIELD_WIDTH/2, FIELD_HEIGHT)
        if i==5:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+65, (surface_height - FIELD_HEIGHT) //3.75, FIELD_WIDTH, FIELD_HEIGHT+5)
        if i==6:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+76, (surface_height - FIELD_HEIGHT) //3.75, FIELD_WIDTH, FIELD_HEIGHT+5)
        if i==7:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+80, (surface_height - FIELD_HEIGHT) //3.5, FIELD_WIDTH/2, FIELD_HEIGHT)
        if i==8:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+45, (surface_height - FIELD_HEIGHT) //3.75, FIELD_WIDTH, FIELD_HEIGHT+5)
        if i==9:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+50, (surface_height - FIELD_HEIGHT) //3.5, FIELD_WIDTH/2, FIELD_HEIGHT)
        if i==10:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+205, (surface_height - FIELD_HEIGHT) //3.75, FIELD_WIDTH, FIELD_HEIGHT+5)
        if i==11:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+210, (surface_height - FIELD_HEIGHT) //3.75, FIELD_WIDTH, FIELD_HEIGHT+5)
        if i==12:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+215, (surface_height - FIELD_HEIGHT) //3.5, FIELD_WIDTH/2, FIELD_HEIGHT)
        if i==13:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+180, (surface_height - FIELD_HEIGHT) //3.75, FIELD_WIDTH, FIELD_HEIGHT+5)
        if i==14:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+185, (surface_height - FIELD_HEIGHT) //3.5, FIELD_WIDTH/2, FIELD_HEIGHT)
        if i==15:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+225, (surface_height - FIELD_HEIGHT) //3.75, FIELD_WIDTH, FIELD_HEIGHT+5)
        if i==16:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+230, (surface_height - FIELD_HEIGHT) //3.75, FIELD_WIDTH, FIELD_HEIGHT+5)
        if i==17:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+235, (surface_height - FIELD_HEIGHT) //3.5, FIELD_WIDTH/2, FIELD_HEIGHT)
        if i==18:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+200, (surface_height - FIELD_HEIGHT) //3.75, FIELD_WIDTH, FIELD_HEIGHT+5)    
        if i==19:
            field_rect = pygame.Rect(i * (FIELD_WIDTH)+205, (surface_height - FIELD_HEIGHT) //3.5, FIELD_WIDTH/2, FIELD_HEIGHT)
        
        #add the field positions to the list
        field_positions.append((field_rect.x, field_rect.y))

        #draw border around the field (with different colour for the active field)
        border_colour = active_field if i == active_field else black
        pygame.draw.rect(surface, border_colour, field_rect, 2)

        
        
        #create the non active borders
        text_surface = field_font.render(text, True, black)
        surface.blit(text_surface, (field_rect.centerx - text_surface.get_width() // 2, field_rect.centery - text_surface.get_height() // 2))



    # updates the surface
    pygame.display.flip()

    #frame limiting
    clock.tick(60)


