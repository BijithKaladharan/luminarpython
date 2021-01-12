from tkinter import messagebox
from tkinter import*
root=Tk()
import mysql.connector
from dbconnectpgm.dbconnect import get_connection
def db_connect(username,password):
    print("inside............")
    db=get_connection()
    cursor=db.cursor()
    try:





        cursor.execute(("select * from users where username=%s AND password=%s"),(username,password))
        user=cursor.fetchone()
        return user

    except Exception as e:
        print(e.args)

    # id="100"
    # name="test1"
    # usertest="test1"
    # userpwd="test2"
    # sql="insert into users(id,name,username,password)values('%s','%s','%s','%s')%(id,name,usertest,userpwd)
    # #db connect logic



def authenticated_user():
    uname=uentry.get()
    pwd=pentry.get()
    user=db_connect(uname,pwd)
    if(user==None):
        messagebox.showerror("invalid user","error")
    else:
        messagebox.showinfo("user successfully logged","logged")


ulabel=Label(root,text="username")
plabel=Label(root,text="password")
uentry=Entry(root)
pentry=Entry(root)

btn=Button(root,text="login",commit=authenticated_user())
ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)

uentry.grid(row=0,column=1)
pentry.grid(row=1,column=1)
btn.grid(row=2,column=1)

root.mainloop()


