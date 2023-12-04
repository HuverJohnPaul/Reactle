
#Main document that runs the main functions of the game: Reactle
"""
Created on Sat Nov 25 17:47:22 2023

@authors: John-Paul Huver, Agnese, Feyi,Madeline
"""

#dictionary contating reactions
from database import reactions_database

#used to pic a random reaction
import random
#used to recognize normal text paterns
import re
#used to change the colour of text
from colorama import Fore, Back, Style
#used to center text in the terminal
import shutil
#variable to store the width of the terminal
terminal_columns = shutil.get_terminal_size().columns
def print_centered(text,end="\n"):
    """
    (str) -> print
    prints the text in the center of the terminal
    """
    #useful for debugging, checks if the text is a string if not raise an error stopping the program
    if type(text)!=str:
        raise TypeError("text must be a string for centered text function")
    #trim whitespace from the text
    text=text.strip()
    #remove coloured stuff(escape characters) when testing length as they do not effect the length of the text
    pattern=re.compile(r'\x1b[^m]*m')
    text_colourless=pattern.sub('', text)
    #get the length of the text
    text_length=len(text_colourless)
    #get the width of the terminal
    terminal_width=terminal_columns
    #calculate the number of spaces needed to center the text
    spaces_needed=int((terminal_width-text_length)/2)
    #print the spaces and then the text
    print(" "*spaces_needed+text,end=end)

def print_centered_multiline(text,end="\n"):
    """
    (str) -> print
    prints the text in the center of the terminal for each line of the text
    """
    #useful for debugging, checks if the text is a string if not raise an error stopping the program
    if type(text)!=str:
        raise TypeError("text must be a string for centered text multiline function")
    #trim whitespace from the text
    t=text.strip()
    #split the text into a list of lines based on the newline character
    lines=t.split("\n")
    #loop throught the list of the lines
    for i in range(len(lines)):
        #get the line
        l=lines[i]
        #remove the whitespace from the line
        l=l.strip()
        #remove coloured stuff(escape characters) when testing length as they do not effect the length of the text
        pattern=re.compile(r'\x1b[^m]*m')
        l_colourless=pattern.sub('', l)
        #get the length of the text
        text_length=len(l_colourless)
        #get the width of the terminal
        terminal_width=terminal_columns
        #calculate the number of spaces needed to center the text(slightly off center but looks better)
        spaces_needed=int((terminal_width-text_length-15)/2)

        #print the neccisarry spaces to center each line and then the text for that line
        #if it is the last line, print the end character
        if i==len(lines):
            #print the neccisarry spaces to center it and then the text
            print(" "*spaces_needed+l,end=end)
        #if it is not the last line, end charcter is default: \n, so it doesnt change the multiline string
        else:
            print(" "*spaces_needed+l)

def random_reaction():
    """
    () -> list
    returns a random reaction from the dictionary
    """
    #pick a random key from the dictionary eg. a random reaction
    return random.choice(list(reactions_database.rdict.keys()))

#print a welcome statement and ask for the user's name
print_centered("Welcome to Reactle!")

print("Reactle is a fascinating world-based game where you'll explore the realm of chemical reactions.")
print("Your mission is to decipher the atoms involved in a reaction by analyzing the spacings, coefficients, and subscripts.")
print("Each reaction presents a puzzle, and it's your job to figure out the elements of the reaction from the clues given by the spacinging and value of the coefficent, and subscirpts, as well as from the clues given as to if atoms are present in the reaction and where they are based off of the previouse guesses.")
print("your mission is to get the correct answer in the least amount of guesses possible.")


print_centered("Let's get started!")
#assign the user's name to a variable
print_centered("First please enter your name: ",end="")
name=input("")
#welcome the user by name
print_centered("welcome "+name+", let's begin.")

def random_reaction_str():
    #create a function equal to a random reaction from the dictionary
    reaction_list=(reactions_database.rdict[random_reaction()])

    #initialize the reaction answer string
    reaction_ans_str=""
    #loop through the reaction list and add each element to the reaction answer string with the proper formatting
    for l in reaction_list:
        a=reaction_list[l]
        #loop through the list inside this list
        for z in a:
            #add the element
            reaction_ans_str+=z
            #if z is not currenetly the last element in this list, add a plus sign
            if z!=reaction_list[l][-1]:
                reaction_ans_str+=" + "
        #if l is not the products list, add a reaction arrow
        if reaction_list[l]!=reaction_list["products"]:
            reaction_ans_str+=" → "
    return reaction_ans_str

def subed(str_to_sub):
    #dictionary of subscripted numbers with the normal number as the key and the subscripted number as the value
    sub_dict={"0":"₀","1":"₁","2":"₂","3":"₃","4":"₄","5":"₅","6":"₆","7":"₇","8":"₈","9":"₉"}
    #loop through the string to be subed
    for l in str_to_sub:
        #if the character is a number, replace it with the subscripted version
        if l.isdigit():
            str_to_sub=str_to_sub.replace(l,sub_dict[l])
    #return the subed string
    return str_to_sub
def cencoured_reaction(reaction_str):
    #initialize the cencoured reaction string
    cencoured_reaction_str=""
    #initialize the atom number counter at 1 so the first element is 1
    atom_num=1
    #initialize the a blank list for the atom answer list
    atom_answer_list=[]
    l_historical=""
    #loop through the reaction string
    for i in range(len(reaction_str)):
        l=reaction_str[i]
        #if the character is a lower case letter, skip it as lower case letters are delt with in the upper case letter section
        if l.islower():
            continue
        #if the character is a capital letter, add a box made from [] to represent an unknown atom with a labling number in the middle and check if the next is apart of the atom by seeing if it is a lower case letter
        elif l.isupper():
            if i+1<len(reaction_str) and reaction_str[i+1].islower():
                if len(atom_answer_list)==0:
                    cencoured_reaction_str+="["+str(atom_num)+"]"
                    atom_answer_list.append([atom_num,l+reaction_str[i+1]])
                    atom_num+=1
                    sub_flag=0
                else:
                    for x in atom_answer_list:
                        if x[1]==(l+reaction_str[i+1]):
                            cencoured_reaction_str+="["+str(x[0])+"]"
                            sub_flag=0
                            break
                    else:
                        cencoured_reaction_str+="["+str(atom_num)+"]"
                        atom_answer_list.append([atom_num,l+reaction_str[i+1]])
                        atom_num+=1
                        sub_flag=0
            else:
                if len(atom_answer_list)==0:
                    cencoured_reaction_str+="["+str(atom_num)+"]"
                    atom_answer_list.append([atom_num,l])
                    atom_num+=1
                    sub_flag=0
                else:
                    for x in atom_answer_list:
                        if x[1]==l:
                            cencoured_reaction_str+="["+str(x[0])+"]"
                            sub_flag=0
                            break
                    else:
                        cencoured_reaction_str+="["+str(atom_num)+"]"
                        atom_answer_list.append([atom_num,l])
                        atom_num+=1
                        sub_flag=0
        #if the character is a plus sign, add a plus sign
        elif l=="+":
            cencoured_reaction_str+="+"
            sub_flag=0
        #if the character is a reaction arrow, add a reaction arrow
        elif l=="→":
            cencoured_reaction_str+="→"
            sub_flag=0
        #if the character is a space, add a space
        elif l=="(":
            cencoured_reaction_str+="("
            sub_flag=0
        elif l==")":
            cencoured_reaction_str+=")"
            sub_flag=0
        elif l==" ":
            cencoured_reaction_str+=" "
            sub_flag=0
        elif l.isdigit():
            if l_historical==" " or (l_historical.isdigit() and sub_flag!=1) or l==reaction_str[0]:
                cencoured_reaction_str+=l
            else:
                cencoured_reaction_str+=subed(l)
                sub_flag=1
        l_historical=l
    #return the cencoured reaction string

    return (cencoured_reaction_str,atom_answer_list)

# a module that will allow parsing of the csv file 
import pandas as pd
#a module that will allow the program to use regular expressions, helps with string parsing
import re
def is_valid_atom(atom_str):
    """
    str -> bool
    checks if the atom string is a valid atom of the form of sybmol (case sensitive) or name (case insensitive for the first letter)
    """
    #columns needed from the periodic table csv file
    needed_columns=["Atomic Number","Atomic Symbol","Name"]
    #read the periodic table csv file and only use the needed columns
    elemnetdata=pd.read_csv("periodictable.csv",usecols=needed_columns)
    #check if the atom string is parsable string, if it is not return false
    if atom_str == None or atom_str == "" or type(atom_str)!=str:
        return False
    #check if the atom string is a valid atom of the form of sybmol or name, if it is return true
    if atom_str in elemnetdata["Atomic Symbol"].values or atom_str in elemnetdata["Name"].values or str(atom_str[0].upper()+atom_str[1:]) in elemnetdata["Name"].values:
        #if the atom string is a valid atom, return true
        return True
    else:
        #if the atom string is not a valid atom, return false
        return False

def guess_converter(guess_str):
    """
    str -> str
    converts the guess string to the proper form of the atom
    eg. converts the name to the symbol if the name is given
    if the guess string is not a valid atom, return None
    """
    #check if the guess string is a valid atom, if it is not return None
    if is_valid_atom(guess_str) == False:
        return None
    #columns needed from the periodic table csv file
    needed_columns=["Atomic Number","Atomic Symbol","Name"]
    #read the periodic table csv file and only use the needed columns
    elemnetdata=pd.read_csv("periodictable.csv",usecols=needed_columns)
    #check if the guess string is an atomic symbol, if it is return the guess string
    if guess_str in elemnetdata["Atomic Symbol"].values:
        return guess_str
    #check if the guess string is a name, if it is return the atomic symbol corsponding to the name
    elif guess_str[0].upper()+guess_str[1:] in elemnetdata["Name"].values:
        return elemnetdata[elemnetdata["Name"]==guess_str[0].upper()+guess_str[1:]]["Atomic Symbol"].values[0]



def coloured_reaction(reaction_str,guess_list,previous_guesses):
    cencoured=cencoured_reaction(reaction_str)[0]
    ans=cencoured_reaction(reaction_str)[1]
    print(ans)
    print(guess_list)
    print(previous_guesses)
    print(cencoured)

    periodic="""
      H                                                  He
      Li Be                               B  C  N  O  F  Ne
      Na Mg                               Al Si P  S  Cl Ar
      K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
      Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
      Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
      Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og
 
            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr
            """
    coloured_guess_result=""
    #loop through the range of the length of the answer list
    for i in range(len(ans)):
        #x is the current element in the answer list
        x=ans[i]

        #correct guess/green
        if x[1] in guess_list[i]:
            cencoured=cencoured.replace("["+str(x[0])+"]",Style.BRIGHT+Fore.GREEN+"["+str(x[0])+"]"+Style.RESET_ALL)
            periodic=periodic.replace(" "+str(x[1])+" ",Style.BRIGHT+Fore.GREEN+" "+str(x[1])+Style.RESET_ALL+" ")
            coloured_guess_result+="["+str(x[0])+"] = "+Style.BRIGHT+Fore.GREEN+str(guess_list[i])+Style.RESET_ALL+"   CORRECT \n"
            if x[1] in previous_guesses:
                if previous_guesses[x[1]]=="R":
                    periodic=periodic.replace(" "+str(x[1])+" "," "+Back.RED+Style.BRIGHT+Fore.GREEN+str(x[1])+Style.RESET_ALL+" ")
                if previous_guesses[x[1]]=="Y":
                    periodic=periodic.replace(" "+str(x[1])+" "," "+Back.YELLOW+Style.BRIGHT+Fore.GREEN+str(x[1])+Style.RESET_ALL+" ")
                if previous_guesses[x[1]]=="G":
                    periodic=periodic.replace(" "+str(x[1])+" "," "+Back.GREEN+Style.BRIGHT+Fore.GREEN+str(x[1])+Style.RESET_ALL+" ")
            else:
                previous_guesses[x[1]]="G"
            #if the guess is correct, skip the rest of the loop for this element
            continue

        #wrong spot/yellow
        #if the guess is in the answer list but not in the right spot
        #does this by in line looping through the answer list and checking if the guess is in the answer list but not in the right spot
        if guest_list[i] in a[1] for a in ans and guess_list[i]!=x[1]:
            print("yellow here")
            #replace the the wrong guess in the cencoured reaction string with yellow
            cencoured=cencoured.replace("["+str(x[0])+"]",Style.BRIGHT+Fore.YELLOW+"["+str(x[0])+"]"+Style.RESET_ALL)
            #replace the wrong guess in the periodic table with yellow
            periodic=periodic.replace(" "+str(x[1])+" ",Style.BRIGHT+Fore.YELLOW+" "+str(x[1])+Style.RESET_ALL+" ")
            #add the wrong guess to the coloured guess result
            coloured_guess_result+="["+str(x[0])+"] = "+Style.BRIGHT+Fore.YELLOW+str(guess_list[i])+Style.RESET_ALL+"     WRONG SPOT \n"
            #if the wrong guess is in the previous guesses, replace the background colour in the periodic table with what it was before
            if x[1] in previous_guesses:
                #replace the background colour with what it was before
                if previous_guesses[x[1]]=="R":
                    periodic=periodic.replace(" "+str(x[1])+" "," "+Back.RED+Style.BRIGHT+Fore.YELLOW+str(x[1])+Style.RESET_ALL+" ")
                elif previous_guesses[x[1]]=="Y":
                    periodic=periodic.replace(" "+str(x[1])+" "," "+Back.YELLOW+Style.BRIGHT+Fore.YELLOW+str(x[1])+Style.RESET_ALL+" ")
                elif previous_guesses[x[1]]=="G":
                    periodic=periodic.replace(" "+str(x[1])+" "," "+Back.GREEN+Style.BRIGHT+Fore.YELLOW+str(x[1])+Style.RESET_ALL+" ")
                #since background colour is best guess, only replace if worse guess, eg. if the guess is red, replace it otherwise it is yellow or green so better or equal guess so dont change it in the dictionary
                if previous_guesses[x[1]]=="R":
                    previous_guesses[x[1]]="Y"
            else:
                #if it is not in the previous guesses, add it to the previous guesses as yellow
                previous_guesses[x[1]]="Y"
            #once the guess is found in the answer list, if it is in it and not the right spot no need to go through the rest of the answer list so break our of this inner for loop 
            break
            #if the guess is correct, skip the rest of the loop for this element
            continue
        #incorret guess/red
        else:
            #replace the the wrong guess in the cencoured reaction string with red
            cencoured=cencoured.replace("["+str(x[0])+"]",Style.BRIGHT+Fore.RED+"["+str(x[0])+"]"+Style.RESET_ALL)
            #replace the wrong guess in the periodic table with red
            periodic=periodic.replace(" "+str(guess_list[i])+" "," "+Style.BRIGHT+Fore.RED+str(guess_list[i])+Style.RESET_ALL+" ")
            #add the wrong guess to the coloured guess result
            coloured_guess_result+="["+str(x[0])+"] = "+Style.BRIGHT+Fore.RED+str(guess_list[i])+Style.RESET_ALL+"     INCORRECT \n"
            #if the wrong guess is in the previous guesses, replace it with red background
            if guess_list[i] in previous_guesses:
                periodic=periodic.replace(" "+str(guess_list[i])+" "," "+Back.RED+str(guess_list[i])+Style.RESET_ALL+" ")
            else:
                previous_guesses[guess_list[i]]="R"
    #loop through keys and values of the previous guesses and add them to the periodic table if they are not in the current guess list
    for g,v in previous_guesses.items():
        #skips current guesses so it doesnt overwrite them
        if g in guess_list:
            continue

        else:
            #if the guess was red replace it with red background
            if v=="R":
                periodic=periodic.replace(" "+str(g)+" ",Back.RED+" "+str(g)+Style.RESET_ALL+" ")
            #if the guess was yellow replace it with yellow background
            if v=="Y":
                periodic=periodic.replace(" "+str(g)+" ",Back.YELLOW+" "+str(g)+Style.RESET_ALL+" ")
            #if the guess was green replace it with green background
            if v=="G":
                periodic=periodic.replace(" "+str(g)+" ",Back.GREEN+" "+str(g)+Style.RESET_ALL+" ")

    #add a title for the periodic table
    periodic_table_coloured="\t\t\tPeriodic Table\n"+periodic+"\n"
    #return the coloured reaction string, the coloured periodic table, the coloured guess result, and the previous guesses
    return (cencoured,periodic_table_coloured,coloured_guess_result,previous_guesses)


print("\n"*2)
print_centered("Here is your reaction:")
reaction_ans_str=random_reaction_str()
reaction=cencoured_reaction(reaction_ans_str)


print_centered(reaction[0])
print_centered("Enter your guesses for the atoms below")

print(reaction_ans_str)
running=True
guessnumber=0
previous_guesses={}
while running:
    index=0
    #whipeout/initalize the guess list (after the first time removes everything in it and begins fresh)
    guess_list=[]
    while index<len(reaction[1]):
        print_centered("["+str(reaction[1][index][0])+"] = ",end="")
        guess=input("")
        if is_valid_atom(guess):
            guess_list.append(guess)
            index+=1
        else:
            print_centered("Invalid atom guess, make sure that the first letter is capitalized and if there is a second it is lowercase.")
            print_centered("Try again")
    guessnumber+=1
    print("\n"*5)
    response=coloured_reaction(reaction_ans_str,guess_list,previous_guesses)
    print_centered("Guess:"+str(guessnumber))
    print_centered_multiline(response[1])
    print_centered_multiline(response[2])
    print_centered(reaction[0])
    print_centered("Sorry not right, try again.")
    print_centered("hint: the green atoms are correct, the yellow are in the reaction but not the right spot, and the red atoms are incorrect.")
    print_centered("on the periodic table the background colour represents the best past guess for that atom")
    print("\n"*2)
        
