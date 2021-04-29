import toml
from toml import TomlDecodeError
import sys, os, shutil

# Error code
# Dir not exsit = 1
# Config.toml not exsit = 2
# TomlDecodeError = 3
# TypeError = 4
# Config format Error = 5
# Config No Error = 6
# Image not match config number = 7

class packageTool():
    def checkDirFormat(self, dirPath):
        self.configPath = os.path.join(dirPath, "config.toml")
        if(not(os.path.isdir)):
            return 1
        if(not(os.path.isfile(self.configPath))):
            return 2

        #check TOML
        try:
            data = toml.load(self.configPath)
            print(data)
        except TomlDecodeError:
            return 3
        except TypeError:
            return 4
        
        try:
            self.title = data["title"]
            ans = data["answer"]
        except Exception as e:
            print(e)
            return 5
        
        self.AnsCount = len(ans)
        
        try:
            for i in range(1,self.AnsCount):
                ans[str(i)]
                #print(item)
        except Exception as e:
            print(str(e))
            return 6

        #Check picture
        for i in range(1,self.AnsCount):
            if(not(os.path.isfile(os.path.join(dirPath, str(i) + ".jpg")))):
                return 7

        return 0

    def copyPackage(self, dirPath):
        path = os.path.join(os.getcwd(), "Questions")
        targetDir = os.path.split(dirPath)[-1]
        self.packageDir = targetDir

        print(targetDir)
        targetDir = os.path.join(path, targetDir)

        #檢查目標目錄是否存在
        if(not(os.path.isdir(targetDir))):
            os.mkdir(targetDir)

        try:
            self.copytree(dirPath, targetDir)
        except Exception :
            return False
        return True
        
        

    #ok
    #https://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth
    def copytree(self, src, dst, symlinks=False, ignore=None):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)
    
if __name__ == "__main__":
    print(os.getcwd())
    p = packageTool()
    print(p.checkDirFormat("test"))
