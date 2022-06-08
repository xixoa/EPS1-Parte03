# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 09:08:08 2022

@author: alumno
"""
import modulo




def pedirUserandContra():
    
    for i in range(2):
        print("\n***********Bienvenido al sistema de la UNTELS***********")
        user = input("\nIngrese usuario: ")
        password = input("Ingrese contraseña:")
        
        if(user == modulo.leer_archivo("login.txt") and password == modulo.leer_archivo("clave.txt")):                      
            menu() 
            break
        else:
            print("Incorrecto")

def menu(): 
    print("\nDatos Persona")
    print("1. Listar Persona")
    print("2. Agregar Persona")
    print("3. Salir")
    opcion = 1
    while opcion!=3:
        opcion = int(input("\nSelecciones una opcion[1-3]: "))
        
        if opcion==1:
            modulo.listar_personas()
        elif opcion==2:
            modulo.agregar_personas()    
        elif opcion==3:
            modulo.salir()
        else:
            modulo.error()
        
    
pedirUserandContra()   


