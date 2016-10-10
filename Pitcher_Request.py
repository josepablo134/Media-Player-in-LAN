import optparse #Parser para lectura de argumentos y recuperacion de estos
import os       #Acceso a la terminal
import xml.etree.ElementTree as XML
from multiprocessing import Process
import sys
import time

SYSTEM = "system.xml"
PLAYLIST = "playlist.xml"
SONGLIST = "songlist.xml"
PLAYERNAME = "Player.py"
STOPCOMMAND = ""
LOGFILE = "error.log"
PLAYINGFILE = ""

try:
   tree = XML.parse(SYSTEM)
   xml = tree.getroot()
   PLAYLIST = xml[0][0].text
   SONGLIST = xml[0][1].text
   PLAYERNAME = xml[0][3].text
   STOPCOMMAND = xml[1][0].attrib['stop']
   LOGFILE = xml[0][5].text
   PLAYINGFILE = xml[0][6].text
except XML.ParseError as Error:
   log = "%s %s"%(time.strftime("%c"),repr(Error))
   f = open(LOGFILE,"a")
   f.write("%s\n"%log)
   f.close()
   exit()

def command(command):
    os.system("sudo "+str(command))

def WriteLog(_STR_):
    log = "%s %s"%(time.strftime("%c"),_STR_)
    f = open(LOGFILE,"a")
    f.write("%s\n"%log)
    f.close()

def stopLog(_STR_):
    WriteLog(_STR_)
    exit()

def launch():
    comando = "sudo %s %s"%("python",PLAYERNAME)
    p = Process(target=command, args=(comando,))
    p.start()
    exit()

def isLaunched():
    #Regresa True cuando existe el documento playing
    #False cuando este documento no existe
    try:
        f = open(PLAYINGFILE,"r")
        f.close
        flag = True
    except:
        flag = False
    return flag

def start():
    if(isLaunched()):
        stopLog("Player is already launched")
    else:
        launch()

def stop():
    if (isLaunched()):
        file = open(PLAYINGFILE,"w")
        file.write("Exit")
        file.close()
        p = Process(target=command, args=(STOPCOMMAND,))
        p.start()
        #os.remove(PLAYINGFILE)
    else:
        stopLog("Player is already stoped")

def add(DIR,_ID_):
#    tree = XML.parse(SONGLIST)
#    xml = tree.getroot()
#    if (xml.findall(str(DIR)) == ''):#Si el archivo no se encuentra en el xml
#        stopLog("File does not exist in database")
    #Si el archivo existe en el xml
    tree = XML.parse(PLAYLIST)
    xml = tree.getroot()
    subE = XML.SubElement(xml,"song")
        #nombre artista y album
    tree2 = XML.parse(SONGLIST)
    xml2 = tree2.getroot()
    for child in xml2:
        if(child.attrib['id'] == _ID_):
            subE.set("name",child.attrib['name'])
            subE.set("artist",child.attrib['artist'])
            subE.set("album",child.attrib['album'])
            break
    subE.text = str(DIR)
    tree.write(PLAYLIST)
    #Se escribe la informacion en la playlist

def main():
    p = optparse.OptionParser()
    p.add_option("--start",action="store_true",dest="launch")
    p.add_option("--stop",action="store_true",dest="stop")
    p.add_option("--add",action="store",dest="SONGDIR")

    p.set_defaults(launch=False)
    p.set_defaults(stop=False)

    opts, args = p.parse_args()

    if opts.launch:
        try:
            f = open(PLAYINGFILE,"r")
        except:
            launch()
        exit()
    if opts.stop:
        stop()
        exit()
    if opts.SONGDIR==None:
        print("Try to launch with arg -h")
        exit()
#    print(sys.argv[2])
    try:
        add(sys.argv[2],sys.argv[3])
    except:
        print("Try to launch with arg -h")
if __name__ == "__main__":
    main()
