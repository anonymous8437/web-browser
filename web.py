import tkinter
from tkinter import *
import webbrowser

root=Tk()
root.title('Web Browser')
root.resizable(0,0)
root.config(width='155',height='150',bg='gray')

entry=Entry(root,width='22')
entry.place(x='10',y='10')

label=Label(root,text='Enter a URl here!')
label.place(x='32',y='30')

button=Button(root,text='Search',bg='red',fg='white')
button.place(x='55',y='75')

button2=Button(root,text='settings',bg='blue',fg='white')
button2.place(x='52.5',y='120')



def search(event):
    webbrowser.open(entry.get())

button.bind('<ButtonPress>',search)

#===================settings=========================================
def settings(event):
    root2=Tk()
    root2.title('settings')
    root2.resizable(0,0)
    root2.config(width='160',height='150',bg='white')
    button3=Button(root2,text='    ',bg='pink')
    button3.place(x='10',y='25')
    button4=Button(root2,text='    ',bg='gray')
    button4.place(x='30',y='25')
    button5=Button(root2,text='    ',bg='yellow')
    button5.place(x='50',y='25')
    button6=Button(root2,text='    ',bg='black')
    button6.place(x='70',y='25')
    button7=Button(root2,text='    ',bg='brown')
    button7.place(x='90',y='25')
    button8=Button(root2,text='    ',bg='green')
    button8.place(x='110',y='25')
    label=Label(root2,text='Background color: ',bg='white')
    label.place(x='10',y='3')

    label2=Label(root2,text='Search color: ',bg='white')
    label2.place(x='10',y='75')
    button9=Button(root2,text='    ',bg='pink')
    button9.place(x='10',y='100')
    button10=Button(root2,text='    ',bg='gray')
    button10.place(x='30',y='100')
    button11=Button(root2,text='    ',bg='yellow')
    button11.place(x='50',y='100')
    button12=Button(root2,text='    ',bg='black')
    button12.place(x='70',y='100')
    button13=Button(root2,text='    ',bg='brown')
    button13.place(x='90',y='100')
    button14=Button(root2,text='    ',bg='green')
    button14.place(x='110',y='100')

    def b1(event):
        root.config(bg='pink')
    button3.bind('<ButtonPress>',b1)
    def b2(event):
        root.config(bg='gray')
    button4.bind('<ButtonPress>',b2)
    def b3(event):
        root.config(bg='yellow')
    button5.bind('<ButtonPress>',b3)
    def b4(event):
        root.config(bg='black')
    button6.bind('<ButtonPress>',b4)
    def b5(event):
        root.config(bg='brown')
    button7.bind('<ButtonPress>',b5)
    def b6(event):
        root.config(bg='green')
    button8.bind('<ButtonPress>',b6)

    def s1(event):
        button.config(bg='pink')
    button9.bind('<ButtonPress>',s1)
    def s2(event):
        button.config(bg='gray')
    button10.bind('<ButtonPress>',s2)
    def s3(event):
        button.config(bg='yellow')
    button11.bind('<ButtonPress>',s3)
    def s4(event):
        button.config(bg='black')
    button12.bind('<ButtonPress>',s4)
    def s5(event):
        button.config(bg='brown')
    button13.bind('<ButtonPress>',s5)
    def s6(event):
        button.config(bg='green')
    button14.bind('<ButtonPress>',s6)
    
                                   

button2.bind('<ButtonPress>',settings)





