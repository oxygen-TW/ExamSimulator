import json
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo
import logging
import os
from os import path
from pathlib import Path
#from certificate import *

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class FilePackageController():

    def __init__(self):
        self.ProgramFolder = str(Path.home()) + "\RunTablePractice"
        logging.debug(self.ProgramFolder)

    def __ProgramFolderExsit(self):
        if(path.isdir(self.ProgramFolder)):
            return True
        else:
            return False
    
    def ProgramFolderPath(self):
        if(self.__ProgramFolderExsit()):
            return self.ProgramFolder
        else:
            try:
                os.mkdir(self.ProgramFolder)
            except OSError:
               logging.error("程式資料夾創建失敗")
            else:
                logging.info("新建程式資料夾")
            return self.ProgramFolder

    def DeleteProgramFolder(self):
        if(not(self.__ProgramFolderExsit())):
            return True
        else:
            try:
                os.rmdir(self.ProgramFolder)
            except OSError:
               logging.error("程式資料夾創建失敗")
               return False
            else:
                logging.info("新建程式資料夾")
            return True
        
class ZipProcess():

    def __init__(self):
        fpc = FilePackageController()
        self.ProgramFolder = fpc.ProgramFolderPath()

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
            #return zipName