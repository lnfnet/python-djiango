#!/usr/bin/env python3

from tkinter import *
import smtplib

class Application(Frame):
    """Build the basic window frame template!"""

    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        menubar = Menu(self)
        menubar.add_command(label='Send',command=self.send)
        menubar.add_command(label='Quit',command=root.quit)
        self.label1=Label(self,text="The Quick E-mailer")
        self.label1.grid(row=0,columnspan=3)
        self.label2=Label(self,text="Entry the recipients:")
        self.label2.grid(row=2,column=0)
        self.label3=Label(self,text="Entry the Subject:")
        self.label3.grid(row=3,column=0)
        self.label4=Label(self,text="Enter your message here:")
        self.label4.grid(row=4,column=0)
        
        self.recipients=Entry(self)
        self.subj=Entry(self)
        self.body=Text(self,width=50,height=10)

        self.recipients.grid(row=2,column=1,sticky=W)
        self.subj.grid(row=3,column=1,sticky=W)
        self.body.grid(row=5,column=0,columnspan=2)
        
        self.button1=Button(self,text="Send mail",command=self.send)
        self.button1.grid(row=6,column=6,sticky=W)
        self.recipients.focus_set()
        root.config(menu=menubar)

    def send(self):
        """Retrieve the text ,build the message,and send it"""
        server="smtp.163.com"
        port=587
        sender="lnfnet2005@163.com"
        password='gkimfmnui1A'
        to=self.recipients.get()
        tolist=to.split(',')
        subject=self.subj.get()
        body=self.body.get('1.0',END)
        header='To:'+ to +'\n'
        header=header + 'From:'+ sender + '\n'
        header=header + 'Subject:'+ subject + '\n'
        message=header + body
        print(message)

        smtpserver=smtplib.SMTP(server,port)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(sender,password)
        smtpserver.sendmail(sender,tolist,message)
        smtpserver.quit()
        self.body.delete('1.0',END)
        self.body.insert(END,'Message sent')
        
root=Tk()
root.title("The Quick Email")
root.geometry('500x300')
app=Application(root)
app.mainloop()
