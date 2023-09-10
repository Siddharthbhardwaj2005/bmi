#!/usr/bin/env python
# coding: utf-8

# In[12]:


import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry('400x300')
def cal_bmi():
    weight = float(e1.get())
    height = float(e2.get())
    bmi = weight/(height*height)
    bmi = round(bmi, 2)
    message = 'BMI is: ' + str(bmi)
    messagebox.showinfo('BMI', message)
var1 = tk.Label(root, text = 'Enter weight in kg')
var1.pack()
e1 = tk.Entry(root)
e1.pack()
var2 = tk.Label(root, text = 'Enter height in meter')
var2.pack()
e2 = tk.Entry(root)
e2.pack()
b1 = tk.Button(root, text = 'Calculate BMI', command = cal_bmi)
b1.pack()
b2 = tk.Button(root, text = 'Exit', command = root.destroy)
b2.pack()
root.mainloop()
    


# In[ ]:




