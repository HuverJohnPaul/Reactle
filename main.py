
#Main document that runs the main functions of the game: Reactle
"""
Created on Sat Nov 25 17:47:22 2023

@authors: John-Paul Huver, Agnese, Feyi,Madeline
"""
#JP--used to navigate directories
import os
#dictionary contating reactions
from database import reactions_database

#used to pic a random reaction
import random
def random_reaction():
    #pick a random key from the dictionary eg. a random reaction
    return random.choice(list(reactions_database.rdict.keys()))

#print a welcome statement and ask for the user's name
print("Welcome to Reactle!")

print("Reactle is a fascinating world-based game where you'll explore the realm of chemical reactions.")
print("Your mission is to decipher the atoms involved in a reaction by analyzing the spacings, coefficients, and subscripts.")
print("Each reaction presents a puzzle, and it's your job to figure out the elements of the reaction from the clues given by the spacinging and value of the coefficent, and subscirpts, as well as from the clues given as to if atoms are present in the reaction and where they are based off of the previouse guesses.")
print("your mission is to get the correct answer in the least amount of guesses possible.")


print("Let's get started!")
name=input("First please enter your name: ")

print("Hello"+name+"! Let's begin!")


reaction_list=(reactions_database.rdict[random_reaction()])
