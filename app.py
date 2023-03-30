def askUser():
    login = input("Informe seu usuário: ")
    return login

def checkUpper(login):
    if not login[0].isupper():
        return False
    else:
        return True
    
def checkSpace(login):
    if " " in login:
        return False
    else:
        return True

def checkSpecial(login):
    if any(not c.isalnum() for c in login):
        return False
    else:
        return True

def checkLenght(login):
    if len(login) > 30:
        return False
    else:
        return True
    
def checkUser():
    while True:
        login = askUser()
        if checkUpper(login) and checkSpace and checkSpecial(login) and checkLenght(login):
            return login
        else:
            print("O usuário não satisfaz as requisições de login.\nVocê deve conter a primeira letra maiúscula, nenhum caracter especial e menos de 30 caracteres ao todo.")
    
def askPassword():
    psw = input("Informe sua senha: ")
    return psw

def checkLenghtPsw(psw):
    if len(psw) < 10:
        return False
    else:
        return True

def checkSpecialPsw(psw):
    if not any(not c.isalnum() for c in psw):
        return False
    else: 
        return True
    
def checkNumberPsw(psw):
    if not any(i.isdigit() for i in psw):
        return False
    else:
        return True

def checkUpperPsw(psw):
    if not any(char.isupper() for char in psw):
        return False
    else:
        return True

def checkLowerPsw(psw):
    if not any(char.islower() for char in psw):
        return False
    else:
        return True
    
def checkPassword():
    while True:
        psw = askPassword()
        if checkLenghtPsw(psw) and checkSpecialPsw(psw) and checkNumberPsw(psw) and checkUpperPsw(psw) and checkLowerPsw(psw):
            return psw
        else:
            print("As requisições de senha não foram satisfeitas.\nVocê deve conter ao menos uma letra maiúscula, uma minúscula, um caracter especial, um número e mais de 10 caracteres.")    
    
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

login = checkUser()
print("Usuário válido.")
psw = checkPassword()
print("Senha válida.")