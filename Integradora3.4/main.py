"""

Alejandro Pizarro Chávez -- A01633784
Actividad Integradora 3.4 Resaltador de sintaxis 
Lunes 28 de Marzo del 2022

"""

import re
reg_exp = []

reg_exp.append(re.compile("(-[0-9]|[0-9])[0-9]*\.[0-9]+[Ee](-[0-9]|[0-9])[0-9]*[\s\n)(]")) # Index 0 - números con exponencial 'e'
reg_exp.append(re.compile("(-[0-9]|[0-9])[0-9]*\.[0-9]+[\s\n)(]")) # Index 1 - números decimales
reg_exp.append(re.compile("(-[0-9]|[0-9])[0-9]*[\s\n)(]")) # Index 2 - números enteros
reg_exp.append(re.compile("([a-z]|[A-Z])([a-z]|[A-Z]|[0-9]|[?!_-])*[\s\n)(]")) # Index 3 - palabras  
reg_exp.append(re.compile("[-*+/][\s\n)(]")) # Index 4 - signos (rest, mult, sum, div) 
reg_exp.append(re.compile("<>[\s\n)(]")) # Index 5 - signos <>
reg_exp.append(re.compile("<=[\s\n)(]")) # Index 6 - signo (menor o igual...)
reg_exp.append(re.compile("<[\s\n)(]")) # Index 7 - signo (menor que)
reg_exp.append(re.compile("=[\s\n)(]")) # Index 8 - signo (igual)
reg_exp.append(re.compile(">=[\s\n)(]")) # Index 9 - signo (mayor o igual...)
reg_exp.append(re.compile(">[\s\n)(]")) # Index 10 - signo (mayor que)
reg_exp.append(re.compile("\(")) # Index 11 - parentesis que abre 
reg_exp.append(re.compile("\)")) # Index 12 - parentesis que cierra
reg_exp.append(re.compile("'")) # Index 13 - comilla 
reg_exp.append(re.compile(";.*\n")) # Index 14 - comentario
reg_exp.append(re.compile("[ ]+")) # Index 15 - espacio (string vacio) 
reg_exp.append(re.compile("[\n]+")) # Index 16 - salto de línea
reg_exp.append(re.compile(".+?[\s\n)(]")) # Index 17 - error de sintaxis 

# Selecciona tres lenguajes de programación: C++, R y Swift
diccionario = "if,for,else,break,while,in,repeat"
diccionario = diccionario.split(',')

def writeExpNum(w, string): # números con exponencial 'e'
    w.write('<span id = "expNum">'+string+'</span>')
def writeDecNum(w, string): # números decimales 
    w.write('<span id = "decNum">'+string+'</span>')
def writeNum(w, string): # numeros enteros 
    w.write('<span id = "num">'+string+'</span>')
def writeWord(w, string): # palabras / letras
    w.write('<span id = "word">'+string+'</span>')
def writeKeyword(w,string): # palabra reservada 
    w.write('<span id = "keyword">'+string+'</span>')
def writeSign(w,string): # signos (rest, mult, sum, div)
    w.write('<span id = "sign">'+string+'</span>')
def writeLessMore(w,string): # signos <>
    w.write('<span id = "lessMore">'+string+'</span>')
def writeLessOrEqual(w,string): # signo <= 
    w.write('<span id = "lessOrEqual">'+string+'</span>')
def writeLess(w,string): # signo < 
    w.write('<span id = "less">'+string+'</span>')
def writeEqual(w,string): # signo = 
    w.write('<span id = "equal">'+string+'</span>')
def writeGreaterOrEqual(w,string): # signo >= 
    w.write('<span id = "greaterOrEqual">'+string+'</span>')
def writeGreater(w,string):  # signo > 
    w.write('<span id = "greater">'+string+'</span>')
def writeOpenParenthesis(w,string): # parentesis que abre
    w.write('<span id = "openParenthesis">'+string+'</span>')
def writeCloseParenthesis(w,string): # parentesis que cierra 
    w.write('<span id = "closeParenthesis">'+string+'</span>')
def writeHyphen(w,string): # guion 
    w.write('<span id = "hyphen">'+string+'</span>')
def writeQuote(w,string): # comilla simple 
    w.write('<span id = "quote">'+string+'</span> ')
def writeSpace(w,string): # espacio
     w.write('<span>'+string+'</span>') 
def writeSkip(w): # salto de línea
    w.write('</br>')
def writeError(w,string): # error de sintaxis
    w.write('<span id = "error">'+string+'</span> ')

k = open("index.html", "w")
k.write('<!DOCTYPE html>\n<head>\n')
k.write('<link rel="stylesheet" href="style.css">\n<title>Actividad Integradora 3.4</title>\n')
k.write("</head>\n<body>\n")
k.write ('<h3><span id = "expNum">Constantes de punto flotante &nbsp &nbsp</span><span id = "num">Constantes enteras &nbsp &nbsp</span><span id = "keyword">Palabras reservadas &nbsp &nbsp</span><span id = "word">Identificadores &nbsp &nbsp</span><span id = "sign">Simbolos especiales &nbsp &nbsp</span><span id = "quote">Comentarios &nbsp&nbsp</span><span id = "error">Error &nbsp &nbsp</span></h3></br></br>\n')


css = open("style.css", "w")
css.write("body{\nfont-size: 25px;\nfont-style: bold;\n}\n")
css.write("#h3{\nfont-size: 35;\n}\n")
css.write("#expNum, #decNum{\ncolor: rgb(143, 78, 142);\n}\n")
css.write("#num{\ncolor:rgb(153, 166, 124)\n}\n")
css.write("#word{\ncolor:rgb(120, 139, 237)\n}\n")
css.write("#keyword{\ncolor:rgb(255, 128, 0)\n}\n")
css.write("#sign, #lessMore, #lessOrEqual, #less, #equal, #greaterOrEqual, #greater, #openParenthesis, #closeParenthesis, #hyphen{\ncolor:rgb(9, 126, 96)\n}\n")
css.write("#quote{\ncolor:rgb(0, 0, 0)\n}\n")
css.write("#error{\ncolor:rgb(244, 43, 91)\n}\n")

leerArchivo = open("testCase.txt", "r")
elemento = leerArchivo.read()
# for element in lista: 

contador = 0 
while elemento != "": 
    contador = (contador+1)%5
    if contador == 0: 
        k.write("\n")
        # imprimir elemento
    for indice,reg in enumerate(reg_exp):
        z = reg.match(elemento)
        if z:
            print(indice)
            print(elemento[z.start():z.end()])
            if indice==3:
                if elemento[z.start():z.end()-1] in diccionario:
                    writeKeyword(k,elemento[z.start():z.end()-1])
                    print("palabra reservada")
                else:
                    writeWord(k,elemento[z.start():z.end()-1])
                elemento = elemento[z.end()-1:]
            elif indice == 0:
                writeExpNum(k,elemento[z.start():z.end()-1])
                elemento = elemento[z.end()-1:]
            elif indice == 1:
                writeDecNum(k,elemento[z.start():z.end()-1])
                elemento = elemento[z.end()-1:]
            elif indice == 2:
                writeNum(k,elemento[z.start():z.end()-1])
                elemento = elemento[z.end()-1:]
            elif indice == 4:
                writeSign(k,elemento[z.start():z.end()-1])
                elemento = elemento[z.end()-1:]
            elif indice == 5:
                writeLessMore(k,elemento[z.start():z.end()-1])
                elemento = elemento[z.end()-1:]
            elif indice == 6:
                writeLessOrEqual(k,elemento[z.start():z.end()-1])
                elemento = elemento[z.end()-1:]
            elif indice == 7:
                writeLess(k,elemento[z.start():z.end()-1])
                elemento = elemento[z.end()-1:]
            elif indice == 8:
                writeEqual(k,elemento[z.start():z.end()-1])
                elemento = elemento[z.end()-1:]
            elif indice == 9:
                writeGreaterOrEqual(k,elemento[z.start():z.end()-1])
                elemento = elemento[z.end()-1:]
            elif indice == 10:
                writeGreater(k,elemento[z.start():z.end()-1])
                elemento = elemento[z.end()-1:]
                
            elif indice == 11:
                writeOpenParenthesis(k,elemento[z.start():z.end()])
                elemento = elemento[z.end():]
            elif indice == 12:
                writeCloseParenthesis(k,elemento[z.start():z.end()])
                elemento = elemento[z.end():]
            elif indice == 13:
                writeHyphen(k,elemento[z.start():z.end()])
                elemento = elemento[z.end():]
            elif indice == 14:
                writeQuote(k,elemento[z.start():z.end()])
                elemento = elemento[z.end():]
            elif indice == 15:
                writeSpace(k,elemento[z.start():z.end()])
                elemento = elemento[z.end():]
            elif indice == 17:
                writeError(k,elemento[z.start():z.end()-1])
                elemento = elemento[z.end()-1:]
            elif indice ==16:
                elemento = elemento[z.end():]
                writeSkip(k)
            else:
                print("errorTotal1")
                elemento = elemento[z.end():]
            break
    if z == None:
        print('errorTotal2')
        elemento = elemento[1:]
            
leerArchivo.close()
k.write("\n</body>\n</html>\n")
k.close()
css.close()
