from tkinter import *
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox
def main_page():
    validate_password() 
    login_window.destroy() 
    import mainpage


def signup_page():
    login_window.destroy()
    import signup
    
def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)
    
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

#Function to handle the login button click
def login_button_click():
    print("Username:", usernameEntry.get())
    print("Email:", emailEntry.get())
    print("Password:", passwordEntry.get())

#FUNCTIONALITY PART
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
def email_enter(event):
    if emailEntry.get()=='email':
        emailEntry.delete(0,END)              
def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
        
#Function to create the database table
conn = sqlite3.connect('signup.db')
cursor = conn.cursor()
table_create_query = ('''CREATE TABLE IF NOT EXISTS login_data
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Username TEXT NOT NULL,email TEXT NOT NULL,
                   Password TEXT UNIQUE NOT NULL
                )
            ''')
    
cursor.execute(table_create_query)


def login_user(Username,email,Password):
    conn = sqlite3.connect("signup.db")
    cursor = conn.cursor()
    data_insert_query = '''INSERT INTO login_data (Username,email,Password) VALUES(?, ?, ?)'''
    data_insert_tuple = (f"'{Username}','{email}','{Password}'")
    cursor.execute(data_insert_query,data_insert_tuple)
    messagebox.showinfo("Information","Login Succesfull")
    conn.commit()
    cursor.execute("SELECT email, Username, Password FROM login_data WHERE login_data.Username = Username and login_data.email = email and login_data.Password = Password")
    cursor.fetchall()
    
cursor.close()       
conn.close()
def validate_password():
    password = passwordEntry.get()
    has_capital_letter = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_symbol = any(char in '!@#$%^&*()_+{}[]:;<>,.?~\\-/' for char in password)
    is_valid_length = 8 <= len(password) <= 20

    if not (has_capital_letter and has_digit and has_special_symbol and is_valid_length):
        messagebox.showerror("Error", "Password should contain at least a capital letter, digits, and special symbols with a length between 8-20.")
    else:
        messagebox.showinfo("Success", "Password validated successfully.") 
        
    
#GUI PART
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('LOGIN')
bgImage=ImageTk.PhotoImage(file='bg.jpg')



bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1 = Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)

emailEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
emailEntry.place(x=580,y=260)
emailEntry.insert(0,'Email')
emailEntry.bind('<FocusIn>',email_enter)

frame3 = Frame(login_window,width=250,height=2,bg='firebrick1')
frame3.place(x=580,y=342)

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=320)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2 = Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=315)

forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1')
forgetButton.place(x=720,y=350)

loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=main_page)
loginButton.place(x=578,y=382)

# orLabel=Label(login_window,text='-------------OR-------------',font=('Open Sans',16),fg='firebrick1',bg='white')
# orLabel.place(x=583,y=425)

# google_logo=PhotoImage(file='google.png')
# googleLabel=Label(login_window,image=google_logo,bg='white')
# googleLabel.place(x=690,y=455)

# facebook_logo=PhotoImage(file='facebook.png')
# fbLabel=Label(login_window,image=facebook_logo,bg='white')
# fbLabel.place(x=640,y=455)

# twitter_logo=PhotoImage(file='twitter.png')
# twitterLabel=Label(login_window,image=twitter_logo,bg='white')
# twitterLabel.place(x=740,y=455)

signupLabel=Label(login_window,text="Dont have an account?",font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create new one',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)

    
login_window.mainloop()