import json
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo
import logging
import os

logging.basicConfig(level=logging.DEBUG,
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
        fp = open(self.configFile, "r")
        text = fp.read()
        fp.close()
        self.config = json.loads(text)

    def writeLastDir(self, _dir):
        self.config["LastDir"] = _dir
        self.__write()    

    def readLastDir(self):
        self.__read()
        return self.config["LastDir"]

class ZipProcess():
    def UnzipPackage(self, src):
        with ZipFile(src, mode='r') as z:
            zipName = ZipInfo(src).filename.replace(".zip","")
            logging.debug(zipName)

            """if(os.path.isdir(zipName)):
                logging.debug("目錄已存在")
                return ""
            """
            z.extractall(".")
            return zipName

if __name__ == "__main__":
    cp = ConfigProcesser("config.json")
    zp = ZipProcess()

    print(zp.UnzipPackage("test2.zip"))