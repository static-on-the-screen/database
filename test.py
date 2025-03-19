database = open('database.txt', 'r')
import tkinter as gui

bookname = ''
bookcount = 5
def helppage():
    print("define thissss")


root = gui.Tk()
root.title("NPLDatabase.exe")
root.geometry("900x650")
title1 = gui.Label(root, text="Nondescript Public Library Database", font=("Times New Roman", 25, "bold"))
title1.pack()
addbutton = gui.Button(root, text="Add Item", padx=5, pady=5, cursor="hand2")
addbutton.place(x=10, y=50)
deletebutton = gui.Button(root, text="Delete Item", padx=5, pady=5, cursor="hand2")
deletebutton.place(x=80, y=50)
helpbutton = gui.Button(root, text="Help", padx=5, pady=5, cursor="hand2")
helpbutton.place(x=845, y=50)
editbutton = gui.Button(root, text="Edit Item", padx=5, pady=5, cursor="hand2")
editbutton.place(x=161, y=50)
entry = gui.Text(root, height=10, width=50)
entry.pack(side='left', fill='both', expand=True)
scrollbar = gui.Scrollbar(root, orient='vertical', command=entry.yview)
scrollbar.pack(side='right', fill='y')
entry.config(yscrollcommand=scrollbar.set)
for i in range(0,20):
    f = open('database.txt')
    line = len(f.readlines())
    content = f.readlines()
    for j in range(0, len(f.readlines())):
        entry.insert('end', str(content[j]))




root.mainloop()