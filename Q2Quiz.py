# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
questionstxt = open("questions.txt", 'r')
print('Welcome to the quiz!\nYou can exit the quiz by entering "EXIT"\n')
streak=0
while True:
    txt=questionstxt.readline()
    if txt != '':
        print('Question',txt.strip('\n'))
        txt=questionstxt.readline()
        for i in range(4):
            print(txt.strip('\n'))
            txt=questionstxt.readline()
        user=input('Your answer (letter): ')
        if user == "EXIT":
            questionstxt.close()
            exit()
        elif str.capitalize(user) == txt[3:4]:
            streak+=1
            print('\nCongratulations! You got it right. Your answer streak is now',str(streak)+'!\n')
        else:
            streak=0
            print("\nSorry! That's wrong. Your answer streak is back to 0!\nThe correct answer was",txt[3:4]+'!\n')
    else:
        print("That's the end of the quiz! Your final answer streak is",str(streak)+'.')
        questionstxt.close()
        break