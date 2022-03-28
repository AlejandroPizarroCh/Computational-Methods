# Activity 3.2 Programming a DFA
# Implementation of Computational Methods
# Alejandro Pizarro Chávez - A01633784
# Tuesday, March 15, 2022

import re

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++ Functions ++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# function that saves each token into a string *main function*
def lexerAritmetico(file):
    with open(file, 'r') as infile: # 'r' open for text file for reading text 
        list = [line.strip() for line in infile]
        list = clear('', list, True) 
    i = 0
    for j in list:
        list[i] = re.split('(\W)', j) # split string by the occurrences of patern
        list[i] = clear('', list[i], True) 
        i += 1
    
    skipSS(list)
    clear('', list, False) 
    mergeExp(list)
    clear('', list, False)
    
    return list # return final list with all functions involved


# function that merge elements from a real number with exponential
def mergeExp(list):
    for i in range(len(list)):
        for k in range(len(list[i])):
            if 'E' in list[i][k].upper() and '.' in list[i][k-1]: # verify if there's an 'E' or a '.' in the given list
                    if list[i][k+1] == '-' and list[i][k+2].isnumeric() == True :
                        merge = list[i][k-1] + list[i][k] + list[i][k+1] + list[i][k+2] # the before, actual, after, and after from the after
                        list[i][k-1] = merge
                        list[i][k] = ''
                        list[i][k+1] = ''
                        list[i][k+2] = ''
                    elif list[i][k+1].isnumeric() == True: # true state if all characters in a string are numeric
                        merge = list[i][k-1] + list[i][k] + list[i][k+1] # the before, actual, and after 
                        list[i][k-1] = merge
                        list[i][k] = ''
                        list[i][k+1] = ''             
    return list    


# function that removes duplicated elements
def clear(tempVal, list, bool):
    if bool == True: 
        while(tempVal in list):
            list.remove(tempVal)
    if bool == False: 
        i = 0
        for x in list:
            list[i] = clear('', list[i], True)
            i += 1 
    return list


# function that merge elements from comments or real numbers into a single string 
def skipSS(list):
    # comments
    for i in range(len(list)):
        for k in range(len(list[i])):
            if k < len(list[i]): # veriyf so loop doesn't break
                if list[i][k] == '/' and list[i][k] == list[i][k+1]: 
                    merge = ''.join(list[i][k:])
                    list[i][k:] = [merge]
                    break
            break    
    # real numbers
        for k in range(len(list[i])):
    # floating point
            if list[i][k] == '.':
                if len(list[i]) - k > 1:
                    if list[i][k-1].isnumeric() == True:
                        if list[i][k+1].isnumeric() == True:
                            merge = list[i][k-1] + list[i][k] + list[i][k+1]
                            list[i][k-1] = merge
                            list[i][k] = '' 
                            list[i][k+1] = ''
                        elif list[i][k+1].isnumeric() == False:
                            merge = list[i][k-1] + list[i][k]
                            list[i][k-1] = merge
                            list[i][k] = ''
                    elif list[i][k-1].isnumeric() == False and list[i][k+1].isnumeric() == True:
                        merge = list[i][k] + list[i][k+1]
                        list[i][k] = merge
                        list[i][k+1] = ''
                elif len(list[i]) - k == 1: 
                    merge = list[i][k-1] + list[i][k]
                    list[i][k-1] = merge
                    list[i][k] = ''  
    # negative real numbers
            if '.' in list[i][k] and list[i][k-1] == '-':
                if list[i][k-2].isnumeric == False or '.' not in list[i][k-2]:
                    merge = list[i][k-1] + list[i][k]
                    list[i][k-1] = merge
                    list[i][k] = ''
    return list


# function that merge corresponding elements from real number with exponential
def mergeExp(list):
    for i in range(len(list)):
        for k in range(len(list[i])):
            if 'E' in list[i][k].upper() and '.' in list[i][k-1]:
                    if  list[i][k+1].isnumeric() == True: # returns True if all characters in a string are numeric characters
                        merge = list[i][k-1] + list[i][k] + list[i][k+1]
                        list[i][k-1] = merge
                        list[i][k] = ''
                        list[i][k+1] = ''
                    elif list[i][k+1] == '-' and list[i][k+2].isnumeric() == True :
                        merge = list[i][k-1] + list[i][k] + list[i][k+1] + list[i][k+2]
                        list[i][k-1] = merge
                        list[i][k] = ''
                        list[i][k+1] = ''
                        list[i][k+2] = '' 
    return list            


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++ Main +++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

file = "C:/Users/aleja/Documents/CUARTO SEMESTRE/métodos computacionales/Computational-Methods/programmingDFA/testCases.txt" # change full route for other test cases, if not, it won't work :(

# defining alphabets
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
operators = ['=','+','-','*','/','^']
operatorsName = ['Asignacion', 'Suma', 'Resta', 'Multiplicacion', 'Division', 'Potencia']
specialSymbol = ['(',')']
specialSymbolName = ['Parentesis que abre', 'Parentesis que cierra']

# file to matrix using arithmetic lexer function previously defined
inputText = lexerAritmetico(file)

# print in specified 'table' format 
print("Token:\tTipo:")
for i in range(len(inputText)):
    for k in range(len(inputText[i])):
        checker = list(filter(inputText[i][k].startswith, letters)) != []
        checker2 = letters + numbers + '_'
        # variables
        if checker == True and any(x not in checker2 for x in inputText[i][k]) == False:
            print(inputText[i][k] + "\t--- Variable")
        # operators 
        elif inputText[i][k] in operators:
            find = operators.index(inputText[i][k])
            print(inputText[i][k] + "\t--- " + operatorsName[find])
        # real numbers
        elif '.' in inputText[i][k] and len(inputText[i][k]) > 1:
            print(inputText[i][k] + "\t--- Real")
        # whole numbers
        elif inputText[i][k].isnumeric() == True:
            print(inputText[i][k] + "\t--- Entero", end = '')
            if inputText[i][k].startswith('0') == True and len(inputText[i][k]) > 1:
                print(" Octal")
            else:
                print('')
        # comments
        elif inputText[i][k].startswith('//') == True:
            print(inputText[i][k] + "\t--- Comentario")
        # special symbols
        elif inputText[i][k] in specialSymbol:
            find = specialSymbol.index(inputText[i][k])
            print(inputText[i][k] + "\t--- " + specialSymbolName[find])
        # error - tolerant
        elif inputText[i][k] != ' ':
            print(inputText[i][k] + "\t--- Error", end = '')
            print(" en Linea " + str(i) + " / Columna " + str(k))   
