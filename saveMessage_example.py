from cryptographyFramework import *

initializeWrite()
user = "Aydan"
password = "aydan2009"
encryptedText = encryptMessage(user, password, "Eu gosto de açaí")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Eu gosto de pizza")
saveNewLine(encryptedText)

