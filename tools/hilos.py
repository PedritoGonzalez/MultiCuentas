import threading
import random
import linecache
import time
import sys

from tools.intento import intentoHilo

#######################

class crearHilos:

    def continuarMain(threads, cantHilos, intentos, self):

        self.bandera = self.Continuar

        try:

            while(self.bandera):

                self.bandera = False

                for i in range(len(intentos)):

                    if not(intentos[i].bandera):

                        self.bandera = True
                        
        except KeyboardInterrupt:
            
            print("\nFinalizando...")

        print("\nHilos iniciados\n")

        self.bandera = self.Continuar

        try:
    
            while(self.bandera):

                for i in range(len(intentos)):

                    if not(intentos[i].bandera):
                        self.bandera = False

        except KeyboardInterrupt:

            print("Finalizando...")

        for i in range((int)(cantHilos)):
        
            intentos[i].bandera = False

        print("\nFinalizado")

    #Crear por primera vez hilos

    def iniciar(cantHilos, url, self):

        self.Continuar = True
        
        intentos = list()  
        threads = list()

        for i in range((int)(cantHilos)):
            intentos.append(intentoHilo(url))
            threads.append(threading.Thread(target = intentos[i].comenzar)  )

        try:

            for i in range((int)(cantHilos)):
                threads[i].start()
                
        except KeyboardInterrupt:
            self.Continuar = False

        #Verificar si los hilos siguen vivos
            
        self.continuarMain(threads, cantHilos, intentos, self)


    #Continuar proceso

                









        
        

        
