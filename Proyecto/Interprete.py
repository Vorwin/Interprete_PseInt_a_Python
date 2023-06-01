# Programación I 
# Proyecto Final (Traductor de pseint a python)
# Integrantes: 
# Gabriel Eduardo Fu Solórzano : 21001494
# Erwin Andrés Solórzano López : 22000270 


import os


def compile(archivo):
    #Abrir archivo .x
    with open(archivo,"r") as file:
        for linea in file:
            
            linea = linea.strip()
            lineas = linea.split(" ")

            fichero = archivo[:-2]

            #Creación del archivo py 
            file = open (f"{fichero}.py", "a")

            #Traducción de Proceso 
            if lineas[0] == "PROCESO":
                definicion = "def"
                nomDef = "main(): \n"
                file.write(definicion + " "+ nomDef)
            
            #Traducción de Definir 
            elif lineas[0] == "DEFINIR":
                nomVariable = lineas[1] 
                tipoVariable = lineas[3]
                if tipoVariable == "ENTERO;":
                    valorVariable = "0 \n"
                    file.write("     " + nomVariable + " = " + valorVariable)
                elif tipoVariable == "CARACTER;":
                    valorVariable = "' '\n"
                    file.write("     " + nomVariable + " = " + valorVariable)
                elif tipoVariable == "REAL;":
                    valorVariable = "0.0 \n"
                    file.write("     " + nomVariable + " = " + valorVariable)
                elif tipoVariable == "LOGICO;":
                    valorVariable = "True\n"
                    file.write("     " + nomVariable + " = " + valorVariable)
            
            #traducción de variables 
            elif "<-" in lineas:
                #Funcion cuadrada
                if "square" in lineas: 
                    file.write ("     import math\n")

                    linea = linea.replace(" square", "math.sqr(")
                    linea=linea.replace(";"," ")
                    signo = linea.split("<-")
                    nomVariable = signo[0]
                    valorVariable = signo[1]
                    file.write("     "+"     "  + nomVariable + " = " + valorVariable +  ")" + "\n")
                
                #función raíz 
                elif "sqrt" in lineas: 

                    file.write ("     import math\n")
                    linea = linea.replace(" sqrt", "math.sqrt(")
                    linea=linea.replace(";"," ")
                    signo = linea.split("<-")
                    nomVariable = signo[0]
                    valorVariable = signo[1]
                    file.write("     "+"     "  + nomVariable + " = " + valorVariable +  ")" + "\n")

                else: 
                    linea=linea.replace(";"," ")
                    signo = linea.split("<-")
                    nomVariable = signo[0]
                    valorVariable = signo[1]
                    file.write("     " + nomVariable + " = " + valorVariable + "\n")
                
                
            
            #Traducción de escribir 
            elif "ESCRIBIR" == lineas[0]:
                linea = linea.replace(";", ")")
                linea = linea.replace("+", ",")
                linea = linea.split(" ")
                linea = linea[1:]
                inicio = "print("
                frase = " ".join(linea)
                file.write("     " + inicio + frase +  "\n")
                
            #Traducción de Escribir linea 
            elif "ESCRIBIR_LINEA" == lineas[0]:
                linea = linea.replace(";", ")")
                linea = linea.replace("+", ",")
                linea = linea.split(" ")
                linea = linea[1:]
                inicio = "     print("
                frase = " ".join(linea)
                file.write("     " + inicio + frase +  "\n")

            #Traducción de Leer
            elif "LEER" == lineas[0]:
                linea = linea.replace(";", "")
                linea = linea.split(" ")
                linea = linea[1:]
                inicio = " = int(input())"
                frase = " ".join(linea)
                file.write("     " + frase + inicio +  "\n")

            #Traducción de Si
            elif "SI" == lineas[0]:
                nomVar = linea[4:]
                nomVariable = nomVar.replace(")",":")
                condicional=linea[:2]
                condicional = "if "
                file.write("     " + condicional + nomVariable + "\n")
                file.write("     ")

            #Traducción de SINO    
            elif "SINO" == lineas[0]:
                nomVar = lineas[0]
                nomVar= "else:"
                file.write("     " + nomVar + "\n")
                file.write("     ")
            
            #Traducción de FINSI
            elif "FINSI" == lineas[0]:
                file.write("     "+ "\n")
            
            #Traducción de Mientras
            elif "MIENTRAS" == lineas[0]:
                nomVar = linea[8:]
                nomVariable = nomVar.replace("HACER", ":")
                condicional = linea[:2]
                condicional = "while "
                file.write("     " + condicional + nomVariable + "\n")
                file.write("     ")
            
            #Traducción de Fin mientras 
            elif "FINMIENTRAS" == lineas[0]:
                file.write("     "+ "\n")
                    
            #Traducción de Fin Proceso 
            elif lineas[0] == "FINPROCESO":
                nomDef = "\nmain()"
                file.write("     " + nomDef)
            file.close()



def load(archivo):
    #Cargar el archivo py
    try: 
        fichero = archivo[:-3]
        exec(open(f"{fichero}.py").read())
    except SyntaxError:
        print("El codigo no esta bien escrito, revise el texto . x ")

def run(archivo):
    #Cargar y traducir archivo pseint 
    try:
        compile(archivo)
        fichero = archivo[:-2]
        exec(open(f"{fichero}.py").read())
    except SyntaxError:
        print("El codigo no esta bien escrito, revise el texto . x ")


def main():
    cerrar = True
    #Menú 
    while cerrar:
        ejecutar = str(input("#>> "))
        espacio = ejecutar.split()
        try:
            for x in espacio:
                if espacio[0] == "compile":
                    compile(espacio[1])
                    print("Traduciendo código... ")
                    break
                elif espacio[0] == "run":
                    print("Traduciendo y corriendo código...")
                    run(espacio[1])
                    break
                    
                elif espacio[0] == "load":
                    print("Corriendo código...")
                    load(espacio[1])
                    break
                elif espacio[0] == "exit":
                    print("Saliendo del programa...")
                    cerrar = False
                    break        
                else: 
                    print("Opción no válida...")
        except FileNotFoundError: 
            print("El archivo no se ha encontrado, ingrese uno válido") 
            pass


main()