import mechanize
import sys
import random
from mechanize import Browser

nombres = ['PedroZ', 'Catalina', 'Tomas', 'Delfina', 'Renata', 'Santiago', 'Matias', 'Sofia', 'Lucia', 'Pilar', 'Ignacio']
class intentoHilo:
        
    def __init__(self, url):
        
        self.bandera = False
        self.url = url

    #Hilo principal de intentos

    def comenzar(self):

        self.bandera = True
        
        browser = Browser()
        
        while(self.bandera):

            try:
                         
                browser.open(self.url)
                browser.select_form(nr = 0)                
                browser.form['username'] = ""
                browser.form['password'] = ""
                browser.submit()

            except:

                print("Error ")






        
