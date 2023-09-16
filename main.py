import random
Newcard = True
score = 0
Totalnumberofquestion = 0
#List of words that could be in the game are listed here
SpanishWords = ["Spanish", "Espanol", "Red", "Rojo", "Hello", "Hola", "Good Morning", "Buenos Dias", "How are you", "Como Estas", "Good Afternoon", "Buenos Tardes", "Good Evening", "Buenos Noches", "Orange", "Naranja", "Green", "Verde", "Blue", "Azul", "Purple", "Morado", "Brown", "Cafe", "White", "Blanco", "Mexico", "Mexicano", "Spring", "Primavera", "Summer", "Verano", "Inverano", "Winter", "Lunes", "Monday", "Tuesday", "Martes", "Wednesday", "Miercoles"]
while Newcard:
    #First Word Get Chosen
    numbertochosefrom = len(SpanishWords) - 2
    #Finding length of list to generate random number subtracting two for index starting at zero and not getting the last number in the list
    WordChosen = random.randint(0, numbertochosefrom)
    if WordChosen % 2 != 0:
        while True:
            numbertochosefrom = len(SpanishWords) - 2
            WordChosen = random.randint(0, numbertochosefrom)
            if WordChosen % 2 == 0:
                continue
    print(SpanishWords[WordChosen])
    Totalnumberofquestion += 1
    Guess = input("Enter what you think the translation of the word is.")
    if Guess == SpanishWords[WordChosen + 1]:
        print("You got the correct answer")
        score += 1
    else:
        print("You did not get the correct answer")
    print(f"The correct answer is {SpanishWords[WordChosen + 1]}")
    NextCard = input("Type Q is you would like to end and get your score. Type enter to continue playing").lower()
    if NextCard == "q":
        print(f"Okay Bye! You got {score}/{Totalnumberofquestion}s right.")
        Newcard = False
        quit()

