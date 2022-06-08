# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 09:08:08 2022

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


def pedirUserandContra():
    
    for i in range(2):
        print("\n***********Bienvenido al sistema de la UNTELS***********")
        user = input("\nIngrese usuario: ")
        password = input("Ingrese contraseña:")
        
        if(user == leer_archivo("login.txt") and password == leer_archivo("clave.txt")):                      
            menu() 
            break
        else:
            print("Incorrecto")

def menu(): 
    print("\nDatos Persona")
    print("1. Listar Persona")
    print("2. Agregar Persona")
    print("3. Salir")
    
    
    
pedirUserandContra()

