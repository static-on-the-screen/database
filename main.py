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
scrollbar = gui.Scrollbar(root)
scrolllist = gui.Listbox(root, yscrollcommand = scrollbar.set, width=150, height=10)
with open('database.txt')as f:
    list = list(f)
for item in list:
        bookname = ''
        for i in range(0,len(item)):
            if item[i] == "*":
                break
            else:
                bookname = (bookname)+str(item[i])
        scrolllist.insert(bookcount,bookname)
scrolllist.place(x=80, y=100)
scrollbar.config(command = scrolllist.yview)
scrollbar.place(x=50, y=100)





root.mainloop()