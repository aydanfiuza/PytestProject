def askPassword():
    password = input("Informe sua senha: ")
    return password

def checkLenghtPsw(password):
    if len(password) < 10:
        return False
    else:
        return True

def checkSpecialPsw(password):
    if not any(not c.isalnum() for c in password):
        return False
    else: 
        return True
    
def checkNumberPsw(password):
    if any(i.isdigit() for i in password):
        return True
    else:
        return False

def checkUpperPsw(password):
    if any(char.isupper() for char in password):
        return True
    else:
        return False

def checkLowerPsw(password):
    if any(char.islower() for char in password):
        return True
    else:
        return False