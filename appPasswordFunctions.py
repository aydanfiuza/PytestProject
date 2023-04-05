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
    if any(i.isdigit() for i in psw):
        return True
    else:
        return False

def checkUpperPsw(psw):
    if any(char.isupper() for char in psw):
        return True
    else:
        return False

def checkLowerPsw(psw):
    if any(char.islower() for char in psw):
        return True
    else:
        return False