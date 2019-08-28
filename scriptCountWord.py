# Universidad Distrital
# Maestria en Ciencias de la Informacion y las Telecomunicaciones
# Informatica
# Willian Pachon


msgIntro = "Programa para contar caracteres en una palabra"
msgInvalidUserPassword = "Usuario o clave invalido"
msgUnauthorized = "Has consumidos todos tus intentos. NO estas autorizado para utilizar este programa" 
msgWellcome = "Bienvenido "
msgIntroduceWord = "Introduce la palabra de interes: "
msgResultLenWord = "La palabra '%s' tiene: %s caracteres"
msgThankForParticipation = "Gracias por participar"

print(msgIntro)

user = "admin"
password = "Qwerty123"

usrInput = raw_input("Usuario: ")
pwdInput = raw_input("Clave: ")

maxNumTries = 2

numTry=0
while pwdInput != password:
	print(msgInvalidUserPassword)
	if numTry==2:
		print(msgUnauthorized)
		break;
	pwdInput=str(input("Clave: "))
	if pwdInput != password:
		numTry+=1
		
if numTry < maxNumTries:
	print(msgWellcome + usrInput)
	
word = raw_input(msgIntroduceWord)

lenWord = len(word)

print(msgResultLenWord % (word, lenWord))
print(msgThankForParticipation)