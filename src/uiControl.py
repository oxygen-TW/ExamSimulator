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
import PIL.ImageTk
from PIL import Image
import logging

from question import *
from tools import *
from certificate import *

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class Viewer(Frame):
    def resize(self, w, h, w_box, h_box, pil_image):  
        ''' 
        resize a pil_image object so it will fit into 
        a box of size w_box times h_box, but retain aspect ratio 
        对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例 
        '''  
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

    def open(self):
        logging.debug(str(self.chkValue.get()))
        if(self.chkValue.get() == True):
            self.qc.randomNext()
        else:
            self.qc.next()
        self.im = PIL.Image.open(self.qc.getImage())
        self.chg_image()
        self.num_page_ans.set("****")
        self.num_page_tv.set("Slide: " + self.qc.getNo())

    def OpenPackage(self):
        _dir = filedialog.askopenfilename(initialdir = "",title = "select file",filetypes = [("zip file", "*.zip")])
        zp = ZipProcess()
        unzipDir = zp.UnzipPackage(_dir)

        self.qc.load(unzipDir)
        self.cp.writeLastDir(unzipDir)
        self.open()

    def showAns(self):
        self.num_page_ans.set(self.qc.getAns())

    def changeMode(self):
        self.qc.setCurrentNo(0)

    def changeMenuOption(self, *args):
        #print(self.QuestionInfo[self.MenuOption.get()])
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
            self.open()

    def __init__(self, master=None):
        #建立資料處理器
        self.fpc = FilePackageController()
        self.qc = QuestionController()
        self.cp = ConfigProcesser("config.json")
        self.QuestionInfo = self.cp.getQuestionInfo()
        self.isLastDirExsit = False
        
        
        Frame.__init__(self, master)

        logging.debug(self.cp.readLastDir())
        if(self.cp.readLastDir() != ""):
            self.qc.load(self.cp.readLastDir())
            self.master.title(self.qc.getTitle())
            self.isLastDirExsit = True
        else:
            self.master.title("跑台練習程式")
        
        #讀取題目資訊給題目選單
        OptionList = list(self.QuestionInfo.keys())
        self.num_page = 0
        self.num_page_tv = StringVar()
        self.num_page_ans = StringVar()
        self.chkValue = BooleanVar() 
        self.chkValue.set(False)
        self.MenuOption = StringVar()
        self.MenuOption.set(self.cp.getLastQuestionOption())

        fram = Frame(self)
        Button(fram, text="Next slide", command=self.open).pack(side=LEFT)
        Label(fram, textvariable=self.num_page_tv).pack(side=LEFT)
        Button(fram, text="Show answer", command=self.showAns).pack(side=LEFT)
        Label(fram, textvariable=self.num_page_ans).pack(side=LEFT)
        OptionMenu(fram, self.MenuOption, *OptionList).pack(side=RIGHT)
        self.MenuOption.trace("w", self.changeMenuOption)
        #Button(fram, text="Open Package", command=self.OpenPackage).pack(side=RIGHT)
        Checkbutton(fram, text='是否隨機', var=self.chkValue, command=self.changeMode).pack(side=RIGHT)
        fram.pack(side=TOP, fill=BOTH)
        

        self.la = Label(self)
        self.la.pack()

        self.pack()
        #載入第一張照片
        if(self.isLastDirExsit):
            self.open()