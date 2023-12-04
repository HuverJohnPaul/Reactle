
#Main document that runs the main functions of the game: Reactle
"""
Created on Sat Nov 25 17:47:22 2023

@authors: John-Paul Huver, Agnese, Feyi ,Madeline
"""

#dictionary contating reactions
from database import reactions_database

#used to pic a random reaction
import random
#used to recognize normal text paterns
import re
#used to change the colour of text
from colorama import Fore, Back, Style, init
#initialize colorama
init()
#used to center text in the terminal
import shutil
# a module that will allow parsing of the csv file 
import pandas as pd
def print_centered(text,end="\n"):
    """
    (str) -> print
    prints the text in the center of the terminal
    """
    #get the width of the terminal
    terminal_columns = shutil.get_terminal_size().columns
    #useful for debugging, checks if the text is a string if not raise an error stopping the program
    if type(text)!=str:
        raise TypeError("text must be a string for centered text function")
    #trim whitespace from the text
    text=text.lstrip()
    #remove coloured stuff(escape characters) when testing length as they do not effect the length of the text
    #eg. \x1b[31m is a red colour escape character that is used by colorama so use the re module to easily remove anything of this style
    pattern=re.compile(r'\x1b[^m]*m')
    pattern_2=re.compile(r'\033[^m]*m')
    #replace the coloured stuff with nothing
    text_colourless=pattern.sub('', text)
    text_colourless=pattern_2.sub('', text_colourless)
    #get the length of the text
    text_length=len(text_colourless)
    #get the width of the terminal
    terminal_width=terminal_columns
    #get the text with spaces on both sides to center it
    centered_text=text_colourless.center(terminal_width)
    #initialize the left side padding as a blank string
    centre_text_left_side_padding=""
    #loop through the centered text
    for i in range(len(centered_text)):
        #if the character is a space, add it to the left side padding
        if centered_text[i]==" ":
            centre_text_left_side_padding+=" "
            #continue to the next character
            continue
        #if the character is not a space, break the loop
        else:
            break
    #print the spaces needed to center the text then the text then the end character
    text_left_side_stripped=text.lstrip()
    print(centre_text_left_side_padding+text_left_side_stripped,end=end)

def print_centered_multiline(text,end="\n"):
    """
    (str) -> print
    prints the text in the center of the terminal for each line of the text
    """
    #get the width of the terminal
    terminal_columns = shutil.get_terminal_size().columns
    #useful for debugging, checks if the text is a string if not raise an error stopping the program
    if type(text)!=str:
        raise TypeError("text must be a string for centered text multiline function")
    #trim whitespace from the text
    t=text.lstrip()
    #split the text into a list of lines based on the newline character
    lines=t.split("\n")
    #loop throught the list of the lines
    for i in range(len(lines)):
        #get the line
        l=lines[i]
        #remove the whitespace from the line
        l=l.lstrip()
        #remove coloured stuff(escape characters) when testing length as they do not effect the length of the text
        pattern=re.compile(r'\x1b[^m]*m')
        l_colourless=pattern.sub('', l)
        pattern_2=re.compile(r'\033[^m]*m')
        l_colourless=pattern_2.sub('', l_colourless)
        #get the length of the text
        text_length=len(l_colourless)
        #get the width of the terminal
        terminal_width=terminal_columns
                #get the text with spaces on both sides to center it
        centered_text=l_colourless.center(terminal_width)
        #initialize the left side padding as a blank string
        centre_text_left_side_padding=""
        #loop through the centered text
        for i in range(len(centered_text)):
            #if the character is a space, add it to the left side padding
            if centered_text[i]==" ":
                centre_text_left_side_padding+=" "
                #continue to the next character
                continue
            #if the character is not a space, break the loop
            else:
                break

        #if it is the last line, print the end character
        if i==len(lines):
            #print the text left side stripped so as to not double pad, with the left side padding and the end character
            left_side_stripped_text=l.lstrip()
            print(centre_text_left_side_padding+left_side_stripped_text,end=end)
        #if it is not the last line print the text centered then a newline character as normal to make it properly multiline
        else:
            left_side_stripped_text=l.lstrip()
            print(centre_text_left_side_padding+left_side_stripped_text)

def random_reaction():
    """
    () -> list
    returns a random reaction from the dictionary 
    """
    #pick a random key from the dictionary eg. a random reaction
    return random.choice(list(reactions_database.rdict.keys()))

#print a welcome statement and ask for the user's name
print_centered("Welcome to Reactle! 🔎 ⚛︎")

print_centered("Your mission is to decipher the atoms involved in a reaction by analyzing the spacings, coefficients, and subscripts.")
print_centered("After each guess, you will be given a hint as to whether your guess was correct, in the wrong spot, or incorrect.")
print_centered("your mission is to get the correct answer in the least amount of guesses possible.")


print_centered("Let's get started!")
#assign the user's name to a variable
print_centered("First please enter your name: ",end="")
name=input("")
#welcome the user by name
print_centered("welcome "+name+", let's begin.")

def random_reaction_str():
    """
    () -> str
    returns a random reaction string from the dictionary
    """
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
    """
    Agnese
    str -> str
    returns a string with the numbers in the string subbed with subscripted numbers
    """
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
    """
    JP/AL
    str -> (str,list)
    returns the cencoured reaction string and the answer list
    the cencoured reaction string is the reaction string with the atoms replaced with numbers in boxes
    the answer list is a list of lists containing the number and the atom for each atom in the reaction string, ordered by the order they appear in the reaction string
    
    example:
    reaction_str="2H2 + O2 → 2H2O"
    cencoured_reaction(reaction_str) -> ("2[1]₂ + [2]₂ → 2[1]₂[2]",[[1,"H"],[2,"O"]])

    JP- I wrote the function and Agnese helped me debug it and make it more efficient
    yes I now know how to spell censored and know how to replace, but its too iconic to change
    """
    #initialize the cencoured reaction string as a blank string in bright style
    cencoured_reaction_str=""+Style.BRIGHT+""+Style.RESET_ALL
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
        #if the character is a capital letter, add a box made from [] to represent an unknown atom with a labling number in the middle and check if the next characters is a part of this atom by seeing if it is a lower case letter
        elif l.isupper():
            #if adding one to i wont cause an index error and the next character is a lower case letter
            if i+1<len(reaction_str) and reaction_str[i+1].islower():
                #if the atom answer list is empty, directly add the atom to the cencoured reaction string with the atom number as we dont need to check if this atom has been used before
                if len(atom_answer_list)==0:
                    cencoured_reaction_str+="["+str(atom_num)+"]"
                    atom_answer_list.append([atom_num,l+reaction_str[i+1]])
                    #add one to the atom number counter
                    atom_num+=1
                    #lower sub flag back to 0 if it was raised in the previous loop
                    sub_flag=0
                #if the atom answer list is not empty, check if the atom has been used before, if it has, censore it with the atom number already in the atom answer list
                else:
                    #loop through the atom answer list
                    for x in atom_answer_list:
                        #if the atom has been used before, censore it with the atom number already in the atom answer list
                        if x[1]==(l+reaction_str[i+1]):
                            cencoured_reaction_str+="["+str(x[0])+"]"
                            #lower sub flag back to 0 if it was raised in the previous loop
                            sub_flag=0
                            #break the for loop as we have found the atom in the atom answer list
                            break
                    #if the atom has not been used before, add it to the cencoured reaction string with a new atom number and add it to the atom answer list
                    else:
                        cencoured_reaction_str+="["+str(atom_num)+"]"
                        #add the atom to the atom answer list
                        atom_answer_list.append([atom_num,l+reaction_str[i+1]])
                        #add one to the atom number counter
                        atom_num+=1
                        #lower sub flag back to 0 if it was raised in the previous loop
                        sub_flag=0
            #if the next character is not a lower case letter
            else:
                #if the atom answer list is empty, directly add the atom to the cencoured reaction string with the atom number as we dont need to check if this atom has been used before
                if len(atom_answer_list)==0:
                    cencoured_reaction_str+="["+str(atom_num)+"]"
                    atom_answer_list.append([atom_num,l])
                    #add one to the atom number counter
                    atom_num+=1
                    #lower sub flag back to 0 if it was raised in the previous loop
                    sub_flag=0
                #if the atom answer list is not empty
                else:
                    #loop through the atom answer list
                    for x in atom_answer_list:
                        #if the atom has been used before, censore it with the atom number already in the atom answer list
                        if x[1]==l:
                            cencoured_reaction_str+="["+str(x[0])+"]"
                            #lower sub flag back to 0 if it was raised in the previous loop
                            sub_flag=0
                            #break the for loop as we have found the atom in the atom answer list
                            break
                    #if the atom has not been used before, add it to the cencoured reaction string with a new atom number and add it to the atom answer list
                    else:
                        #add the atom to the cencoured reaction string
                        cencoured_reaction_str+="["+str(atom_num)+"]"
                        #add the atom to the atom answer list
                        atom_answer_list.append([atom_num,l])
                        #add one to the atom number counter
                        atom_num+=1
                        #lower sub flag back to 0 if it was raised in the previous loop
                        sub_flag=0
        #if the character is a special character, add it to the cencoured reaction string as is and lower the sub flag
        elif l=="+":
            cencoured_reaction_str+="+"
            sub_flag=0
        elif l=="→":
            cencoured_reaction_str+="→"
            sub_flag=0
        elif l=="(":
            cencoured_reaction_str+="("
            sub_flag=0
        elif l==")":
            cencoured_reaction_str+=")"
            sub_flag=0
        elif l==" ":
            cencoured_reaction_str+=" "
            sub_flag=0
        #if the character is a number
        elif l.isdigit():
            #if the previous character was a number, space, or the first character, add it to the cencoured reaction string as is
            #if the sub flag is raised goto the else statement
            if l_historical==" " or (l_historical.isdigit() and sub_flag!=1) or l==reaction_str[0]:
                cencoured_reaction_str+=l
            #add the number to the cencoured reaction string as a subscripted number and raise the sub flag
            else:
                cencoured_reaction_str+=subed(l)
                sub_flag=1
        #add the character to the historical variable
        l_historical=l
    #return the cencoured reaction string and the atom answer list as a tuple
    return (cencoured_reaction_str,atom_answer_list)


def is_valid_atom(atom_str):
    """
    Jp
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
    JP
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
    """
    JP
    str,list,dict -> str,str,str,dict
    returns the coloured reaction string, the coloured periodic table, the coloured guess result, and the previous guesses
    reaction_str is the reaction string to be coloured-> is outputted as the reaction string coloured
    guess_list is the list of current guesses for the reaction string it is used to determine the colour of the reaction string and other elements
    previous_guesses is a dictionary of the previous guesses and their colours
        - red=R, yellow=Y, green=G
    for the periodic table, the background colour represents the best past guess for that atom if there is one, if the user guesses in the same spot the background colour will remain as the previous best guess
    the current guesses in the periodic table are underlined and bolded to make them stand out and make it easier to see what the user has guessed
    this underlining and bolding is easpecially useful for when the user guesses in the same spot as a previous guess as it makes it easier to see what the user has guessed

    """
    #get the cencoured reaction string and the answer list from the cencoured reaction function
    cencoured=cencoured_reaction(reaction_str)[0]
    ans=cencoured_reaction(reaction_str)[1]
    #initialize the periodic table string
    periodic="""
       █ H                                                  He █
       █ Li Be                               B  C  N  O  F  Ne █
       █ Na Mg                               Al Si P  S  Cl Ar █
       █ K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr █
       █ Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe █
       █ Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn █
       █ Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og █
 
            █ Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu █
            █ Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr █
            """
    #initialize the coloured guess result as a blank string
    coloured_guess_result=""
    #initialize the current guesses as a blank dictionary
    current_guesses={}
    #loop through the range of the length of the answer list
    for i in range(len(ans)):
        #x is the current element in the answer list
        x=ans[i]
        #correct guess/green
        #if the guess is in the answer list and in the right spot
        if x[1] in guess_list[i]:
            #replace the the correct guess in the cencoured reaction string with green
            cencoured=cencoured.replace("["+str(x[0])+"]",Style.BRIGHT+Fore.GREEN+"["+str(x[0])+"]"+Style.RESET_ALL)
            #replace the correct guess in the periodic table with green text
            periodic=periodic.replace(" "+str(x[1])+" "," "+Style.RESET_ALL+"\033[m"+""+Style.BRIGHT+"\033[1m"+"\033[4m"+Fore.GREEN+str(x[1])+Style.RESET_ALL+"\033[m"+" ")
            #add the correct guess to the coloured guess result
            coloured_guess_result+="["+str(x[0])+"] = "+Style.BRIGHT+Fore.GREEN+str(guess_list[i])+Style.RESET_ALL+"   CORRECT \n"
            #if the guess is in the previous guesses, replace the background colour in the periodic table with what it was before
            if guess_list[i] in previous_guesses:
                if previous_guesses[guess_list[i]]=="R":
                    periodic=periodic.replace(" "+Style.RESET_ALL+"\033[m"+""+Style.BRIGHT+"\033[1m"+"\033[4m"+Fore.GREEN+str(x[1])+Style.RESET_ALL+"\033[m"+" "," "+Style.RESET_ALL+"\033[m"+""+Back.RED+Style.BRIGHT+"\033[1m"+"\033[4m"+Fore.GREEN+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" ")
                if previous_guesses[guess_list[i]]=="Y":
                    periodic=periodic.replace(" "+Style.RESET_ALL+"\033[m"+""+Style.BRIGHT+"\033[1m"+"\033[4m"+Fore.GREEN+str(x[1])+Style.RESET_ALL+"\033[m"+" "," "+Style.RESET_ALL+"\033[m"+""+Back.YELLOW+Style.BRIGHT+"\033[1m"+'\033[4m'+Fore.GREEN+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" ")
                if previous_guesses[guess_list[i]]=="G":
                    periodic=periodic.replace(" "+Style.RESET_ALL+"\033[m"+""+Style.BRIGHT+"\033[1m"+"\033[4m"+Fore.GREEN+str(x[1])+Style.RESET_ALL+"\033[m"+" "," "+Style.RESET_ALL+"\033[m"+""+Back.GREEN+Style.BRIGHT+"\033[1m"+'\033[4m'+Fore.GREEN+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" ")
                #since background colour represents the best colour replace it always with green
                previous_guesses[guess_list[i]]="G"
            #if the guess is not in the previous guesses, add it to the previous guesses as green
            else:
                current_guesses[x[1]]="G"
            #if the guess is correct, skip the rest of the loop for this element
            continue

        #wrong spot/yellow
        #if the guess is in the answer list but not in the right spot
        #does this by in line looping through the answer list and checking if the guess is in the answer list but not in the right spot
        elif any(guess_list[i] in a for a in ans) and guess_list[i]!=x[1]:
            #replace the the wrong guess in the cencoured reaction string with yellow
            cencoured=cencoured.replace("["+str(x[0])+"]",Style.BRIGHT+Fore.YELLOW+"["+str(x[0])+"]"+Style.RESET_ALL+"\033[m")
            #replace the wrong guess in the periodic table with yellow
            periodic=periodic.replace(" "+str(guess_list[i])+" "," "+Style.RESET_ALL+"\033[m"+Style.BRIGHT+""+"\033[1m"+"\033[4m"+Fore.YELLOW+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" ")
            #add the wrong guess to the coloured guess result
            coloured_guess_result+="["+str(x[0])+"] = "+Style.BRIGHT+Fore.YELLOW+str(guess_list[i])+Style.RESET_ALL+"     WRONG SPOT \n"
            #if the wrong guess is in the previous guesses, replace the background colour in the periodic table with what it was before
            if guess_list[i] in previous_guesses:
                #replace the background colour with previous guess colour but keep the text the same for this guess
                if previous_guesses[guess_list[i]]=="R":
                    periodic=periodic.replace(" "+Style.RESET_ALL+"\033[m"+Style.BRIGHT+""+"\033[1m"+"\033[4m"+Fore.YELLOW+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" "," "+Style.RESET_ALL+"\033[m"+""+Back.RED+Style.BRIGHT+"\033[1m"+'\033[4m'+Fore.YELLOW+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" ")
                elif previous_guesses[guess_list[i]]=="Y":
                    periodic=periodic.replace(" "+Style.RESET_ALL+"\033[m"+Style.BRIGHT+""+"\033[1m"+"\033[4m"+Fore.YELLOW+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" "," "+Style.RESET_ALL+"\033[m"+"\033[m"+""+Back.YELLOW+Style.BRIGHT+"\033[1m"+"\033[4m"+Fore.YELLOW+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" ")
                elif previous_guesses[guess_list[i]]=="G":
                    periodic=periodic.replace(" "+Style.RESET_ALL+"\033[m"+Style.BRIGHT+""+"\033[1m"+"\033[4m"+Fore.YELLOW+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" "," "+Style.RESET_ALL+"\033[m"+""+Back.GREEN+Style.BRIGHT+"\033[1m"+'\033[4m'+Fore.YELLOW+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" ")
                #since background colour is best guess, only replace if worse guess, eg. if the guess is red, replace it otherwise it is yellow or green so better or equal guess so dont change it in the dictionary
                if previous_guesses[guess_list[i]]=="R":
                    previous_guesses[guess_list[i]]="Y"
            else:
                #if it is not in the previous guesses, add it to the previous guesses as yellow
                current_guesses[guess_list[i]]="Y"
            #if the guess is correct, skip the rest of the loop for this element
            continue

        #incorret guess/red
        else:
            #replace the the wrong guess in the cencoured reaction string with red
            cencoured=cencoured.replace("["+str(x[0])+"]",Style.BRIGHT+Fore.RED+"["+str(x[0])+"]"+Style.RESET_ALL)
            #replace the wrong guess in the periodic table with red
            periodic=periodic.replace(" "+str(guess_list[i])+" "," "+Style.RESET_ALL+"\033[0m"+""+Style.BRIGHT+"\033[1m"+'\033[4m'+Fore.RED+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" ")
            #add the wrong guess to the coloured guess result
            coloured_guess_result+="["+str(x[0])+"] = "+Style.BRIGHT+Fore.RED+str(guess_list[i])+Style.RESET_ALL+"     INCORRECT \n"
            #if the wrong guess is in the previous guesses, replace it with red background
            if guess_list[i] in previous_guesses:
                if previous_guesses[guess_list[i]]=="R":
                    periodic=periodic.replace(" "+Style.RESET_ALL+"\033[0m"+""+Style.BRIGHT+"\033[1m"+'\033[4m'+Fore.RED+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" "," "+Style.RESET_ALL+"\033[m"+""+Back.RED+Style.BRIGHT+"\033[1m"+'\033[4m'+Fore.RED+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" ")
                elif previous_guesses[guess_list[i]]=="Y":
                    periodic=periodic.replace(" "+Style.RESET_ALL+"\033[0m"+""+Style.BRIGHT+"\033[1m"+'\033[4m'+Fore.RED+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" "," "+Style.RESET_ALL+"\033[m"+""+Back.YELLOW+Style.BRIGHT+"\033[1m"+'\033[4m'+Fore.RED+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" ")
                elif previous_guesses[guess_list[i]]=="G":
                    periodic=periodic.replace(" "+Style.RESET_ALL+"\033[0m"+""+Style.BRIGHT+"\033[1m"+'\033[4m'+Fore.RED+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" "+" "," "+Style.RESET_ALL+"\033[m"+""+Back.GREEN+Style.BRIGHT+"\033[1m"+'\033[4m'+Fore.RED+str(guess_list[i])+Style.RESET_ALL+"\033[0m"+" ")
                #since background colour is best guess, never replace it with red if already red since it is the worst guess

            #if the guess is not in the previous guesses, add it to the previous guesses as red
            else:
                current_guesses[guess_list[i]]="R"

    #update the previous guesses with the current guesses
    previous_guesses.update(current_guesses)

    #loop through keys and values of the previous guesses and add them to the periodic table if they are not in the current guess list
    for g,v in previous_guesses.items():
        #skips current guesses so it doesnt overwrite them
        if g in guess_list:
            continue

        else:
            #if the guess was red replace it with red background
            if v=="R":
                periodic=periodic.replace(" "+str(g)+" "," "+Style.RESET_ALL+""+Back.RED+str(g)+Style.RESET_ALL+" ")
            #if the guess was yellow replace it with yellow background
            if v=="Y":
                periodic=periodic.replace(" "+str(g)+" "," "+Style.RESET_ALL+""+Back.YELLOW+str(g)+Style.RESET_ALL+" ")
            #if the guess was green replace it with green background
            if v=="G":
                periodic=periodic.replace(" "+str(g)+" "," "+Style.RESET_ALL+""+Back.GREEN+str(g)+Style.RESET_ALL+" ")

    #add a title for the periodic table
    periodic_table_coloured="\t\t\tPeriodic Table\n"+periodic+"\n"
    #return the coloured reaction string, the coloured periodic table, the coloured guess result, and the previous guesses
    return (cencoured,periodic_table_coloured,coloured_guess_result,previous_guesses)


def check_guess(guess_list,ans_list):
    """
    JP
    list,list -> bool
    checks if the guess list is the same as the answer list
    """
    #loop through the guess list and check if each element is in the answer list
    for i in range(len(guess_list)):
        #if the element is not in the answer list, in the right spot, return false
        if guess_list[i]!=ans_list[i][1]:
            return False
    #if all the elements are in the answer list, return true
    return True

#text and instructions for the user and actual game was primarily written by Feyi, Madeline, and Agnese
print("\n"*2)
#initialize the play again variable
play_again="y"
#initialize the games played variable
games_played=0
#loop through the game till the user does not want to play again
while play_again!="n":
    #print starting greetings
    print("\n"*2)
    print_centered("⚗️"+"  Get ready to play Reactle!"+"🧪")
    if games_played!=0:
        print_centered("You have played "+str(games_played)+" games so far!")
    print_centered("You have 6 guesses to figure out all of the atoms in the reaction in the right places.")
    print_centered("You will be given hints after each guess to help you figure out the correct answer.")
    print_centered("Good luck "+name+"!")
    print_centered("Here is your reaction:")
    reaction_ans_str=random_reaction_str()
    reaction=cencoured_reaction(reaction_ans_str)
    
    #print the censored reaction string the player will be guessing
    print_centered(reaction[0])
    print_centered("Enter your guesses for the atoms below")
    #initialize running as true
    running=True
    #initialize the guess number as 0
    guessnumber=0
    #initialize the guess list as a blank dictionary
    previous_guesses={}
    #loop through the game till running is false
    while running:
        #if the user used all their guesses and did not get the reaction right
        if guessnumber==6:
            #print the game lost type stuff
            print_centered("good try, but you ran out of guesses")
            print_centered("the answer was:")
            #tell the user the answer
            print_centered(reaction_ans_str)
            #ask the user if they want to play again
            print_centered("would you like to play again? (y/n)",end="")
            #initialize the play again variable/whipe it if it was used before
            play_again=input("")
            games_played+=1
            #wait for the user to enter a valid input
            while play_again!="y" and play_again!="n":
                print_centered("please enter a valid input (y/n)",end="")
                play_again=input("")
            if play_again=="n":
                #if the user does not want to play again, print the credits and thank you message
                print("\n"*5)
                print_centered("Thanks for playing Reactle "+name+", hope you had fun!")
                if games_played!=1:
                    print_centered("You played "+str(games_played)+" games!")
                print_centered("Play again sometime!")
                print("\n"*3)
                print_centered("⭐⭐⭐Credits⭐⭐⭐")
                print_centered("Coding by: John-Paul, Agnese, Feyi, Madeline")
                #joke that the user is the play tester for the game
                print_centered("Playing testing by: "+name)
                #exit the program
                exit()
            #if the user wants to play again, break the loop
            else:
                running=False
                break

            
        #if the user has not used all their guesses and has not gotten the reaction right and they have made at least one guess
        if guessnumber!=0 and running==True:
            #print the reaction string, the periodic table, and the guess result
            response=coloured_reaction(reaction_ans_str,guess_list,previous_guesses)
            print("\n"*4)
            print_centered(Style.BRIGHT+"\033[1m"+""+"Guess:"+str(guessnumber)+Style.RESET_ALL+"\033[m")
            print_centered_multiline(response[1])
            print_centered_multiline(response[2])
            print_centered(response[0])
            #tell the user if their guess was correct, in the wrong spot, or incorrect and tell them how to interprit the colours
            print_centered("Sorry not right, try again.")
            print_centered("Hint: the"+ Fore.GREEN+" green"+Style.RESET_ALL+" atoms are correct, the "+Fore.YELLOW+"yellow"+Style.RESET_ALL+" are in the reaction but not the right spot, and the "+Fore.RED+"red"+Style.RESET_ALL+" atoms are incorrect.")
            print_centered("On the periodic table the background colour represents the best past guess for that atom.")
            #tell the user how many guesses they have left
            if guessnumber==5:
                print("\n"*2)
                #if the user is on their last guess, tell them
                print_centered("⚠️  ⚠️  ⚠️  This is your last guess  ⚠️  ⚠️  ⚠️")

            #if the user is not on their last guess, tell them how many guesses they have left
            else:
                print("\n"*2)
                print_centered("You have "+str(6-guessnumber)+" guesses left")
            print("\n"*2)

        #whipeout/initalize the guess list
        guess_list=[]
        #initialize the index as 0
        index=0
        #loop through the range of the length of the answer list, so as to get the right number of inputs
        while index<len(reaction[1]):
            #ask the user for their guess
            print_centered("["+str(reaction[1][index][0])+"] = ",end="")
            guess=input("")
            #if the guess is valid atom
            if is_valid_atom(guess):
                #add the converted guess to the guess list
                guess_list.append(guess_converter(guess))
                #add one to the index(going to the next element in the answer list)
                index+=1
            #if the guess is not a valid atom
            else:
                #tell user guess is not valid, and prompt them to try again
                print_centered("Invalid atom guess, make sure that the first letter is capitalized and if there is a second it is lowercase.")
                print_centered("Try again")
        #add one to the guess number
        guessnumber+=1
        #check if the user's guess is correct
        if check_guess(guess_list,reaction[1])==True:
            #if the user's guess is correct, congratulate them and tell them how many guesses it took them
            print_centered("Congratulations "+name+" you got the reaction right!🎉🎉🎉")
            #if the user got the reaction right on their first try
            if guessnumber==1:
                #special message for getting it on the first try
                print_centered("On your first try too!🎉🎉🎉")
                print_centered("You are a Reactle master!")
            #if the user did not get the reaction right on their first try
            else:
                #tell the user how many guesses it took them
                print_centered("You got the reaction right in "+str(guessnumber)+" guesses!")
                print_centered("The reaction was indeed \""+reaction_ans_str+"\" as you have guessed.")
            #ask the user if they want to play again
            print_centered("would you like to play again? (y/n)",end="")
            #initialize the play again variable/whipe it if it was used before
            play_again=input("")
            #add one to the games played variable
            games_played+=1
            #wait for the user to enter a valid input
            while play_again!="y" and play_again!="n":
                print_centered("please enter a valid input (y/n)",end="")
                play_again=input("")
            if play_again=="n":
                #if the user does not want to play again, print the credits and thank you message
                print("\n"*5)
                print_centered("Thanks for playing Reactle "+name+", hope you had fun!")
                if games_played!=1:
                    print_centered("You played "+str(games_played)+" games!")
                print_centered("Play again sometime!")
                print("\n"*3)
                print_centered("⭐⭐⭐Credits⭐⭐⭐")
                print_centered("Coding by: John-Paul, Agnese, Feyi, Madeline")
                #joke that the user is the play tester for the game
                print_centered("Playing testing by: "+name)
                #exit the program
                exit()
            #if the user wants to play again, break the loop
            else:
                running=False
                break

            