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

try:
    from Tkinter import *
    import tkFileDialog as filedialog
except ImportError:
    from tkinter import *
    from tkinter import filedialog
import PIL.ImageTk
from PIL import Image
import random, logging, json


class Viewer(Frame):
    def LoadAnsConfig(self):
        configName = "config.json"

        self.fp = open(configName,"r",encoding="utf-8")
        jsondata = self.fp.read()
        ansdict = json.loads(jsondata)
        self.fp.close()
        return ansdict

    def chg_image(self):
        
        if self.im.mode == "1":  # bitmap image
            self.img = PIL.ImageTk.BitmapImage(self.im, foreground="white")
        else:              # photo image
            scale_w = 475
            scale_h = 363
            #self.im = self.im.resize((scale_h, scale_w), Image.ANTIALIAS)
            self.img = PIL.ImageTk.PhotoImage(self.im)
        self.la.config(image=self.img, bg="#000000",
                       width=self.img.width(), height=self.img.height())

    def open(self):
        #filename = filedialog.askopenfilename()
        self.fileNo = random.randint(1, self.total)
        filename = r"media/image" + str(self.fileNo) + "_c.jpg"
        if 1 != "":
            self.im = PIL.Image.open(filename)
        self.chg_image()
        self.num_page_ans.set("****")
        self.num_page_tv.set("Slide: " + str(self.fileNo))

    def showAns(self):
        self.num_page_ans.set(self.ansdict["ans"][str(self.fileNo)])

    def __init__(self, master=None):
        self.ansdict = self.LoadAnsConfig()

        Frame.__init__(self, master)
        self.master.title(self.ansdict["title"])  

        self.num_page = 0
        self.num_page_tv = StringVar()
        self.num_page_ans = StringVar()
        self.total = len(self.ansdict["ans"])

        fram = Frame(self)
        Button(fram, text="Next slide", command=self.open).pack(side=LEFT)
        Label(fram, textvariable=self.num_page_tv).pack(side=LEFT)
        Button(fram, text="Show answer", command=self.showAns).pack(side=LEFT)
        Label(fram, textvariable=self.num_page_ans).pack(side=LEFT)
        fram.pack(side=TOP, fill=BOTH)

        self.la = Label(self)
        self.la.pack()

        self.pack()
        #載入第一張照片
        self.open()


if __name__ == "__main__":
    app = Viewer()
    app.mainloop()
