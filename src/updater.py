import logging
import os
import requests
import shutil

from tools import ConfigProcesser
from tools import ZipProcess

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class Updater():

    def __init__(self):
        self.cp = ConfigProcesser("config.json")
        self.ServerVersionURL = self.cp.getUpdateServer() + "/ver"

    def update(self):
            if(self.ServerTest()):
                if(self.CheckVersion()):
                    if(self.DownloadUpdateFile(self.cp.getUpdateServer())):
                        logging.info("Download file success")
                        self.ProcessUpdateFile()
                        return True
                    else:
                        logging.error("Download File failed.")
                        return False
                else:
                    logging.warning("Version lastest")
                    return False
            else:
                logging.error("Server test failed")
                return False

    def CheckVersion(self):     
        if(self.ServerTest()):
            r = requests.get(self.ServerVersionURL)

            ServerVersionValueStr = r.text.strip().split(".")
            ServerVersionValue = int(ServerVersionValueStr[0]) * 100 + int(ServerVersionValueStr[1])
            CurrentVersionValueStr = self.cp.getVersion().strip().split(".")
            CurrentVersionValue = int(CurrentVersionValueStr[0]) * 100 + int(CurrentVersionValueStr[1])

            if(ServerVersionValue > CurrentVersionValue):
                return True
            else:
                return False
        else:
            return False

    def ServerTest(self):
        r = requests.get(self.ServerVersionURL)
        if(r.status_code == 200):
            return True
        else:
            return False

    def DownloadUpdateFile(self, url):
        packageURL = url + "/package.zip"
        configURL = url + "/config.json.new"

        try:
            #Download package
            r = requests.get(packageURL, stream=True)
            with open("package.temporary", 'wb') as f:
                for chunk in r.iter_content(chunk_size=128):
                    f.write(chunk)

            r = requests.get(configURL)
            with open("config.json.new", "w") as f:
                f.write(r.text)
        except Exception as identifier:
            return False
        return True

    def ProcessUpdateFile(self):
        #處理config
        os.remove("config.json")
        os.rename("config.json.new", "config.json")
        #os.remove("config.json.new")

        #處理package
        zp = ZipProcess()
        zp.UnzipPackage("package.temporary", "package")
        shutil.rmtree("Questions")
        os.rename("package", "Questions")
        os.remove("package.temporary")
        
if __name__ == "__main__":
    ud = Updater()
    ud.update()

