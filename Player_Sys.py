import optparse #Parser para lectura de argumentos y recuperacion de estos
import os       #Acceso a la terminal
from multiprocessing import Process
import sys
import time
import xml.etree.ElementTree as XML

SYSTEM = "system.xml"
PLAYLIST = "playlist.xml"
PITCHERDIR = "Pitcher_Request.py"
SONGLIST = "songlist.xml"
PLAYERNAME = "Play.py"
STOPCOMMAND = ""
LOGFILE = "error.log"
PLAYINGFILE = ""
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
except XML.ParseError as Error:
   log = "%s %s"%(time.strftime("%c"),str(Error))
   f = open(LOGFILE,"a")
   f.write("%s\n"%log)
   exit()

#Escribe al final del documento de errores, una cadena de caracteres
def WriteLog(_STR_):
    log = "%s %s"%(time.strftime("%c"),_STR_)
    f = open(LOGFILE,"a")
    f.write("%s\n"%log)
    f.close()

def stopLog(_STR_):
    WriteLog(_STR_)
    exit()

def command(command):
    os.system("sudo "+str(command))

def launch():
    #os.system("python %s --start"%PITCHERDIR)
    comando = "%s %s %s"%("python",PITCHERDIR,"--start")
    p = Process(target=command, args=(comando,))
    p.start()
    exit()

def stop():
    comando = "%s %s %s"%("python",PITCHERDIR,"--stop")
    p = Process(target=command, args=(comando,))
    p.start()
    exit()

def add(DIR):
    #Si el fichero existe se agrega su direccion
    tree = XML.parse(SONGLIST)
    xml = tree.getroot()
    flag = False
    songdir = ""
    for child in xml:
        if(child.attrib['id'] == DIR):
            flag=True
            songdir = child.text
            break

    if not(flag):
        stopLog("Song does not exist in data base")


    comando = "%s %s %s \'%s\' \'%s\'"%("python",PITCHERDIR,"--add",songdir,DIR)
    #print(comando)
    p = Process(target=command, args=(comando,))
    p.start()
    exit()

def main():
    p = optparse.OptionParser()
    p.add_option("--start",action="store_true",dest="launch")
    p.add_option("--stop",action="store_true",dest="stop")
    p.add_option("--add",action="store",dest="SONGID")
    p.add_option("--vol",action="store",dest="VOL")

    p.set_defaults(launch=False)
    p.set_defaults(stop=False)

    opts, args = p.parse_args()

    if opts.launch:
        try:
            f = open(PLAYINGFILE,"r")
        except:
            while(True):
                launch()
        exit()
    if opts.stop:
        stop()
        exit()
    if opts.VOL != None:
       command("python %s %s"%(VOLUMEDIR,str(opts.VOL)))
       exit()
    if opts.SONGID==None:
        print("Especifica una direccion . . .")
        exit()
    add(sys.argv[2])
if __name__ == "__main__":
    main()
