#Error code
#0 = Normal exit or User cancel
#1 = IO error
#2 = Server Error

import requests
import json
import shutil
import os
from requests.exceptions import RequestException, Timeout
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo
import pprint
import logging

class ZipProcess():
    def UnzipPackage(self, src, dest):
        with ZipFile(src, mode='r') as z:
            #zipName = "{0}/{1}".format(self.ProgramFolder, ((ZipInfo(src).filename.replace(".zip","")).split("\\")).split("/"))
            logging.debug(((ZipInfo(src).filename.replace(".zip",""))))
            #exit(0)
            """if(os.path.isdir(zipName)):
                logging.debug("目錄已存在")
                return ""
            """
            z.extractall(dest)

def LoadUpdateConfig():
    config = ""
    file = object()

    try:
        file = open("update.config", "r")
        configJson = file.read()
        config = json.loads(configJson)
    except IOError as e:
        logging.error("[IOError] " + str(e))
        exit(1)
    finally:
        file.close()
        return config

def CheckServer(url):
    try:
        r = requests.get(url, timeout=3)
    except RequestException as e:
        logging.error("[RequestException] " + str(e))
        return False
    
    if(r.status_code != 200):
        return False
    return True

def checkVersion(config):
    r = requests.get(config["Update-server"] + config["Version-data"], timeout=3)

    ServerVersionValueStr = r.text.strip().split(".")
    ServerVersionValue = int(ServerVersionValueStr[0]) * 100 + int(ServerVersionValueStr[1])
    currentVer = config["Current-version"].strip().split(".")
    CurrentVersionValue = int(currentVer[0]) * 100 + int(currentVer[1])

    if(ServerVersionValue > CurrentVersionValue):
        return True
    else:
        return False

def FetchFile(url):
    try:
        r = requests.get(url, timeout=3, stream=True)
        with open("app-update.temporary", 'wb') as f:
                for chunk in r.iter_content(chunk_size=128):
                    f.write(chunk)

    except RequestException as e:
        logging.error("[RequestException] " + str(e))
        return False
    
    if(r.status_code != 200):
        return False
    return True
def main():
    print("Loading config...")
    config = LoadUpdateConfig()

    print("Check connection of update server...")
    if(CheckServer(config["Update-server"])):
        print("Server connection -> ok")
    else:
        print("Server connection -> error")
        exit(2)

    print("Check software version...")
    if(checkVersion(config)):
        print("Can update to the newest version.")

        reply = input("Do you want to update? (y/n)  ")
        if(reply.upper() != "Y"):
            print("Update abort.")
            exit(0)
    else:
        print("You have installed the newest version software.")

    print("Pre-fetch files on server...")
    if(FetchFile(config["Update-server"]+config["Update-file"])):
        print("File fetch completed")
    else:
        print("[Server error] Please contact server administrator. code={0}".format(2))
        exit(2)

    #檔案處理
    print("Unzipping new files...")
    zp = ZipProcess()
    os.rename("viewer.exe", "viewer.exe.backup")
    zp.UnzipPackage("app-update.temporary", ".")
    #os.remove("package.temporary")

if __name__ == "__main__":
    main()