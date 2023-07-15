'''
파일명: Ex24-1-Tkinter.py

tkinter
    Python에서 기본적으로 제공하는 GUI(Graphical User Interface)
    프로그램 모듈

    tkinter 모듈은 간단하게 GUI 프로그램 만들기 좋다.
    모듈 pyQt
'''

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

entry = tk.Entry(root)
entry.pack()

text = tk.Text(root)
text.pack()

checkbox_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Check me!", variable=checkbox_var)
checkbutton.pack()

var = tk.StringVar()
var.set("option1")
radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=var, value="option1")
radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=var, value="option2")
radiobutton1.pack()
radiobutton2.pack()

scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
scale.pack()

spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

combo = ttk.Combobox(root, values=["Item 1", "Item 2", "Item 3"])
combo.pack()

def onClick():
    print("Button Click!")
    s_entry = entry.get()
    s_text = text.get('1.0', tk.END)
    s_radiobutton = var.get()
    i_checkbox_var = checkbox_var.get()
    i_scale = scale.get()
    i_spinbox = spinbox.get()
    s_combo = combo.get()

    print(f's_entry: {s_entry}')
    print(f's_text: {s_text}')
    print(f's_radiobutton: {s_radiobutton}')
    print(f's_checkbox_var: {i_checkbox_var}')
    print(f'i_scale: {i_scale}')
    print(f'i_spinbox: {i_spinbox}')
    print(f's_combo: {s_combo}')

button = tk.Button(root, text="Click me!", command=onClick)
button.pack()




# 실행코드
root.mainloop()


