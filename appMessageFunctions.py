def askMessage():
    message = input("Informe a mensagem a ser criptografada: ")
    return message    
    
def checkLenghtMsg(message):
    if len(message) > 70:
        return False
    else:
        return True