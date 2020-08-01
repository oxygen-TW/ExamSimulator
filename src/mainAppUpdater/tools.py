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