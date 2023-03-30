from cryptographyFramework import *

def askUser():
    login = input("Informe seu usuário: ")
    loginOkay = checkUser(login)
    if loginOkay != "...":
        print("Usuário válido.")

def checkUser(login):
    if not login[0].isupper():
        print("O usuário deve conter a primeira letra maiúscula.")
        return "..."
    elif any(not c.isalnum() for c in login):
        print("O usuário não pode conter caracteres especiais.")
        return "..."
    elif len(login) > 30:
        print("O usuário deve conter menos de 30 caracteres.")
        return "..."
    else:
        return login
    
def askPassword():
    psw = input("Informe sua senha: ")
    pswOkay = checkPassword(psw)
    if pswOkay != "..":
        print("Senha válida.")

def checkPassword(psw):
    if len(psw) < 10:
        print("A senha deve ter no mínimo 10 caracteres.")
        return ".."
    elif not any(not c.isalnum() for c in psw):
        print("A senha deve conter ao menos um caracter especial.")
        return ".."
    elif not any(i.isdigit() for i in psw):
        print("A senha deve conter ao menos um número.")
        return ".."
    elif not any(char.isupper() for char in psw):
        print("A senha deve conter ao menos uma letra maiúscula.")
        return ".."
    elif not any(char.islower() for char in psw):
        print("A senha deve conter ao menos uma letra minúscula.")
        return ".."
    else:
        return psw
    
def askMessage():
    message = input("Informe a mensagem a ser criptografada: ")
    messageOkay = checkMessage(message)
    if messageOkay != ".":
        print("Mensagem criptografada válida.")

def checkMessage(message):
    if len(message) > 70:
        print("A mensagem criptografada deve ter no máximo 70 caracteres.")
        return "."
    else:
        return message

askUser()
askPassword()
askMessage()

