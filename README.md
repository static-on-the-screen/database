database = open('database.txt', 'r')
import tkinter as gui

bookname = ''
bookcount = 5
titlelist=[]
authorlist=[]
isbnlist=[]
medialist=[]
<<<<<<< HEAD
mediaoptions=["Book", "CD", "DVD", "Magazine"]
=======
>>>>>>> origin/master

def addmedia():
    addwindow = gui.Toplevel(root)
    addwindow.title("Add Item")
    addwindow.geometry("500x375")
    addmedialabel= gui.Label(addwindow, text="Add Item", justify="center", font=("Times New Roman", 20, "bold"))
    addmedialabel.pack()
<<<<<<< HEAD
    titlelabel = gui.Label(addwindow, text="Title:")
    titlelabel.pack()
    addtitle = gui.Entry(addwindow)
    addtitle.pack()
    surnamelabel = gui.Label(addwindow, text="Author Surname:")
    surnamelabel.pack()
    addsurname = gui.Entry(addwindow)
    addsurname.pack()
    namelabel = gui.Label(addwindow, text="Author's First Name:")
    namelabel.pack()
    addname = gui.Entry(addwindow)
    addname.pack()
    isbnlabel = gui.Label(addwindow, text="ISBN:")
    isbnlabel.pack()
    addisbn = gui.Entry(addwindow)
    addisbn.pack()
    medialabel = gui.Label(addwindow, text="Media Type:")
    addmedia = gui.OptionMenu(addwindow, *mediaoptions)
    medialabel.pack()
    addmedia.pack()

=======
>>>>>>> origin/master

def helppage():
    print("define thissss")

def viewinfo():
<<<<<<< HEAD
    item = scrolllist.curselection()
    item = item[0]
=======
>>>>>>> origin/master
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
<<<<<<< HEAD
               author = (author)+str(item[a])
=======
               author = (author)+str(item[a])       
>>>>>>> origin/master
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
<<<<<<< HEAD
    isbnlist.append(isbn)
=======
    isbnlist.append(isbn)        
>>>>>>> origin/master

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
<<<<<<< HEAD
    medialist.append(mediatype)
=======
    medialist.append(mediatype)        
>>>>>>> origin/master

scrolllist.place(x=80, y=100)
scrollbar.config(command = scrolllist.yview)
scrollbar.place(x=50, y=100)
infobutton = gui.Button(root, text="View Item Information", command=viewinfo, padx=5, pady=5)
infobutton.place(x=375, y=275)




root.mainloop()
