import random
Newcard = True
score = 0
Totalnumberofquestion = 0
#List of words that could be in the game are listed here
SpanishWords = ["Spanish", "Espanol", "Red", "Rojo", "Hello", "Hola", "Good Morning", "Buenos Dias", "How are you", "Como Estas", "Good Afternoon", "Buenos Tardes", "Good Evening", "Buenos Noches", "Orange", "Naranja", "Green", "Verde", "Blue", "Azul", "Purple", "Morado", "Brown", "Cafe", "White", "Blanco", "Mexico", "Mexicano", "Spring", "Primavera", "Summer", "Verano", "Inverano", "Winter", "Lunes", "Monday", "Tuesday", "Martes", "Wednesday", "Miercoles", "See You Soon", "Hasta Pronto", "What's New", "Que Hay De Nuevo", "I'm sorry", "Lo Siento", "Thin", "Delgado", "Fat", "Gordo", "Young", "Joven", "Old", "Major", "Ugly", "Feo", "Handsome", "Guapo", "Beautiful", "Bonito", "How are you? I am Happy", "Como Eres Soy Contento", "Fall", "Otono", "Janurary", "Enero", "Feburary", "Febrero", "March", "Marzo", "April", "Abril", "May", "Mayo", "June", "Junio", "July", "Julio", "August", "Agosto", "September", "Septiembre", "October", "Octubre", "November", "Noviembre", "December", "Diciembre", "Thursday", "Jueves", "Friday", "Viernes", "Saturday", "Sabado", "Sunday", "Domingo", "What's The Weather Like", "Que Tiempo Hace", "Nice weather", "Hace Buen Tiempo", "It's very hot", "Hace Mucho Calor", "It's Sunny", "Hace Sol", "There is bad weather", "Hay Mal Tiempo", "It's cold", "Hace Frio", "It's Windy", "Hace Viento", "It's cool", "Esta Fresco", "It's Sunny", "Esta Soleado", "It's Cloudy", "Esta Nublado", "It's Rainy", "Esta Lloviendo", "It's Snowing", "Esta Nevando", "It's Windy", "Hay Viento", "There are clouds", "Hay Nubes", "Boy (12 or older)", "Chico", "Girl (12 or older)", "Chica", "Boy (Young)", "Nino", "Girl (Young)", "Nina", "See you Tommorow", "Hasta Manana", "Have a good weekend", "Pasa Buen Fin De Semana", "I present to you (Formal) with name Tyler", "Le presento A Tyler", "I present to you (Informal) with name Tyler", "Te presento A Tyler", "How are you(formal)", "Como Esta Usted", "Happy", "Contento", "Sad", "Triste", "Bored", "Aburrido", "Excited", "Emocionado", "Angry", "Enojado", "Sick", "Infermo", "Tired", "Cansado", "Nervous", "Nervioso", "I Am Scared", "Tengo Miedo", "I Am thristy", "Tengo Sed", "I Am hungry", "Tengo Hambre", "I Am Cold", "Tengo frio", "How Many Or How Much", "Cuanto", "When", "Cuando", "From Whom", "De Quien", "Who", "Quien", "There is/there are", "Hay", "Where", "Donde", "From Where", "De Donde", "How", "Como", "What/which", "Que", "Can I go to the Restroom Please", "Puedo Ir Al Bano Por Favor", "11", "Once", "12", "Doce", "13", "Trece", "14", "Catorce", "15", "Quince", "16", "Dieciseis", "17", "Diecisiete", "18", "Dieciocho", "19", "Diecinueve", "20", "Vente", "25", "Benticinco", "5", "Cinco", "2", "Dos", "1", "Uno", "Zero", "Cero", "3", "Tres", "4", "Cuatro", "6", "Seis", "7", "Siete", "8", "Ocho", "9", "Nueve"]
#Asks what game mode to play
Gamemode = input("Would you like to play English to Spanish or Spanish to English (Experimental). Type ES for English to Spanish SE for the oposite").lower()
if Gamemode == "es":
    while Newcard:
        #First Word Get Chosen
        numbertochosefrom = len(SpanishWords) - 2
        #Finding length of list to generate random number subtracting two for index starting at zero and not getting the last number in the list
        WordChosen = random.randrange(0, numbertochosefrom, 2)
        print(SpanishWords[WordChosen])
        Totalnumberofquestion += 1
        Guess = input("Enter what you think the translation of the word is.")
        if Guess.casefold() == SpanishWords[WordChosen + 1].casefold():
            print("You got the correct answer")
            score += 1
        else:
            print("You did not get the correct answer")
        print(f"The correct answer is {SpanishWords[WordChosen + 1]}")
        NextCard = input("Type Q is you would like to end and get your score. Type enter to continue playing").lower()
        if NextCard == "q":
            print(f"Okay Bye! You got {score}/{Totalnumberofquestion} questions right.")
            Newcard = False
            quit()

elif Gamemode == "se":
    while Newcard:
        # First Word Get Chosen
        numbertochosefrom = len(SpanishWords) - 2
        # Finding length of list to generate random number subtracting two for index starting at zero and not getting the last number in the list
        WordChosen = random.randrange(0, numbertochosefrom, 2)
        print(SpanishWords[WordChosen + 1])
        Totalnumberofquestion += 1
        Guess = input("Enter what you think the translation of the word is.")
        if Guess.casefold() == SpanishWords[WordChosen].casefold():
            print("You got the correct answer")
            score += 1
        else:
            print("You did not get the correct answer")
        print(f"The correct answer is {SpanishWords[WordChosen]}")
        NextCard = input("Type Q is you would like to end and get your score. Type enter to continue playing").lower()
        if NextCard == "q":
            print(f"Okay Bye! You got {score}/{Totalnumberofquestion} questions right.")
            Newcard = False
            quit()

