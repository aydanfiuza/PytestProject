from appUserFunctions import *
from appPasswordFunctions import *
from appMessageFunctions import *
from cryptographyFramework import *    
   
def checkUser():
    while True:
        login = askUser()
        if checkUpper(login) and checkSpace and checkSpecial(login) and checkLenght(login):
            return login
        else:
            print("O usuário não satisfaz as requisições de login.\nVocê deve conter a primeira letra maiúscula, nenhum caracter especial e menos de 30 caracteres ao todo.")
    
def checkPassword():
    while True:
        password = askPassword()
        if checkLenghtPsw(password) and checkSpecialPsw(password) and checkNumberPsw(password) and checkUpperPsw(password) and checkLowerPsw(password):
            return password
        else:
            print("As requisições de senha não foram satisfeitas.\nVocê deve conter ao menos uma letra maiúscula, uma minúscula, um caracter especial, um número e mais de 10 caracteres.")

def checkMessage():
    while True:
        message = askMessage()
        if checkLenghtMsg(message):
            return message
        else:
            print("A requisição de mensagem não foi satisfeita.\nVocê precisa escreve-la com menos de 70 caracteres.")


login = checkUser()
print("Usuário válido.")
password = checkPassword()
print("Senha válida.")
message = checkMessage()
print("Sua mensagem foi armazenada e criptografada com sucesso.")

initializeWrite()
encryptedText = encryptMessage(login, password, message)
saveNewLine(encryptedText)

initializeRead()
line1 = readNextLine()
print('--------------------------')
print(f'Mensagem criptografada:\n{line1}')
print('--------------------------')