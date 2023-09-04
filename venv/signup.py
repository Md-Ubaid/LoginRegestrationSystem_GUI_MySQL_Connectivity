from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#Functionality Part

def clear():
    emailentry.delete(0,END)
    UserNameEntry.delete(0,END)
    PasswordEntry.delete(0,END)
    CPasswordEntry.delete(0,END)
    check.set(0)


def login_page():
    signup_window.destroy()
    import signin


def connect_database():
    if emailentry.get()=='' or UserNameEntry.get()=='' or PasswordEntry.get()=='' or CPasswordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif PasswordEntry.get()!=CPasswordEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please Accept Our Terms And Conditions')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='admin')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return
        try:
            query='create database Registration_Data'
            mycursor.execute(query)
            query='use Registration_Data'
            mycursor.execute(query)
            query='create table data(Id int auto_increment primary key not null, User_Email varchar(50), Username varchar(30), User_Password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use registration_data')
        query='select*from data where Username=%s'
        mycursor.execute(query,(UserNameEntry.get()))

        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror('Error','Username Already Exists')
        
        else:
            query='insert into data(User_Email,Username,User_Password) values(%s,%s,%s)'
            mycursor.execute(query,(emailentry.get(),UserNameEntry.get(),PasswordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
            signup_window.destroy()
            import signin






signup_window=Tk()
signup_window.title('Sign Up')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='venv/bg.jpg')


bgLabel=Label(signup_window,image=background)
bgLabel.grid()


frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)



heading=Label(frame,text='Create An Account',font=('Microsoft Yehei UI Light',22,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)



emaillabel=Label(frame,text='Email',font=('Microsoft Yehei UI Light',11,'bold'),bd=0,fg='firebrick1',bg='white')
emaillabel.grid(row=1,column=0,padx=25,pady=(10,0),sticky='w')

emailentry=Entry(frame,width=30,font=('Microsoft Yehei UI Light',11,'bold'),bg='firebrick1',fg='white')
emailentry.grid(row=2,column=0,sticky='w',padx=25)


UserName=Label(frame,text='Username',font=('Microsoft Yehei UI Light',11,'bold'),bd=0,fg='firebrick1',bg='white')
UserName.grid(row=3,column=0,padx=25,pady=(10,0),sticky='w')

UserNameEntry=Entry(frame,width=30,font=('Microsoft Yehei UI Light',11,'bold'),bg='firebrick1',fg='white')
UserNameEntry.grid(row=4,column=0,sticky='w',padx=25)


Password=Label(frame,text='Password',font=('Microsoft Yehei UI Light',11,'bold'),bd=0,fg='firebrick1',bg='white')
Password.grid(row=5,column=0,padx=25,pady=(10,0),sticky='w')

PasswordEntry=Entry(frame,width=30,font=('Microsoft Yehei UI Light',11,'bold'),bg='firebrick1',fg='white')
PasswordEntry.grid(row=6,column=0,sticky='w',padx=25)


CPassword=Label(frame,text='Confirm Password',font=('Microsoft Yehei UI Light',11,'bold'),bd=0,fg='firebrick1',bg='white')
CPassword.grid(row=7,column=0,padx=25,pady=(10,0),sticky='w')

CPasswordEntry=Entry(frame,width=30,font=('Microsoft Yehei UI Light',11,'bold'),bg='firebrick1',fg='white')
CPasswordEntry.grid(row=8,column=0,sticky='w',padx=25)


check=IntVar()
terms=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yehei UI Light',11,'bold'),fg='firebrick1',activeforeground='firebrick1',bg='white',activebackground='white',cursor='hand2',variable=check)
terms.grid(row=9,column=0,padx=15,pady=10)


SignupButton=Button(frame,text='Sign Up',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activebackground='firebrick1',
                   activeforeground='White',cursor='hand2',bd=0,width=19,command=connect_database)
SignupButton.grid(row=10,column=0,pady=10)


Alreadyhaveacc=Button(frame,text='Already have an Account?',bd=0,bg='white',activebackground='white',cursor='hand2',
                    font=('Microsoft Yehei UI Light',9,'bold'),fg='firebrick1',activeforeground='firebrick1')
Alreadyhaveacc.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Login',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activebackground='white',activeforeground='blue',cursor='hand2',bd=0,command=login_page)
loginButton.place(x=177,y=383)



signup_window.mainloop()