#chemical reaction balancer taken from "https://github.com/diegoAchacong/python_chemical_equation_balancer/blob/main/PythonChemEuqationBalancer.py"
#modified by: John-Paul Huver to be used in the Reactle project for the database"
#modified to allow for an entire dictionary of reactions to be balanced at once
import re
from sympy import Matrix, lcm
from reactions_database import rdict
def remove_coefficient(coefficient_dict):
    reaction_dict={}
    for reaction in coefficient_dict:
        for chem in coefficient_dict[reaction]['reactants']:
            while chem[0].isdigit():
                if coefficient_dict[reaction]['reactants'][0].isdigit():
                    reaction_dict[reaction]['reactants']=coefficient_dict[reaction]['reactants'][1:]
        for chem in coefficient_dict[reaction]['products']:
            while chem[0].isdigit():
                if coefficient_dict[reaction]['products'][0].isdigit():
                    reaction_dict[reaction]['products']=coefficient_dict[reaction]['products'][1:]
                
    return reaction_dict
def reaction_balence_dict(reaction_dict):
    reaction_dict_balenced={}
    elementList=[]
    elementMatrix=[]
    for reaction in reaction_dict:
        reaction_dict_balenced[reaction]={}
        elementList=[]
        elementMatrix=[]
        reactants = reaction_dict[reaction]['reactants']
        products = reaction_dict[reaction]['products']
        reactants=str(reactants)
        products=str(products)
        reactants = reactants.replace(' ', '').split("+")
        products = products.replace(' ', '').split("+")
        for i in range(len(reactants)):
            compoundDecipher(reactants[i],i,1)

        for i in range(len(products)):
            compoundDecipher(products[i],i+len(reactants),-1)
        elementMatrix = Matrix(elementMatrix)
        elementMatrix = elementMatrix.transpose()
        solution=elementMatrix.nullspace()[0]
        multiple = lcm([val.q for val in solution])
        solution = multiple*solution
        coEffi=solution.tolist()
        for i in range(len(reactants)):
            reaction_dict_balenced[reaction]['reactants_balanced']+=str(coEffi[i][0])+reactants[i]
            if i<len(reactants)-1:
                reaction_dict_balenced[reaction]['reactants_balanced']+=" + "
        for i in range(len(products)):
            reaction_dict_balenced[reaction]['products_balanced']+=str(coEffi[i+len(reactants)][0])+products[i]
            if i<len(products)-1:
                reaction_dict_balenced[reaction]['products_balanced']+=" + "
        
        if reaction_dict_balenced[reaction]['reactants_balanced'] == reaction_dict[reaction]['reactants']:
            print("Reaction: "+reaction+" is already balanced")
        else:
            print("Reaction: "+reaction+" is not balanced")
            print("Balanced reaction: "+reaction_dict_balenced[reaction]['reactants_balanced']+" -> "+reaction_dict_balenced[reaction]['products_balanced'])
    return reaction_dict_balenced




elementMatrix=[]
elementList=[]
def addToMatrix(element, index, count, side):
    if(index == len(elementMatrix)):
       elementMatrix.append([])
       for x in elementList:
            elementMatrix[index].append(0)
    if(element not in elementList):
        elementList.append(element)
        for i in range(len(elementMatrix)):
            elementMatrix[i].append(0)
    column=elementList.index(element)
    elementMatrix[index][column]+=count*side
    
def findElements(segment,index, multiplier, side):
    elementsAndNumbers=re.split('([A-Z][a-z]?)',segment)
    i=0
    while(i<len(elementsAndNumbers)-1):#last element always blank
          i+=1
          if(len(elementsAndNumbers[i])>0):
            if(elementsAndNumbers[i+1].isdigit()):
                count=int(elementsAndNumbers[i+1])*multiplier
                addToMatrix(elementsAndNumbers[i], index, count, side)
                i+=1
            else:
                addToMatrix(elementsAndNumbers[i], index, multiplier, side)        
    
def compoundDecipher(compound, index, side):
    segments=re.split('(\([A-Za-z0-9]*\)[0-9]*)',compound)    
    for segment in segments:
        if segment.startswith("("):
            segment=re.split('\)([0-9]*)',segment)
            multiplier=int(segment[1])
            segment=segment[0][1:]
        else:
            multiplier=1
        findElements(re.sub('(\[|\])', '', segment), index, multiplier, side)
            

reaction_balence_dict(remove_coefficient(rdict))
