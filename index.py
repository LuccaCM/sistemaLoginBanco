# Importando as bibliotecas:
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import baseDados

# Criando a janela:
jan = Tk()
jan.title("DP Systems - Painel de Acesso")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/banco.ico")

# ========= Carregando imagens ====
logo = PhotoImage(file="icons/banc.png")

# ========= Widgets ===============
LeftFrame = Frame(jan, width=200, height=300, bg="red", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="red", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="red")
LogoLabel.place(x=17, y=70)

# Usuário:
UserLabel = Label(RightFrame, text="Usuário:", font=("Century Gothic", 20), bg="red", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=110, y=110)

# Senha:
PassLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="red", fg="white")
PassLabel.place(x=5, y=140)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=110, y=150)


# Botões:
# Login
def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    baseDados.cursor.execute("""
    SELECT * FROM Users
    WHERE (Usuário = ? and Senha = ?)
    """, (User, Pass))
    print("Selecionou")
    verificaLogin = baseDados.cursor.fetchone()
    try:
        if User in verificaLogin and Pass in verificaLogin:
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado. Bem Vindo!")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique se esta cadastrado no Sistema!")


LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=210)


# Registrar
def Register():
    # Removendo os widgets de login:
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    # Inserindo os widgets de cadastro:
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="red", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=110, y=15)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="red", fg="white")
    EmailLabel.place(x=5, y=45)

    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=110, y=55)

    def RegistrarBanco():
        Nome = NomeEntry.get()
        Email = EmailEntry.get()
        Usuario = UserEntry.get()
        Senha = PassEntry.get()

        if Nome == "" and Email == "" and Usuario == "" and Senha == "":
            messagebox.showerror(title="Register Error", message="Não deixe Nenhum Campo Vazio. Preecha Todos os "
                                                                 "Campos!")
        else:
            baseDados.cursor.execute("""
            INSERT INTO USers(Nome, Email, Usuário, Senha) VALUES(?, ?, ?, ?)
            """, (Nome, Email, Usuario, Senha))
            baseDados.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta Criada Com Sucesso!")

    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegistrarBanco)
    Register.place(x=100, y=225)

    def BackToLogin():
        # Removendo widgets de Cadastro:
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        # Trazendo de volta os widgets de Login:
        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Voltar", width=20, command=BackToLogin)
    Back.place(x=125, y=260)


RegisterButton = ttk.Button(RightFrame, text="Registrar", width=20, command=Register)
RegisterButton.place(x=125, y=250)

jan.mainloop()
