import shutil, os
from tools import ConfigProcesser

print("ExamSimulator Package Detete Tool")
print("Programmer: Liu, Tzu-Hao Taiwan\n\n")

cp = ConfigProcesser("config.json")
questions = cp.getQuestionInfo()

for i, item in enumerate(questions):
    print("{}: {}".format(i, item))

index = int(input("請輸入你要刪除的題目包編號(需一字不差!):  "))

while(index < 0 or index > len(questions)-1):
    for i, item in enumerate(questions):
        print("{}: {}".format(i, item))

    index = int(input("請輸入你要刪除的題目包編號(需一字不差!):  "))


tmplist = list(questions)
folderName = questions[tmplist[index]]
name = tmplist[index]

shutil.rmtree(os.path.join(os.getcwd(), os.path.join("Questions", folderName)))
cp.removePackage(name)