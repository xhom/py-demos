# coding=UTF-8

from Tkinter import *

root = Tk() # 创建GUI

list = ["C","Java","PHP","Python"]
movie = ["CSS","jQuery",'Bootstrap']

listb = Listbox(root)
listb2 = Listbox(root)
for item in list:
    listb.insert(0, item)

for item in movie:
    listb2.insert(0,item)

listb.pack()
listb2.pack()

root.mainloop() # 启动GUI