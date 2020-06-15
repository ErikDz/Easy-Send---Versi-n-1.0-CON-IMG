
from datetime import datetime
from os import getcwd
from os import remove


class hacer_vcard:
    def __init__(self, names, phones):
        self.phones = phones
        self.names = names
        self.crear_archivo()
        
        
        
    def hacer_contacto(self,name, phone):
        j = ("BEGIN:VCARD\n\nVERSION:2.1\n\nN:;{0};;;\n\nFN:\n\nTEL;TYPE=CELL:{1}\n\nEND:VCARD\n").format(name, phone)
        return j
        

    def crear_archivo(self):
        now = datetime.now()
        nombre_a_poner = str(now.year) + str(now.month) + str(now.day) + "_contactos.vcf"

        try:
            remove(getcwd() + "\\contacts\\" + nombre_a_poner)
        except:
            pass

        f = open(getcwd() + "\\contacts\\" + nombre_a_poner , "a")
        for i in range(len(self.phones)):
            f.write(self.hacer_contacto(self.names[i], self.phones[i]))
        
        f.close()



    
    
          
