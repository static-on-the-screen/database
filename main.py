database = open('database.txt', 'r')
import tkinter as gui

bookname = ''
bookcount = 5
titlelist=[]
authorlist=[]
isbnlist=[]
medialist=[]

def addmedia():
    addwindow = gui.Toplevel(root)
    addwindow.title("Add Item")
    addwindow.geometry("500x375")
    addmedialabel= gui.Label(addwindow, text="Add Item", justify="center", font=("Times New Roman", 20, "bold"))
    addmedialabel.pack()

def helppage():
    print("define thissss")

def viewinfo():
    infowindow = gui.Toplevel(root)
    infowindow.title(str(titlelist[item]))
    infowindow.geometry("500x375")
    titlelabel = gui.Label(infowindow, text="Title: "+str(titlelist[item]))
    titlelabel.place(x=20, y=15)
    authorlabel = gui.Label(infowindow, text="Author Name: "+str(authorlist[item]))
    authorlabel.place(x=20, y=40)
    isbnlabel = gui.Label(infowindow, text="ISBN: "+str(isbnlist[item]))
    isbnlabel.place(x=20, y=65)
    typelabel = gui.Label(infowindow, text="Media Type: "+str(medialist[item]))
    typelabel.place(x=20, y=90)

root = gui.Tk()
root.title("NPLDatabase.exe")
root.geometry("900x650")
title1 = gui.Label(root, text="Nondescript Public Library Database", font=("Times New Roman", 25, "bold"))
title1.pack()
addbutton = gui.Button(root, text="Add Item", padx=5, pady=5, cursor="hand2", command=addmedia)
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
            if seperate == 1:
                break
            elif seperate == 0:
                seperate = seperate+1
                continue
        else:
            if seperate == 0:
                continue
            elif seperate == 1:
               author = (author)+str(item[a])       
    authorlist.append(author)

for item in list:
    seperate = 0
    isbn = ''
    for a in range(0, len(item)):
        if item[a] == '*':
            if seperate == 2:
                break
            elif seperate == 0 or seperate == 1:
                seperate = seperate+1
                continue
        else:
            if seperate == 0 or seperate == 1:
                continue
            elif seperate == 2:
               isbn = (isbn)+str(item[a])
    isbnlist.append(isbn)        

for item in list:
    seperate = 0
    mediatype = ''
    for a in range(0, len(item)):
        if item[a] == '*':
            if seperate == 3:
                break
            elif seperate == 0 or seperate == 1 or seperate == 2:
                seperate = seperate+1
                continue
        else:
            if seperate == 0 or seperate == 1 or seperate == 2:
                continue
            elif seperate == 3:
               mediatype = (mediatype)+str(item[a])
    medialist.append(mediatype)        

scrolllist.place(x=80, y=100)
scrollbar.config(command = scrolllist.yview)
scrollbar.place(x=50, y=100)
infobutton = gui.Button(root, text="View Item Information", command=viewinfo, padx=5, pady=5)
infobutton.place(x=375, y=275)




root.mainloop()
