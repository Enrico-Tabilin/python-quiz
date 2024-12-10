# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
questionstxt = open("questions.txt", 'w')

def exitcheck(txt):
    if txt == "EXIT":
        questionstxt.close()
        exit()

user = input('Hello! Welcome to the quiz maker.\nTo start, type "RANDOM" if you want the questions to be randomized, or type "NORMAL" for the questions to be in order.\nEnter "EXIT" to quit and save.\n')
exitcheck(user)
questionstxt.write(str.capitalize(user)+'\n')

q=1
while True:
    print("Typing Question",q)
    user = input('Enter your question, enter "EXIT" to quit and save.\n')
    exitcheck(user)
    question = str(q)+". "+user+"\n"
    print('Enter 4 answers, and choose the correct answer (1,2,3 or 4), or enter "EXIT" to quit and save. (5 = Correct Answer Number)')
    i=1
    while True:
        exitcheck(user)
        if i>4:
            user = input("5: ")
            try:
                if int(user)>0 and int(user)<5:
                    question = question+"5: "+user+"\n"
                break
            except:
                print('Please enter 1,2,3 or 4.')
        else:
            user = input(str(i)+": ")
            question = question+str(i)+": "+user+"\n"
            i+=1
    questionstxt.write(question)
    q+=1