from pymysql import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

db=connect("localhost","root","hp7619","UsersDetail")
cursor=db.cursor()

class Signup_system:
            def __init__(self,root,oldmaster):
                self.root=root
                self.root.title("SignUp")
                self.root.geometry("1350x700+0+0")
                #for images.....................
                self.bg_icon=ImageTk.PhotoImage(file="security-background.jpg")
                self.user_icon=PhotoImage(file="man-user.png")
                self.pass_icon =PhotoImage(file="password.png")
                self.logo_icon = PhotoImage(file="logo.png")
                #variables for entry.............
                self.firstname=StringVar()
                self.age=IntVar()
                self.password=StringVar()
                bg_lb1 = Label(self.root, image=self.bg_icon).pack()

                #login frame......................
                Login_Frame=Frame(self.root,bg="white")

                Login_Frame.place(x=510,y=60,)
                title = Label(Login_Frame, text="SignUp", font=("Industry Inc Detail Fill", 40, "bold"),bg="white", fg="gray", bd=0, relief=GROOVE)
                title.grid(row=0,columnspan=2)

                logo1lbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=1,columnspan=2,pady=20)
                label_first=Label(Login_Frame,text="User name",image=self.user_icon,compound=LEFT,font=("Industry Inc Detail Fill",20,"bold"),bg="white")
                label_first.grid(row=2,column=0,padx=20,pady=10)
                first_entry = Entry(Login_Frame, bd=5, textvariable=self.firstname, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20)
                labelpass = Label(Login_Frame, text="Password", image=self.pass_icon,compound=LEFT,font=("Industry Inc Detail Fill", 20, "bold"), bg="white")
                labelpass.grid(row=6,column=0,padx=20,pady=10)
                label_age = Label(Login_Frame, text="Age", image=self.user_icon, compound=LEFT,font=("Industry Inc Detail Fill", 20, "bold"), bg="white")
                label_age.grid(row=5, column=0, padx=20, pady=10)
                age_entry= Entry(Login_Frame, bd=5, textvariable=self.age, relief=GROOVE, font=("", 15)).grid(row=5, column=1, padx=20)
                pass_entry = Entry(Login_Frame,show="*", bd=5,textvariable=self.password, relief=GROOVE, font=("", 15)).grid(row=6, column=1, padx=20)
                btn_signup=Button(Login_Frame,command=lambda:self.signup(oldmaster),text="SignUp",width=15,\
                                  font=("Industry Inc Detail Fill", 20, "bold"),bg="skyblue",fg="white").grid(row=7,column=1,pady=10)


            def signup(self,oldmaster):
                if self.firstname.get()=="" or self.age.get()=="" or self.password.get()=="":
                    messagebox.showerror("Error","All Fields Are Mandatory")
                else:
                    sql = "INSERT INTO SIGNUP(USENAME, \
                                      PASSWORD,AGE) \
                                      VALUES ('%s','%s','%d')" % \
                          (self.firstname.get(),self.password.get(),self.age.get())
                    try:
                        # Execute the SQL command
                        cursor.execute(sql)
                        # Commit your changes in the database
                        db.commit()
                        messagebox.showinfo("Successfull","You are SignedUp Please Login")
                    except:
                        # Rollback in case there is any error
                        db.rollback()
                        db.close()
                    oldmaster.deiconify()
                    self.root.destroy()

if __name__=="__main__":
    root = Tk()
    obj = Signup_system(root,oldmaster=None)
    root.mainloop()





