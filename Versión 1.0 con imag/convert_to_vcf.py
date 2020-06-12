# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:19:58 2020

@author: erikd


IMPORTANTE: CAMBIAR Ñ O LETRAS CON ACENTO -> dan error
"""

#TEL



class hacer_vcard:
    def __init__(self, names, phones):
        self.phones = phones
        self.names = names
        self.crear_archivo()
        

    def hacer_contacto(self,name, phone):
        j = ("BEGIN:VCARD\n\nVERSION:2.1\n\nN:;{0};;;\n\nFN:\n\nTEL;TYPE=CELL:{1}\n\nEND:VCARD\n").format(name, phone)
        return j
        

    def crear_archivo(self):
        f = open("test_11.vcf", "a")
        for i in range(len(self.phones)):
            f.write(self.hacer_contacto(self.names[i], self.phones[i]))
        
        f.close()



    
    
          
