database = open('database.txt', 'r')
import tkinter as gui

bookname = ''
bookcount = 5
titlelist=[]
authorlist=[]
def helppage():
    print("define thissss")

def viewinfo():
    print(authorlist)
    with open('database.txt') as f:
        for item in scrolllist.curselection():
            print("You have selected"+str(titlelist[item]))
    infowindow = gui.Toplevel(root)
    infowindow.title(str(titlelist[item]))
    infowindow.geometry("500x375")
    titlelabel = gui.Label(infowindow, text="Title: "+str(titlelist[item]))
    titlelabel.place(x=20, y=15)
    authorlabel = gui.Label(infowindow, text="Author Name: "+str(authorlist[item]))
    authorlabel.place(x=20, y=30)




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
scrolllist = gui.Listbox(root, yscrollcommand = scrollbar.set, width=125, height=10)
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
        titlelist.append(bookname)

for item in list:
    seperate = 0
    author = ''
    for a in range(0, len(item)):
        if item[a] == '*':
            seperate = seperate+1
        else:
            if seperate > 2:
                continue
            elif seperate == 2:
               author = author+str(item[a])
            if seperate < 2:
                break
        authorlist.append(author)
scrolllist.place(x=80, y=100)
scrollbar.config(command = scrolllist.yview)
scrollbar.place(x=50, y=100)
infobutton = gui.Button(root, text="View Item Information", command=viewinfo, padx=5, pady=5)
infobutton.place(x=375, y=275)




root.mainloop()