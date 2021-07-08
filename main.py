#imports
from tools.hilos import crearHilos


#Comenzar ataque
print("\nCantidad de hilos:", end = " ")
cantHilos = input()
print("\nPagina:", end = " ")
url = input()
print("\nIniciando ataque...")
print("\nIniciando hilos...")

crearHilos.iniciar(cantHilos, url, crearHilos)
    
    
    


