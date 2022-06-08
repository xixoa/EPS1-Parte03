# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 09:25:49 2022

@author: alumno
"""

def leer_archivo(nombre):
    archivo = open(nombre,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido


def agregar_archivo(nombre,contenido):
    archivo = open (nombre, "at")
    archivo.write("," + contenido)
    archivo.close()

def listar_personas():
    contenido1 = leer_archivo("dni.txt")
    contenido2 = leer_archivo("nombre.txt")
    contenido3 = leer_archivo("apellido.txt")
    
    c=contenido1.split(",")
    d=contenido2.split(",")
    e=contenido3.split(",")
   
    
    print(" DNI\t\tNOMBRE\t\tAPELLIDO")
    print("--------------------------------")
    for i  in range(len(c)):
        print(f" {c[i]}\t\t{d[i]}\t\t{e[i]}")

    
def agregar_personas():
    print("\n___Agregar nueva persona__\n")
    dni = input("Ingrese el DNI:")
    nombre = input("Ingrese el nombre:")
    apellido = input("Ingrese el apellido:")
    agregar_archivo("dni.txt",dni)
    agregar_archivo("nombre.txt",nombre)
    agregar_archivo("apellido.txt",apellido)

def salir():
    print("Gracias por su visita")
    
def error():
    print("Opción Incorrecta >:v")
    



