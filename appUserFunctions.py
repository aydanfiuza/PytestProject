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