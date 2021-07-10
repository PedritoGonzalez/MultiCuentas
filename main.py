#imports
try:
    from tools.hilos import crearHilos
except:
    os.system("pip3 install mechanize")
    from tools.hilos import crearHilos
import os


#Comenzar ataque
print("\nCantidad de hilos:", end = " ")
cantHilos = input()
print("\nPagina:", end = " ")
url = input()
print("\nIniciando ataque...")
print("\nIniciando hilos...")

crearHilos.iniciar(cantHilos, url, crearHilos)
