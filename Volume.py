#amixer sset 'Master' XX%
import os
import sys

def main():
    if( len(sys.argv) > 0):
        command = "amixer sset \'Master\' %d"%(int(sys.argv[1])%63)
        os.system(command)
    else:
        print("write a volumen")

if __name__ == "__main__":
   main()
