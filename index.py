import email
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser
from attr import attributes


#Window
jWindow = Tk()
jWindow.title("DP systems - Aces Panel")
jWindow.geometry("700x300")
jWindow.configure(background="white")
jWindow.resizable(width=False ,height=False)
jWindow.attributes("-alpha",0.9)
jWindow.iconbitmap(default = "icons/LogoIcon.ico")

#image
logo = PhotoImage(file="icons/logo.png")

#widgets
LeftFrame = Frame(jWindow, width=250, height=450, bg="MIDNIGHTBLUE",relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jWindow, width=445, height=450, bg="MIDNIGHTBLUE",relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame,text="Username:", font=("century Gothic",20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=50,y=100)

UserEntry = ttk.Entry(RightFrame, width=35)
UserEntry.place(x=205, y=110)

PassLabel = Label(RightFrame,text="Password:", font=("century Gothic",20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=50,y=135)

PassEntry = ttk.Entry(RightFrame, width=35, show="*")
PassEntry.place(x=205, y=145)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()
    
    DataBaser.cursor.execute("""
    SELECT * FROM USERS 
    WHERE (User = ? AND Password = ?)
    """, (User,Pass))
    print("Selecionou")
    VeryfyLogin = DataBaser.cursor.fetchone()

    try:
        if(User in VeryfyLogin and Pass in VeryfyLogin):
            messagebox.showinfo(title="Login Info",  message="Acesso confirmado. Bem vindo(a)!")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso Negado. Verificar se astá cadastrado no sistma!")
            
#buttons
LoginButton = ttk.Button(RightFrame, text="Login", width=40, command=Login)
LoginButton.place(x=100,y=215)

def Register(): 
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    
    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=49,y=15)
    
    NomeEntry = ttk.Entry(RightFrame,width=44)
    NomeEntry.place(x=151, y=30)
    
    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=50, y=50)
    
    EmailEntry = ttk.Entry(RightFrame,width=44)
    EmailEntry.place(x=151, y=63)
    
    def RegisterToDataBase():
        
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        
        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Ainda há campos vazios. Preencha todos os campos")
        else:
            
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?,?,?,?)
            """, (Name,Email,User,Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register info" , message="Conta criada com sucesso!")
        
    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    Register.place(x=135,y=230)
    
    def BackToLogin():
        #remove 
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #add
        LoginButton.place(x=100)
        RegisterButton.place(x=125)
        
    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=170, y=262)
        
    
    
RegisterButton = ttk.Button(RightFrame, text="Register", width=30, command=Register)
RegisterButton.place(x=135,y=250)


jWindow.mainloop()