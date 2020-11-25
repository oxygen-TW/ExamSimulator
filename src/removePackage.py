import shutil, os
from tools import ConfigProcesser

print("ExamSimulator Package Detete Tool")
print("Programmer: Liu, Tzu-Hao Taiwan\n\n")

name = input("請輸入你要刪除的題目包名稱(需一字不差!):  ")

r = input("請確認題目包名稱是否正確 -> {} 是請輸入y 不是請輸入n : ".format(name))

while(r.upper() != "Y"):
    name = input("請重新輸入你要刪除的題目包名稱(需一字不差!):  ")
    r = input("請確認題目包名稱是否正確 -> {} 是請輸入y 不是請輸入n : ".format(name))

cp = ConfigProcesser("config.json")
questions = cp.getQuestionInfo()
folderName = questions[name]

shutil.rmtree(os.path.join(os.getcwd(), os.path.join("Questions", folderName)))

cp.removePackage(name)