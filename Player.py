'''
    Autor   :    Josepablo Cruz Baas
    Fecha   :    19 - 08 - 2016

    Descripcion :    Este programa reproduce uno a uno, las canciones en el
        documento playlist.xml si existen, de lo contrario
        espera a que existan nuevos contenidos.

    Todos los errores y excepciones se aniaden al documento error.log
    Las direcciones y nombres de documentos pueden editarse
    sin comprometer el codigo siendo estas variables, las primeras declaradas.

    Requerimientos :
        mplayer instalado y las librerias subprocess y xml.etree.ElementTree
'''

import xml.etree.ElementTree as XML #Parser xml
#import subprocess                   #Lanzador de proceso
from multiprocessing import Process
import time                         #Fecha y Hora e Interrupciones
import os                           #Lanzador de comandos de sistema

#VARIABLES CONSTANTES
    #DIRECCIONES DE FICHEROS Y PROGRAMAS
PLAYLIST = "playlist.xml"   #Lista de reproduccion
PLAYCOMMAND = ""    #Programa reproductor de audio
PLAYINGFILE = "playing"     #Archivo bandera que indica el estado del subproceso
                            #    de reproduccion
LOGFILE = "error.log"       #Archivo de almacenamiento de errores
SYSTEM = "system.xml"
PITCHERDIR = ""
SONGLIST = "songlist.xml"
PLAYERNAME = ""
STOPCOMMAND = ""
VOLUMEDIR = ""


try:
  tree = XML.parse(SYSTEM)
  xml = tree.getroot()
  PLAYLIST = xml[0][0].text
  SONGLIST = xml[0][1].text
  PITCHERDIR = xml[0][2].text
  PLAYERNAME = xml[0][3].text
  STOPCOMMAND = xml[1][0].attrib['stop']
  LOGFILE = xml[0][5].text
  PLAYINGFILE = xml[0][6].text
  VOLUMEDIR = xml[0][7].text
  PLAYCOMMAND = xml[1][0].attrib['start']
  print(PLAYCOMMAND)
except XML.ParseError as Error:
    log = "%s %s"%(time.strftime("%c"),repr(Error))
    f = open(LOGFILE,"a")
    f.write("%s\n"%log)
    f.close()
    quit()
#Lanza un comando directamente a la consola
def command(command):
    os.system(str(command))

#Escribe al final del documento de errores, una cadena de caracteres
def WriteLog(_STR_):
    log = "%s %s"%(time.strftime("%c"),_STR_)
    f = open(LOGFILE,"a")
    f.write("%s\n"%log)
    f.close()
def stopLog(_STR_):
    WriteLog(_STR_)
    quit()
#Escritura del documento bandera del estado del subproceso
def isPlaying():
    f = open(PLAYINGFILE,"w")
    f.write("playing")
    f.close()
    WriteLog("Is playing . . .\n")
#Remueve el documento bandera para hacer saber a los otros procesos
#Que se ha detenido la reproduccion
def isnotPlaying():
    try:
        os.remove(PLAYINGFILE)
        return True
    except:
        return False
    WriteLog("Is not playing . . .\n")

#Lanza el reproductor con el elemento a reproducir indicado
# En forma de direccion como cadena de caracteres
def play(dir):
    comando = "%s \'%s\'"%(PLAYCOMMAND,dir)
    p = Process(target=command, args=(comando,))
    p.start()
    while p.is_alive():
        try:
            file = open(PLAYINGFILE,"r");
            fileContent = file.read()
            if(fileContent == "Exit"):
                isnotPlaying()
                file.close()
                os.remove(PLAYINGFILE)
                stopLog("Stopped by the User")
                quit()
            file.close()
        except:
            continue

#Funcion principal, Si existe elemento que reproducir lo reproduce,
# de lo contario espera y vuelve a comenzar
def main():
    flag = True
    while(True):
        isnotPlaying()
#Se abre la lista de reproduccion
        try:
            tree = XML.parse(PLAYLIST)
            xml = tree.getroot()
        except XML.ParseError as Error:
            print("No se ha podido parsear")
            WriteLog(repr(Error))
            break
#Si hay algo que reproducir se reproduce
        if ( xml.findall("song") == [] ):
            if(flag):
                print("Empty play list")
                flag = False
            time.sleep(1)
            continue
        else:
            flag = True
            isPlaying()
            play(xml[0].text)
            try:
                tree = XML.parse(PLAYLIST)
                xml = tree.getroot()
            except XML.ParseError as Error:
            	print("No se ha podido parsear")
            	stopLog(repr(Error))
            xml.remove(xml[0])
            tree.write(PLAYLIST)
if __name__=="__main__":
    main()
