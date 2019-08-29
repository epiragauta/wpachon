# Universidad Distrital
# Maestria en Ciencias de la Informacion y las Telecomunicaciones
# Informatica
# Willian Pachon

def count_word_app():

	msgIntro = "Programa para contar caracteres en una palabra"
	msgInvalidUserPassword = "Usuario o clave invalido, intento No. %s"
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
	
	while (pwdInput != password) or (usrInput != user):
		print(msgInvalidUserPassword % (numTry+1))
		if numTry==2:
			print(msgUnauthorized)
			return;
		
		numTry+=1
		pwdInput = raw_input("Clave: ")
			
	if numTry < maxNumTries:
		print(msgWellcome + usrInput)
	
				
	word = raw_input(msgIntroduceWord)

	lenWord = count_letters(word)

	print(msgResultLenWord % (word, lenWord))
	print(msgThankForParticipation)

def count_letters(word):

	lenWord = len(word)
	return lenWord
	
def count_letters_test():
	print "count_letters_test"
	assert count_letters("test") == 4, "Debe ser 4"
	
	
if __name__ == '__main__':
    
	count_letters_test()
	count_word_app()

