#main visulaized experment

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


#usedto draw the users guess after it has been guessed
def draw_guess(guess, result=None):
    #loop through the guess
    for i, element in enumerate(guess):    
        #if there is no result yet
        color = (255, 255, 255) if result is None else result[i]
        #create the rectangle to put the text onto
        field_rect = pygame.Rect(i * (FIELD_WIDTH)+20, (surface_height - FIELD_HEIGHT) // 3.75 + len(guesses) * (FIELD_HEIGHT + 10), FIELD_WIDTH+5, FIELD_HEIGHT+5)
        #actually draw the rectangle
        pygame.draw.rect(surface, color, field_rect, 2)
        #create the text surface to be put onto the rectangle
        text_surface = field_font.render(element, True, (0, 0, 0))
        #blit them together to be shown
        surface.blit(text_surface, (field_rect.x + (field_rect.width - text_surface.get_width()) // 2, field_rect.y + (field_rect.height - text_surface.get_height()) // 2))


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




# Create a font object
font_button = pygame.font.SysFont("Franklin Gothic", 70)

# Create a rectangle for the button
button_width = 200 
button_height = 100  
#ceter the button in the x axis
button_x = (surface_width - button_width) // 2
#put the button 200 pixels above the bottom of the screen
button_y = surface_height - button_height - 200 
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Create a text surface for the button label
text_surface = font_button.render('Submit', True, (255, 0, 0))

# Draw the button
pygame.draw.rect(surface, (0, 0, 0), button_rect)

# Blit the text onto the screen at the position of the rectangle
surface.blit(text_surface, (button_rect.x + (button_rect.width - text_surface.get_width()) // 2, button_rect.y + (button_rect.height - text_surface.get_height()) // 2))


#itinilizes the necicassary number of fields for the double displacment reaction
field_text=[""]*20

#sets white as the RGB colour code for white
white=(255,255,255)

#the font used for the input fields
field_font = pygame.font.SysFont("times new roman", 56)
#constants for the double displacment reaction
FIELD_WIDTH = 85
FIELD_HEIGHT = 60
MAX_CHARS = 2
NUM_FIELDS = 20

#intially be in the first text box
active_field=0


#intitlaize the lists of preivous geusses and results
guesses = []
results = []
#loop till break
while True:
    #clear the screen by filling it with white to ensure that graphics are updated properly
    surface.fill(white)
    #add back all the surfaces that are background elements
    surface.blit(background_image_upscale, (0,0))
    surface.blit(background_image_chem_upscale, (0, 0))
    surface.blit(arrow_text_surface, arrow_text_box_centered)
    surface.blit(plus1_text_surface, plus1_text_box_position)
    surface.blit(plus2_text_surface, plus2_text_box_position)
    surface.blit(title_text_surface, title_text_box_centered)
    
    #create the text for the button
    text_surface = font_button.render('Submit', True, (21,20,30))

    #draw the button
    pygame.draw.rect(surface, (0, 0, 139), button_rect)

    #blit the text onto the button
    surface.blit(text_surface, (button_rect.x + (button_rect.width - text_surface.get_width()) // 2, button_rect.y + (button_rect.height - text_surface.get_height()) // 2))

    #check for events
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
                #if it doesnt already have a character in it make it uppercase
                if len(field_text[active_field]) == 0:
                    new_char = new_char.upper()
                #if it does have a character in it make it lowercase
                elif len(field_text[active_field]) == 1:
                    new_char = new_char.lower()

                # check if the field should only accept numbers e.g. subscript or coefficient
                if active_field in [0,2,4,5,7,9,10,12,14,15,17,19]:
                    #if the character is not a coefficient break out of this event loop, e.g. the user inputted is ingored in these fields if not a number
                    if not new_char.isdigit():

                        continue #break out of the event loop
                else:
                    #check if the character is a letter, if not break out of the event loop, e.g. the user inputted is ingored in these fields if not a letter 
                    if not new_char.isalpha():
                        continue

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
                # get the mouse positions e.g. x and y corrdinates for when it was clicked
                mouse_x, mouse_y = event.pos
                    # loop through the fields enumerated
                for i, (field_rect) in enumerate(field_rects):
                    if field_rect.collidepoint(mouse_x, mouse_y):
                        # set the active field to the one that was clicked on
                        active_field = i
                    if event.type == pygame.KEYDOWN:
                    # Ignore keypress events if the active field is not the current field
                        if active_field < len(guesses) * NUM_FIELDS:
                            continue

                        # Add the user's input and the result to the lists of previous guesses and results
                        guesses.append(user_input)
                        results.append(result)

                        # Clear the user's input
                        field_text = [''] * NUM_FIELDS * 2


    # Draw the previous rounds if any
    for i, guess in enumerate(guesses):
        result = results[i]
        for j, element in enumerate(guess):
            color = result[j]
            field_rect = pygame.Rect(j * (FIELD_WIDTH)+20, (surface_height - FIELD_HEIGHT) // 3.75 + i * (FIELD_HEIGHT + 10), FIELD_WIDTH+5, FIELD_HEIGHT+5)
            pygame.draw.rect(surface, color, field_rect, 2)
            text_surface = field_font.render(element, True, (0, 0, 0))
            surface.blit(text_surface, (field_rect.x + (field_rect.width - text_surface.get_width()) // 2, field_rect.y + (field_rect.height - text_surface.get_height()) // 2))

    # Draw the current guess
    for j, element in enumerate(field_text[:NUM_FIELDS]):
        field_rect = pygame.Rect(j * (FIELD_WIDTH)+20, (surface_height - FIELD_HEIGHT) // 3.75 + len(guesses) * (FIELD_HEIGHT + 10), FIELD_WIDTH+5, FIELD_HEIGHT+5)
        pygame.draw.rect(surface, (255, 255, 255), field_rect, 2)
        text_surface = field_font.render(element, True, (0, 0, 0))
        surface.blit(text_surface, (field_rect.x + (field_rect.width - text_surface.get_width()) // 2, field_rect.y + (field_rect.height - text_surface.get_height()) // 2))

    #initialize the list of field rectangles
    field_rects = []
    # Draw the input text fields
    # draw the text input fields with boarders
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
        field_rects.append(field_rect)

        #draw border around the field (with different colour for the active field)
        border_colour = active_field if i == active_field else white
        pygame.draw.rect(surface, border_colour, field_rect, 2)
        

        
        
        #create the non active borders in white since not active
        text_surface = field_font.render(text, True, white)

        text_surface = field_font.render(text, True, white)
        padding = 5 
        text_x = field_rect.x + padding
        text_y = field_rect.y + padding
        #if the field is a subscript field
        if i in [2,4,7,9,12,14,17,19]:
            #define a new smaller font to use for these subscript fields
            subscript_font = pygame.font.SysFont("times new roman", 36)
            text_surface = subscript_font.render(text, True, white)
            surface.blit(text_surface, (field_rect.x + 5, field_rect.y + 5))
        #add the text surface to the main surface
        else:
            surface.blit(text_surface, (text_x, text_y))



    # updates the surface
    pygame.display.flip()

    #frame limiting
    clock.tick(60)


