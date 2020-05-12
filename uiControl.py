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
import PIL.ImageTk
from PIL import Image
import random, logging, json
from question import *
from tools import *

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class Viewer(Frame):
    def chg_image(self):
        
        if self.im.mode == "1":
            self.img = PIL.ImageTk.BitmapImage(self.im, foreground="white")
        else:
            scale_w = 475
            scale_h = 363
            self.img = PIL.ImageTk.PhotoImage(self.im)
        self.la.config(image=self.img, bg="#000000",
                       width=self.img.width(), height=self.img.height())

    def open(self):
        self.qc.randomNext()
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


    def __init__(self, master=None):
        #建立資料處理器

        self.qc = QuestionController()
        self.cp = ConfigProcesser("config.json")
        self.isLastDirExsit = False
        
        
        Frame.__init__(self, master)

        print(self.cp.readLastDir())
        if(self.cp.readLastDir() != ""):
            self.qc.load(self.cp.readLastDir())
            self.master.title(self.qc.getTitle())
            self.isLastDirExsit = True
        else:
            self.master.title("跑台練習程式")
         
        self.num_page = 0
        self.num_page_tv = StringVar()
        self.num_page_ans = StringVar()

        fram = Frame(self)
        Button(fram, text="Next slide", command=self.open).pack(side=LEFT)
        Label(fram, textvariable=self.num_page_tv).pack(side=LEFT)
        Button(fram, text="Show answer", command=self.showAns).pack(side=LEFT)
        Label(fram, textvariable=self.num_page_ans).pack(side=LEFT)
        Button(fram, text="Open Package", command=self.OpenPackage).pack(side=RIGHT)
        fram.pack(side=TOP, fill=BOTH)

        self.la = Label(self)
        self.la.pack()

        self.pack()
        #載入第一張照片
        if(self.isLastDirExsit):
            self.open()