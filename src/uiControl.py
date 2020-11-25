# -*- coding: UTF-8 -*-
##############################################################################
# Copyright (c) 2012 Hajime Nakagami<nakagami@gmail.com>
# All rights reserved.
# Licensed under the New BSD License
# (http://www.freebsd.org/copyright/freebsd-license.html)
#
# A image viewer. Require Pillow ( https://pypi.python.org/pypi/Pillow/ ).
##############################################################################
import PIL.Image


from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Progressbar
import PIL.ImageTk
from PIL import Image
import logging

from question import *
from tools import *
from updater import *
from embeddedServer import *
from packageTools import packageTool

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class Viewer(Frame):
    def resize(self, w, h, w_box, h_box, pil_image):  
        f1 = 1.0*w_box/w # 1.0 forces float division in Python2  
        f2 = 1.0*h_box/h  
        factor = min([f1, f2])  
        #print(f1, f2, factor) # test  
        # use best down-sizing filter  
        width = int(w*factor)  
        height = int(h*factor)  
        return pil_image.resize((width, height), Image.ANTIALIAS) 

    def chg_image(self):
        if self.im.mode == "1":
            self.img = PIL.ImageTk.BitmapImage(self.im, foreground="white")
        else:
            scale_w = 1000
            scale_h = 750
            
            w, h = self.im.size          
            self.im = self.resize(w, h, scale_w, scale_h, self.im)

            self.img = PIL.ImageTk.PhotoImage(self.im)
        self.la.config(image=self.img, bg="#000000",
                       width=self.img.width(), height=self.img.height())

    def next(self):
        logging.debug(str(self.chkValue.get()))
        if(self.chkValue.get() == True):
            self.qc.randomNext()
        else:
            self.qc.next()
        self.im = PIL.Image.open(self.qc.getImage())
        self.chg_image()

        self.num_page_ans.set("****")
        #練習模式直接顯示答案
        if(self.practiceMode.get() == True):
            self.showAns()

        self.num_page_tv.set("Slide: " + self.qc.getNo())

    def back(self):
        logging.debug(str(self.chkValue.get()))
        if(self.chkValue.get() == True):
            self.qc.randomBack()
        else:
            self.qc.back()
        self.im = PIL.Image.open(self.qc.getImage())
        self.chg_image()
        self.num_page_ans.set("****")
        #練習模式直接顯示答案
        if(self.practiceMode.get() == True):
            self.showAns()

        self.num_page_tv.set("Slide: " + self.qc.getNo())

    def showAns(self):
        self.num_page_ans.set(self.qc.getAns())

    def changeMode(self):
        self.qc.setCurrentNo(0)

    def changeMenuOption(self, *args):
        #TODO
        if(self.MenuOption.get() == "匯入題目"):
            folder = filedialog.askdirectory()
            #如果取消、不做任何事
            if(folder == ""):
                self.MenuOption.set(self.cp.getLastQuestionOption())
                return False
            pt = packageTool()
            #檢查題目包是否合法
            r = pt.checkDirFormat(folder)
            if(r != 0):
                messagebox.showerror("Error", "Error code: "+str(r))
                return False
            
            #複製題目包
            if(pt.copyPackage(folder)):
                messagebox.showinfo("OK", "匯入成功，軟體將關閉，請重新開啟軟體 Code="+str(r))
            #Config update
            self.cp.addPackage(pt.title, pt.packageDir)

            #回復題目選單
            #self.cp.reload()
            self.MenuOption.set(self.cp.getLastQuestionOption())
            print(self.cp.getLastQuestionOption())
            self.quit()
            return True
            
        if(self.MenuOption.get() == "移除題目"):
            os.system(os.path.join(os.getcwd(), "removePackage.exe"))
            self.MenuOption.set(self.cp.getLastQuestionOption())
            self.quit()
            return True

        self.cp.writeLastDir(self.QuestionInfo[self.MenuOption.get()])
        self.cp.WriteLastQuestionOption(self.MenuOption.get())
        logging.debug(self.cp.readLastDir())

        if(self.cp.readLastDir() != ""):
            self.qc.load(self.cp.readLastDir())
            self.master.title(self.qc.getTitle())
            self.isLastDirExsit = True
        else:
            self.master.title("跑台練習程式")

        #載入照片
        if(self.isLastDirExsit):
            #手動變更隨機選項，使其變成循序模式
            self.chkValue.set(False)
            self.changeMode()
            self.next()

    def ShowAbout(self):
        messagebox.showinfo("關於 | About", self.cp.getAbout())

    def progress(self, currentValue):
        #self.progressbar["value"]=currentValue
        pass

    def __init__(self, master=None):
        #建立資料處理器
        self.fpc = FilePackageController()
        self.qc = QuestionController()
        self.cp = ConfigProcesser("config.json")
        self.ud = Updater()
        self.QuestionInfo = self.cp.getQuestionInfo()
        #print(self.QuestionInfo)
        self.isLastDirExsit = False

        #self.es.start()

        #更新題目
        if(self.ud.CheckVersion()):
            messagebox.showinfo("題目更新", "程式題目更新中，請稍候\n拜託不要關閉視窗，會出事！")
            
            if(not(self.ud.update())):
                messagebox.showerror("更新失敗", "程式題目更新失敗")
            else:
                messagebox.showinfo("Finish!", "更新完成！")

        Frame.__init__(self, master)

        print(self.cp.readLastDir())
        if(self.cp.readLastDir() != ""):
            self.qc.load(self.cp.readLastDir())
            self.master.title(self.qc.getTitle())
            self.isLastDirExsit = True
        else:
            self.master.title("跑台練習程式")
        
        #讀取題目資訊給題目選單
        OptionList = list(self.QuestionInfo.keys())
        OptionList.append("匯入題目")
        OptionList.append("移除題目")

        self.num_page = 0
        self.num_page_tv = StringVar()
        self.num_page_ans = StringVar()
        self.practiceMode = BooleanVar() 
        self.practiceMode.set(False)
        self.chkValue = BooleanVar() 
        self.chkValue.set(False)
        self.MenuOption = StringVar()
        self.MenuOption.set(self.cp.getLastQuestionOption())

        fram = Frame(self)
        self.master.iconbitmap("icon.ico")

        Button(fram, text="Back", command=self.back).pack(side=LEFT)
        Label(fram, textvariable=self.num_page_tv).pack(side=LEFT)
        Button(fram, text="Next", command=self.next).pack(side=LEFT)
        Button(fram, text="Show answer", command=self.showAns).pack(side=LEFT)
        Label(fram, textvariable=self.num_page_ans).pack(side=LEFT)
        Button(fram, text="關於", command=self.ShowAbout).pack(side=RIGHT)
        OptionMenu(fram, self.MenuOption, *OptionList, command=self.changeMenuOption).pack(side=RIGHT)

        self.MenuOption.trace("w", self.changeMenuOption)
        #Button(fram, text="Open Package").pack(side=RIGHT)
        Checkbutton(fram, text='是否隨機', var=self.chkValue, command=self.changeMode).pack(side=RIGHT)
        Checkbutton(fram, text='練習模式', var=self.practiceMode, command=self.changeMode).pack(side=RIGHT)
        fram.pack(side=TOP, fill=BOTH)
        
        self.la = Label(self)
        self.la.pack()

        self.pack()
        #載入第一張照片
        if(self.isLastDirExsit):
            self.next()