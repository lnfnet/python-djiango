#!/usr/bin/env python3

from tkinter import *

class Application(Frame):
    """buid the basec window frame template"""

    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.varSausage=IntVar()
        self.varPepp=IntVar()
        self.create_widgets()

    def create_widgets(self):
        self.label1=Label(self,text='Welcome to my window！')
        self.label1.grid(row=0,column=0,sticky=W)
        self.check1 = Checkbutton(self,text='Sausage',variable=self.varSausage)
        self.check2 = Checkbutton(self,text='Pepperoni',variable=self.varPepp)
        self.check1.grid(row=1,column=0,sticky = W)
        self.check2.grid(row=2,column=0,sticky = W)
        self.button1 = Button(self,text='Click me',command=self.display)
        self.button1.grid(row=3,column=0,sticky = W)
        self.text1=Entry(self)
        self.text1.grid(row=4)
        self.listbox1 = Listbox(self,selectmode=EXTENDED)
        items = ['Item One','Item Two','Item Three']
        for item in items:
            self.listbox1.insert(END,item)
        self.listbox1.grid(row=7)

        self.button2 = Button(self,text='Clear result',command=self.clear)
        self.button2.grid(row=5)
        self.button3 = Button(self,text='Convert',command=self.convert)
        self.button3.grid(row=5,column=1)

        self.text2=Text(self,width=20,height=10)
        self.text2.grid(row=6)

        menubar=Menu(self)
        filemenu=Menu(menubar)
        filemenu.add_command(label="Calculate",command=self.display)
        filemenu.add_command(label="Rest",command=self.clear)
        menubar.add_cascade(label="File",menu=filemenu)
        menubar.add_cascade(label="Exit",command=root.quit)
        root.config(menu=menubar)
        
        self.text2.focus_set()
        
    def convert(self):
        """ Retrieve the text and convert to upper case"""
        varText = self.text1.get()
        varReplaced=varText.upper()
        self.text1.delete(0,END)
        self.text1.insert(END,varReplaced)

        varText2 = self.text2.get("1.0",END)
        varReplaced2=varText2.upper()
        self.text2.delete("1.0",END)
        self.text2.insert(END,varReplaced2)
        
    def clear(self):
        """Clear the Entry form"""
        self.text1.delete(0,END)        
        self.text2.delete("1.0",END)
        self.text2.focus_set()    

    def display(self):
        """Event handler for the button"""
        print("The button in the window was clicked")
        if(self.varSausage.get()):
            print('You want sausage')
        if(self.varPepp.get()):
            print('you want Pepperoni')
        if(not self.varPepp.get() and not self.varSausage.get()):
            print("You do not want anything on your pizza!")
        print('---------------------------------------')


        items = self.listbox1.curselection()
        for item in items:
            strItem = self.listbox1.get(item)
            self.text2.insert(END,strItem)
            self.label1.insert(strItem)
            print(strItem)
        print("________________________________________")

root=Tk()
root.title("this is my fist GUI")
root.geometry('300x500')
app = Application(root)
app.mainloop()
