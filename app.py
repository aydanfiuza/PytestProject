from appUserFunctions import *
from appPasswordFunctions import *
from appMessageFunctions import *
    
def checkUser():
    while True:
        login = askUser()
        if checkUpper(login) and checkSpace and checkSpecial(login) and checkLenght(login):
            break
        else:
            print("O usuário não satisfaz as requisições de login.\nVocê deve conter a primeira letra maiúscula, nenhum caracter especial e menos de 30 caracteres ao todo.")
    
def checkPassword():
    while True:
        psw = askPassword()
        if checkLenghtPsw(psw) and checkSpecialPsw(psw) and not checkNumberPsw(psw) and not checkUpperPsw(psw) and not checkLowerPsw(psw):
            break
        else:
            print("As requisições de senha não foram satisfeitas.\nVocê deve conter ao menos uma letra maiúscula, uma minúscula, um caracter especial, um número e mais de 10 caracteres.")

def checkMessage():
    while True:
        message = askMessage()
        if checkLenghtMsg(message):
            break
        else:
            print("A requisição de mensagem não foi satisfeita.\nVocê precisa escreve-la com menos de 70 caracteres.")


login = checkUser()
print("Usuário válido.")
psw = checkPassword()
print("Senha válida.")
message = checkMessage()
print("Sua mensagem foi armazenada e criptografada com sucesso.")