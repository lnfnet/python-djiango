#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *           # ���� Tkinter ��
root = Tk()                     # �������ڶ���ı���ɫ
                                # ���������б�
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  ���������б����
listb2 = Listbox(root)
for item in li:                 # ��һ��С������������
    listb.insert(0,item)

for item in movie:              # �ڶ���С������������
    listb2.insert(0,item)

listb.pack()                    # ��С�������õ���������
listb2.pack()
root.mainloop()                 # ������Ϣѭ��
