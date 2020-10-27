import binascii
import sys

from pn532pi import Pn532, pn532
from pn532pi import Pn532Hsu

class RfidPN532:
    
    def __init__(self):
        pass
        
            
    def read_uid(self):
        PN532_HSU = Pn532Hsu(Pn532Hsu.RPI_MINI_UART) #Creo interfaz. El argumento indica el puerto serial al que esta conectado el PN532
        lector = Pn532(PN532_HSU) #Creo el objeto encargado de interpretar la información recibida

        lector.begin()
        
        if (not lector.getFirmwareVersion()): #Este método se usa exclusivamente para verificar si la RPI detecta el dispositivo

            print("ERROR. Compruebe la conexión del dispositivo a la RPI. Vuelva a intentarlo")    # Solo entra en esta condición si no se reconoce PN532
            sys.exit()


        leido, uid = lector.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)

        while(not leido):

            leido, uid = lector.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)

        uid = binascii.hexlify(uid).decode('utf-8').upper()
        return uid

if __name__=="__main__":
    rf=RfidPN532()
    print("Porfavor, acerque su tarjeta al lector")
    uid=rf.read_uid()
    print("\nLa UID detectada es la siguiente: ")
    print(uid)
