#!/bin/python
# Project name: DPIVI - Detect People Identity Via Image
# Version: 1.0
# Written by : KsrvcO
# Contact me: flower.k2000[at]gmail.com
# This source is compatible with linux systems
import os
import sys
import time
import face_recognition
from urllib2 import urlopen
from urllib import urlretrieve
from BeautifulSoup import BeautifulSoup as bs
if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] Run this tool as root privileges. Exiting ... \033[1;m""")
os.system("clear")
print("\n")
print(""" 
  8888888b.       8888888b.       8888888      888     888      8888888 
  888  "Y88b      888   Y88b        888        888     888        888   
  888    888      888    888        888        888     888        888   
  888    888      888   d88P        888        Y88b   d88P        888   
  888    888      8888888P"         888         Y88b d88P         888   
  888    888      888               888          Y88o88P          888   
  888  .d88P      888               888           Y888P           888   
  8888888P"       888             8888888          Y8P          8888888 
                                                                                                                                                                                    
  [+] Project name: DPIVI - Detect People Identity Via Image
  [+] Version: 1.0
  [+] Written by: KsrvcO
  [+] Contact me: flower.k2000[at]gmail.com
  [+] Compatible with: Linux Operation Systems
  
""")
time.sleep(4)
print("""
  1. Identity people
  2. Import database to system
  3. Exit
""")
choo = input("  [+] Choose an option: ")
if choo == 1:
    dir = raw_input("  [-] Enter your database directory ex /home/DBdir/ : ")
    samplepic = raw_input("  [-] Enter your picture for identity ex /home/mypic.jpg : ")
    print("""
      **************************************
          P R O C C E S S  S T A R T E D
      **************************************
    """)
    time.sleep(2)
    images = os.listdir(dir)
    image_to_be_matched = face_recognition.load_image_file(samplepic)
    image_to_be_matched_encoded = face_recognition.face_encodings(
        image_to_be_matched)[0]

    for image in images:

        current_image = face_recognition.load_image_file(dir + image)
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
        result = face_recognition.compare_faces(
            [image_to_be_matched_encoded], current_image_encoded)
        if result[0] == True:
                print ("  **********************************************")
                print ("  [+] Detected person with name:  " + image)
                print ("  **********************************************")
        else:
                print ("  [-] Not detected  " + image)
elif choo == 2:
    os.system("clear")
    print("\n")
    print(""" 
      8888888b.       8888888b.       8888888      888     888      8888888 
      888  "Y88b      888   Y88b        888        888     888        888   
      888    888      888    888        888        888     888        888   
      888    888      888   d88P        888        Y88b   d88P        888   
      888    888      8888888P"         888         Y88b d88P         888   
      888    888      888               888          Y88o88P          888   
      888  .d88P      888               888           Y888P           888   
      8888888P"       888             8888888          Y8P          8888888 
           I M P O R T   T H E   D A T A B A S E   T O   S Y S T E M 
        !Note 1! make sure that your files in source system are jpg formats.
        !Note 2! In same directory of this tool we will create a folder with 
             name  outfolder  and all of your  database from  source address 
             will be imported into this folder. If you have any folder  with
             this name on this directory please  first remove  or rename  it 
             and then continue.
    """)
    serveraddr = raw_input("  [+] Enter server address ex http://SourceServerIP/pics/ : ")
    os.system("mkdir outfolder")
    def main(url, out_folder="outfolder/"):
        soup = bs(urlopen(url))
        for image in soup.findAll("a"):
            parsed =  url+image['href']
            filename = image['href']
            outpath = os.path.join("outfolder/", filename)
            try:
                urlretrieve(parsed, outpath)
            except:
                print ("")
    if __name__ == "__main__":
        main(serveraddr, "outfolder/")
    os.system("find outfolder/ -type f ! -name '*.jpg' -delete")
elif choo == 3:
    os.system("exit")
else:
    print("  [!] Wrong selection. Exiting ...")
    os.system("exit")
