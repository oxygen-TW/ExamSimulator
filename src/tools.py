import json
from zipfile import ZipFile, ZipInfo
import logging
import os
from os import path
from pathlib import Path
#from certificate import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class ConfigProcesser():

    def __init__(self, _config):
        self.configFile = _config
        self.config = {
            "LastDir": ""
        }

    def __write(self):
        output = json.dumps(self.config)
        fp = open(self.configFile, "w")
        fp.write(output)
        fp.close()

    def __read(self):
        fp = open(self.configFile, "r", encoding="utf-8")
        text = fp.read()
        fp.close()
        self.config = json.loads(text)

    def writeLastDir(self, _dir):
        self.config["LastDir"] = _dir
        self.__write()    

    def readLastDir(self):
        if(not(self.checkConfigFlie())):
            return ""

        self.__read()
        return os.path.join(self.config["QuestionRoot"],self.config["LastDir"])
    
    def checkConfigFlie(self):
        if(path.isfile(self.configFile)):
            return True
        else:
            return False

    def getId(self):
        self.__read()
        return self.config["id"]

    def getServerUrl(self):
        self.__read()
        return self.config["server"]

    def getQuestionInfo(self):
        self.__read()
        return self.config["questions"]

    def getLastQuestionOption(self):
        self.__read()
        return self.config["LastOption"]

    def WriteLastQuestionOption(self, LastOption):
        self.config["LastOption"] = LastOption
        self.__write()

    def getUpdateServer(self):
        self.__read()
        return self.config["update"]

    def getVersion(self):
        self.__read()
        return self.config["version"]

    def getAbout(self):
        _about = "跑台練習程式 2020-\nAuthor: CSMU MT 107 劉子豪\n題目包版本:{0}\n軟體版本:2.3".format(self.getVersion())
        return _about
        
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

class FilePackageController():

    def __init__(self):
        self.ProgramFolder = str(Path.home()).join("RunTablePractice")
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
"""
class Authorization():

    def __init__(self, _config):
        cp = ConfigProcesser(_config)
        self.id = cp.getId()
        self.url = cp.getServerUrl()

    def checkNewKey(self):
        if (not(os.path.isfile("certificate/{0}.pub".format(self.id)))):
            return True
        else:
            return False

    def NewKey(self):
        RSAnewKey(self.id, self.url)
        
    def check(self):
        if (not(os.path.isfile("certificate/{0}.pub".format(self.id)))):
            return RSAcheck(self.id, "certificate/{0}.pub".format(self.id), self.id)
        else:
            return RSAcheck(self.id, "certificate/{0}.pub".format(self.id), self.id)
"""

if __name__ == "__main__":
    #CP = ConfigProcesser("config.json")
    #print(CP.getQuestionInfo())
    
    pass