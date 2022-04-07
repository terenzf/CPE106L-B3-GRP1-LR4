import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

#Root Window
root = tk.Tk()
root.title('Tkinter Text File Reader')
root.resizable(False, False)
root.geometry('300x150')

def select_file():

    target=fd.askopenfilename(filetypes=[(("Text files", "*.txt"))]) 
    for line in open(target):
        print(line, end='')
    print('***The filename and content has been displayed.***\n')

    showinfo(
        title='Selected File',
        message=target
    )

#File Open Button
open_button = ttk.Button(
    root,
    text='Open a Text File',
    command=select_file
)

open_button.pack(expand=True)

#Execute
root.mainloop()


