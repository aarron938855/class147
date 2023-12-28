# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:38:52 2023

@author: user
"""

from tkinter import *

root=Tk()
root.title("ENCRYPTION WITH ASCII CODE")

root.geometry("1000x500")
root.configure(background = 'light blue')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.3,anchor=CENTER)

label = Label(root, text = "NAME IN ASCII : ",bg="white",fg="black")
label_encrypted = Label(root, text = "ENCRYPTED NAME : ",bg="white",fg="black")

def convert():
    input_word=enter_word.get()
    for letter in input_word : 
        label["text"] += str(ord(letter)) + "  "
       
    for letter in label.get :
        ascii_value = int(ord(letter))
        encrypted = ascii_value-1
        encrypted_word = dtr(chr(sncrypted))
        label["text"] += str(ord(letter))
btn=Button(root,text="Display the Ascii code and Encrypted value",command=convert,bg='dark blue',fg='white')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER) 
label_encrypted.place(relx=0.5,rely=0.7,anchor=CENTER) 
root.mainloop()   
