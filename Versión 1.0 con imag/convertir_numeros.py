# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:20:38 2020

@author: erikd

Hace falta:
    + Saber que columna es que
    + Convertir a contactos 
    + Returnear lista contactos
    
"""

import pandas as pd
import unidecode



from PyQt5 import QtCore, QtGui, QtWidgets

class Leer_xlsx:
    
    def __init__(self, location):
        self.location = location
        
    def return_values(self):#para devolver valores
        return self.nombres, self.telefonos
              

    def dar_columnas(self): #Consigue el nombre de la columna donde esta el nombre, y quita valores inimportantes en df
        df = pd.read_excel(self.location)
        return df.columns
        
    def ajustar_nombres(self, nombres_columna, telefono_columna, location):#Quita acentos y cosas por estilo
        df = pd.read_excel(location)
        nombres = df.iloc[:, df.columns.get_loc(nombres_columna)]
        for n in nombres:
            nombre_convertido = ""

            n = str(n)


            for letra in n:
                if letra != int:
                    letra = unidecode.unidecode(letra)
                else:
                    letra = str(letra)
                nombre_convertido = nombre_convertido + letra


            df = df.replace(n, nombre_convertido)
            
        nombres = df.iloc[:, df.columns.get_loc(nombres_columna)]
        telefonos = df.iloc[:, df.columns.get_loc(telefono_columna)]
                
        return nombres, telefonos
    
    


#-----------------------------------------------------------------


        


        




