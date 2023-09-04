from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#Functionality Part

def forget_pass():
    def change_password():
        if user_entry.get()=='' or pass_entry.get()=='' or Cpass_entry.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=window)
        elif pass_entry.get()!=Cpass_entry.get():
            messagebox.showerror('Error','Password Mismatch',parent=window)
        else:
            con=pymysql.connect(host='localhost',user='root',password='admin',database='Registration_Data')
            mycursor=con.cursor()
            query='select*from data where Username=%s'
            mycursor.execute(query,(UserName.get()))

            row=mycursor.fetchone()

            if row==None:
                messagebox.showerror('Error','Invalid Username',parent=window)
            else:
                query='update data set User_Password=%s where Username=%s'
                mycursor.execute(query,(pass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Your Password Is Sucessfully Changed',parent=window)
                window.destroy()




    window=Toplevel()
    window.title('Change Password')

    bgpic=ImageTk.PhotoImage(file='venv/background.jpg')
    bgLabel= Label(window,image=bgpic)
    bgLabel.grid()

    heading_label= Label(window,text='RESET PASSWORD',font=('arial','18','bold'),bg='white',fg='magenta2')
    heading_label.place(x=480,y=60)

    userlabel=Label(window,text='Username',font=('arial','12','bold'),bg='white',fg='orchid1')
    userlabel.place(x=470,y=130)

    user_entry=Entry(window,width=25,fg='magenta2',font=('arial','11','bold'),bd=0)
    user_entry.place(x=473,y=160)
   

    Frame(window,width=250,height=2,bg='orchid1').place(x=473,y=180)


    passlabel=Label(window,text='Password',font=('arial','12','bold'),bg='white',fg='orchid1')
    passlabel.place(x=470,y=210)

    pass_entry=Entry(window,width=25,fg='magenta2',font=('arial','11','bold'),bd=0)
    pass_entry.place(x=473,y=240)
   

    Frame(window,width=250,height=2,bg='orchid1').place(x=473,y=260)


    Cpasslabel=Label(window,text='Confirm Password',font=('arial','12','bold'),bg='white',fg='orchid1')
    Cpasslabel.place(x=470,y=290)

    Cpass_entry=Entry(window,width=25,fg='magenta2',font=('arial','11','bold'),bd=0)
    Cpass_entry.place(x=473,y=320)
   

    Frame(window,width=250,height=2,bg='orchid1').place(x=473,y=340)


    SubmitButton=Button(window,text='Submit',font=('Open Sans',16,'bold'),fg='white',bg='magenta2',activebackground='magenta2',
                   activeforeground='White',cursor='hand2',bd=0,width=19,command=change_password)
    SubmitButton.place(x=470,y=390)

    window.mainloop()



def login_user():
    if UserName.get()=='' or Password.get()=='':
        messagebox.showerror('Error','All Fields Are Required')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='admin')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection Is Not Established Try Again')
            return
        query='use Registration_Data'
        mycursor.execute(query)
        query='select*from data where Username=%s and User_Password=%s'
        mycursor.execute(query,(UserName.get(),Password.get()))
        row=mycursor.fetchone()

        if row==None:
            messagebox.showerror('Error','Invalid Username or Password')
        else:
            messagebox.showinfo('Wellcome','Login is Sucessful')
            



def user_enter(event):
    if UserName.get()=='Username':
        UserName.delete(0,END)
    


def password_enter(event):
    if Password.get()=='Password':
        Password.delete(0,END)



def hide():
    openeye.config(file='venv/openeye.png')
    Password.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='venv/closeye.png')
    Password.config(show='')
    eyeButton.config(command=hide)


def Signup_page():
    login_window.destroy()
    import signup


#GUI Part
login_window=Tk()
login_window.geometry('960x660+50+50')
login_window.resizable(0,0)
login_window.title('LOGIN PAGE')

bgImage=ImageTk.PhotoImage(file='venv/bg.jpg')

bgLabel=Label(login_window,image=bgImage)
bgLabel.grid(row=0,column=0)
#bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yehei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)

UserName=Entry(login_window,width=25,font=('Microsoft Yehei UI Light',11,'bold'),bd=0,fg='firebrick1')
UserName.place(x=588,y=200)
UserName.insert(0,'Username')

UserName.bind('<FocusIn>',user_enter)

#for Underline under Username
Frame(login_window,width=250,height=2,bg='firebrick1').place(x=588,y=220)


Password=Entry(login_window,width=25,font=('Microsoft Yehei UI Light',11,'bold'),bd=0,fg='firebrick1')
Password.place(x=588,y=260)
Password.insert(0,'Password')

Password.bind('<FocusIn>',password_enter)

#for Underline under Password
Frame(login_window,width=250,height=2,bg='firebrick1').place(x=588,y=280)

openeye=PhotoImage(file='venv/openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=815,y=252)

forgetButton=Button(login_window,text='Forget Password?',bd=0,bg='white',activebackground='white',cursor='hand2',
                    font=('Microsoft Yehei UI Light',11,'bold'),fg='firebrick1',activeforeground='firebrick1',command=forget_pass)
forgetButton.place(x=700,y=290)


loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activebackground='firebrick1',
                   activeforeground='White',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=578,y=350)


orLabel=Label(login_window,text='----------------OR----------------',font=('Open Sans',12),fg='firebrick1',bg='White')
orLabel.place(x=610,y=400)


fblogo=PhotoImage(file='venv/facebook.png')
fblabel=Label(login_window,image=fblogo,bg='White')
fblabel.place(x=640,y=440)

glogo=PhotoImage(file='venv/google.png')
glabel=Label(login_window,image=glogo,bg='White')
glabel.place(x=690,y=440)

twlogo=PhotoImage(file='venv/twitter.png')
twlabel=Label(login_window,image=twlogo,bg='White')
twlabel.place(x=740,y=440)


SignupButton=Button(login_window,text='Don\'t Have Account',bd=0,bg='white',activebackground='white',cursor='hand2',
                    font=('Microsoft Yehei UI Light',9,'bold'),fg='firebrick1',activeforeground='firebrick1')
SignupButton.place(x=590,y=500)


NewAccButton=Button(login_window,text='Create New Account',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activebackground='white',activeforeground='blue',cursor='hand2',bd=0,command=Signup_page)
NewAccButton.place(x=710,y=500)





login_window.mainloop()