from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from pymysql import *
from Tooltip import CreateToolTip
from datetime import datetime
db=connect("localhost","root","hp7619","UsersDetail")
cursor=db.cursor()

class PS:
    def __init__(self,root,username):
        self.root=root
        self.username=username
        self.root.title("Presence System")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg='gray')
        title = Label(self.root, text="Welcome to Presence System", font=("Industry Inc Detail Fill", 40, "bold"),\
                       fg="light cyan",bg="gray", bd=0, relief=GROOVE)
        title.place(x=310,y=10)
        sql="SELECT USERNAME FROM LOGIN WHERE Timeout is NULL"
        cursor.execute(sql)
        result=cursor.fetchall()
        PS_Frame=Frame(self.root,bg="gray")
        PS_Frame.place(x=200,y=70,)
        for i in range(len(result)):
            label=Label(PS_Frame, text=result[i][0][0], font=("Industry Inc Detail Fill", 25, "bold"),\
                       fg="light cyan",bg="blue", bd=8, relief=GROOVE,padx=20,pady=10)
            label.grid(row=0,column=i,padx=20,pady=10)
            CreateToolTip(label,result[i][0])
        b1=Button(self.root,text="Log Out",fg="white",bg="green",font="bold",command=self.button)
        b1.place(x=1250,y=10)
        label=Label(self.root, text="Previous Users:-", font=("Industry Inc Detail Fill", 25, "bold"),\
                       fg="light cyan",bg="gray", bd=0, relief=GROOVE,padx=20,pady=10)
        label.place(x=200,y=200)
        T_Frame=Frame(self.root,bg="gray")
        T_Frame.place(x=200,y=250)
        sq1="SELECT * FROM LOGIN WHERE Timeout is NOT NULL"
        cursor.execute(sq1)
        results=cursor.fetchall()
        col=['Username','InTime','OutTime']
        for j in range(len(results[0])):
            b = Entry(T_Frame, text="",fg="black",bg="gray",bd=0)
            b.grid(row=0, column=j)
            b.insert(END,col[j])
        for i in range(len(results)):
            for j in range(len(results[0])):
                b = Entry(T_Frame, text="",fg="light cyan",bg="gray",bd=0)
                b.grid(row=i+1, column=j)
                b.insert(END,results[i][j])
        
            

    def button(self):
        sq="UPDATE LOGIN SET Timeout=%s WHERE Username=%s"%(datetime.now(),self.username)
        cursor.execute ("""
                        UPDATE LOGIN
                        SET Timeout=%s
                        WHERE Username=%s
                        """, (datetime.now(),self.username))

        db.commit()
        self.root.quit()
        self.root.destroy()
    
            
        
if __name__=="__main__":
    root = Tk()
    obj = PS(root)
    root.mainloop()