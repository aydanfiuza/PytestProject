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