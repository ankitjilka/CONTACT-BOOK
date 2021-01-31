from tkinter import *
import sqlite3
from tkinter import messagebox

win = Tk()
win.title('CONTACT-BOOK')
win.geometry('900x640')
win.minsize(900,640)
win.maxsize(900,640)
win.configure(bg='#EFFCE8')
#win.iconbitmap(r"mypic.ico")

h_canvas = Canvas(win,width=900,height = 2 , background='black')
h_canvas.place(x=0,y=490)

v_canvas = Canvas(win,width=2,height=340 , background = 'black')
v_canvas.place(x=445,y=150)

pic = PhotoImage(file='C:\pic.png')
piclabel= Label(win,image=pic,width=190,height=95)
piclabel.pack()

pic2 = PhotoImage(file='C:\mypic.png')
win.iconphoto(False,pic2)
title = Label(win,text="CONTACT-BOOK",bg='#212121',fg='red', font=('Arial Rounded MT',34,'bold'))
title.pack(fill='x')

#conn = sqlite3.connect('app4.db')
#cur = conn.cursor()
#cur.execute("create table t4(id integer primary key, name text not null, phno integer unique not null,email text , city text)")
#conn.commit()
#cur.close()

def insert1():
    conn = sqlite3.connect("app2.db")
    cur = conn.cursor()
    name1= entry_name.get()
    if name1 != "":
        pass
    else:
        messagebox.showwarning("Warning !! ", "PLEASE  ENTER  A  NAME")
        entry_name.delete(0, END)
        entry_name.focus()
        return

    phn1 = entry_phno.get()
    cur.execute("select * from t2 where phno = '%s'"%phn1)
    var = cur.fetchall()
    if len(var) == 0 and phn1.isdigit() == 1 and len(phn1) == 10:
        pass
    else:
      if len(var) != 0:
         messagebox.showinfo("ALERT !! ", "THIS  TYPE  OF  PH_NO  ALREADY EXSISTS ")
         entry_phno.delete(0, END)
         entry_phno.focus()
         return
      elif phn1.isdigit() == 0:
         messagebox.showwarning("Warning !! ", "PLEASE  ENTER  DIGITS  IN  PH_NO")
         entry_phno.delete(0, END)
         entry_phno.focus()
         return
      else:
          messagebox.showwarning("Warning !! ", "PLEASE  ENTER  EXACTLY  10  DIGITS")
          entry_phno.delete(0, END)
          entry_phno.focus()
          return

    email1 = entry_email.get()
    if len(email1) != 0 and email1.endswith("@gmail.com") == 0:
        messagebox.showwarning("Warning !! ", "PLEASE  ENTER  VALID  EMAIL_ID")
        entry_email.delete(0, END)
        entry_email.focus()
        return

    city1 = entry_city.get()
    cur.execute("insert into t2 (name,phno,email,city) values(?,?,?,?)",(name1,phn1,email1,city1,))
    messagebox.showinfo("CONGRATULATION ","YOUR  DATA  INSERTED  SUCCESSFULLY !!")

    entry_name.delete(0, END)
    entry_phno.delete(0, END)
    entry_email.delete(0, END)
    entry_city.delete(0, END)
    conn.commit()
    conn.close()
    entry_name.focus()

def contacts():
    q_all = "select * from t2"
    all_in_one(q_all)

def find():
    e1 = e_name.get()
    if e1 == "":
        messagebox.showwarning("ALERT !! ", "PLEASE  ENTER  A  NAME  WHICH  DATA YOU  WANT  TO  FIND ")
        e_name.focus()
        return
    else:
       q_find = "select * from t2 where name = '%s'"%e1
       all_in_one(q_find)
       e_name.delete(0,END)
       e_name.focus()

def dlt():
    e2 = e_name.get()
    conn = sqlite3.connect("app2.db")
    cur = conn.cursor()
    cur.execute("select * from t2 where name = '%s'"%e2)
    values = cur.fetchall()
    if e2 == "":
         messagebox.showwarning("WARNING !! ", "PLEASE ENTER  A  NAME  WHICH  DATA  YOU  WANT  TO  DELETE ")
         e_name.focus()
         return
    elif len(values)== 0:
        messagebox.showinfo("ALERT !! ","NO  SUCH  TYPE  OF  DATA ... ")
        e_name.delete(0,END)
        e_name.focus()
        return
    ans = messagebox.askquestion('ALERT !! ',"ARE  YOU  SURE  WANT  TO  DELETE  A  RECORD ? ")
    if ans == 'yes':
        cur.execute("delete from t2 where name = ?",(e2,))
    e_name.delete(0,END)
    conn.commit()
    conn.close()

def dlt_all():
   conn = sqlite3.connect("app2.db")
   cur = conn.cursor()
   cur.execute("select * from t2")
   values = cur.fetchall()
   if len(values) == 0:
       messagebox.showinfo("ALERT !! ", "NO  DATA  FOUND ... ")
       return
   ans = messagebox.askquestion("ALERT !!","ARE  YOU  SURE  WANT  TO  DELETE  ALL  RECORDS .. ")
   if ans == 'yes':
       cur.execute("delete from t2")
       messagebox.showinfo("Notification !! ", "YOUR  ALL  DATA  DELETED  SUCCESSFULLY !! ")
   conn.commit()
   conn.close()

def all_in_one(var):
    conn = sqlite3.connect("app2.db")
    cur = conn.cursor()
    cur.execute(var)
    r = cur.fetchall()
    if len(r) == 0:
        messagebox.showinfo("WARNING !! ", "NO DATA FOUND ")
        e_name.delete(0,END)
        e_name.focus()
        return

    nx = Tk()
    nx.geometry("600x600")
    nx.maxsize(600,600)
    nx.minsize(600,600)
    nx.title("CONTACTS")

    title_label = Label(nx,text="Contacts" , bg='#212121',fg='red', font=('Arial Rounded MT',35,'bold') , padx=200 ,pady=6)
    title_label.place(x=0,y=0)
    num = 120
    for i in r:
        id_f = Label(nx, text=i[0], font=("Arial", 11, 'italic'))
        id_f.place(x=15, y=num)

        name_f = Label(nx, text=i[1], font=("Arial", 11, 'italic'))
        name_f.place(x=75, y=num)

        phno_f = Label(nx, text=i[2], font=("Arial", 11, 'italic'))
        phno_f.place(x=190, y=num)

        email_f = Label(nx, text=i[3], font=("Arial", 11, 'italic'))
        email_f.place(x=319, y=num)
        city_f = Label(nx, text=i[4], font=("Arial", 11, 'italic'))
        city_f.place(x=510, y=num)

        num = num + 40

    conn.commit()
    conn.close()

    l1 = Label(nx, text="Id", font=("Arial Rounded MT", 14, "bold"), fg="#0147FA")
    l1.place(x=15 , y = 80)

    l2 = Label(nx, text="Name", font=("Arial Rounded MT", 14, "bold"), fg="#0147FA")
    l2.place(x=75 , y = 80)

    l3 = Label(nx, text="Ph_no", font=("Arial Rounded MT", 14, "bold"), fg="#0147FA")
    l3.place(x=190, y=80)

    l4 = Label(nx, text="Email_id", font=("Arial Rounded MT", 14, "bold"), fg="#0147FA")
    l4.place(x=320, y=80)

    l5 = Label(nx, text="City", font=("Arial Rounded MT", 14, "bold"), fg="#0147FA")
    l5.place(x=510, y=80)


name = Label(win,text='Name',bg='#EFFCE8',fg='#551011',font=('Elephant',13,'italic'))
name.place(x=30,y=210)
entry_name = Entry(win ,width = 35, bd = 3)
entry_name.place(x = 125,y=210)
entry_name.focus()

phno = Label(win,text='Ph_No',bg='#EFFCE8',fg='#551011',font=('Elephant',13,'italic'))
phno.place(x=30,y=252)
entry_phno= Entry(win ,  width = 35, bd = 3)
entry_phno.place(x=125,y=252)

email = Label(win,text='Email_id',bg='#EFFCE8',fg='#551011',font=('Elephant',13,'italic'))
email.place(x=30,y=294)
entry_email = Entry(win,width=35,bd=3)
entry_email.place(x=125,y=294)

city = Label(win,text='City',bg='#EFFCE8',fg='#551011',font=('Elephant',13,'italic'))
city.place(x=30,y=336)
entry_city = Entry(win,width=35,bd=3)
entry_city.place(x=125,y=336)



find_name = Label(win , text = "Name" , bg='#EFFCE8',fg='#551011',font=('Elephant',13,'italic'))
find_name.place(x=530 , y = 235)
e_name = Entry(win , width = 35,bd=3)
e_name.place(x=610,y=235)

button_add = Button(win,text= "ADD" , fg="#DC143C" , bg = "#CDD704" , width=20, height = 2 , font=('Britannic',13,'bold'),command = insert1)
button_add.place(x=60,y=380)

show_button = Button(win,text= "SHOW ALL CONTACTS" , fg="#DC143C" , bg = "#CDD704" , width=25, height = 2 , font=('Britannic',13,'bold'),command = contacts)
show_button.place(x=145,y=520)

find_button = Button(win,text = "FIND" , fg = "#DC143C" , bg = "#CDD704" , width=20, height = 2 , font=('Britannic',13,'bold'),command = find)
find_button.place(x=560,y=295)

dlt_button = Button(win,text = "DELETE" , fg = "#DC143C" , bg = "#CDD704" , width=20, height = 2 , font=('Britannic',13,'bold'),command = dlt)
dlt_button.place(x=560,y=380)

dlt_all = Button(win,text = "DELETE ALL CONTACTS" , fg = "#DC143C" , bg = "#CDD704" , width=25, height = 2 , font=('Britannic',13,'bold'),command = dlt_all)
dlt_all.place(x=480,y=520)

devloper = Label(win,text="devloped  by  ANKIT JILKA",fg="#F22C1E" ,bg='#2F4F2F', font=('Gill Sans',22,'bold'))
devloper.pack(side='bottom',fill='x')

win.mainloop()     # running gui app infinite time
