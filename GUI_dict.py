from tkinter import *
from difflib import get_close_matches
import database

words_list=[]

def result():
    list1.delete(0,END)
    for res in database.search(word.get()):
            list1.insert(END,(res))
            print(type(word))
    
def suggests():
    for res in list(database.view()):
        word_row  = str(res)
        new=""
        word_row_indexed =  word_row.rindex('\'',1)
        words_list.append(word_row[2:word_row_indexed])
    sug=get_close_matches(word.get(),words_list,n=1)
    entry2.delete(0,END)
    entry2.insert(END,sug)
    list1.delete(0,END)
    for x in sug:
        new+=x
    for res in database.search(new):
        list1.insert(END,res)
   






    

window=Tk()
window.title("Dictonary")
lab=Label(text="word")
lab.grid(row=0,column=0)

lab2=Label(text="suggestion")
lab2.grid(row=1,column=0)

word=StringVar()
entry=Entry(textvariable=word)
entry.grid(row=0,column=1)

sug=StringVar()
entry2=Entry(textvariable=sug)
entry2.grid(row=1,column=1)


list1=Listbox(height=6,width=29)
list1.grid(row=2,column=1,rowspan=6,columnspan=2)

sb=Scrollbar()
sb.grid(row=1,column=4,columnspan=4,rowspan=6)

list1.configure(xscrollcommand=sb.set)
sb.configure(command=list1.xview)

b=Button(text="fetch",width=8,command=result)
b.grid(row=0,column=3)

b1=Button(text="suggest",width=8,command=suggests)
b1.grid(row=1,column=3)

b2=Button(text="close",width=8,command=window.destroy)
b2.grid(row=7,column=3)


window.mainloop()
