# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
questionstxt = open("questions.txt", 'w')
q=1
while True:
    print("Typing Question",q)
    user = input('Enter your question, enter "EXIT" to quit and save.\n')
    if user == "EXIT":
        questionstxt.close()
        break
    question = str(q)+". "+user+"\n"
    print('Enter 4 answers, and choose the correct answer (A,B,C or D), or enter "EXIT" to quit and save. (E = Correct Answer Letter)')
    for i in range(5):
        user = input(str(i+1)+": ")
        if user == "EXIT":
            questionstxt.close()
            exit()
        if i==4:
            try:
                if int(user)>0 and int(user)<5:
                    question = question+chr(65+i)+": "+user+"\n"
                
        #if i==4:
        #    if str.capitalize(user)!="A" and str.capitalize(user)!="B" and str.capitalize(user)!="C" and str.capitalize(user)!="D":
        #        while True:
        #            print('Please type A,B,C or D.')
        #            user = input('E: ')
        #            if user == "EXIT":
        #                questionstxt.close()
        #                exit()
        #            print(user)
        #            if str.capitalize(user)=="A" or str.capitalize(user)=="B" or str.capitalize(user)=="C" or str.capitalize(user)=="D":
        #                question = question+chr(65+i)+": "+str.capitalize(user)+"\n"
        #                break
        #    else:
        #        question = question+chr(65+i)+": "+str.capitalize(user)+"\n"
        else:
            question = question+chr(65+i)+": "+user+"\n"
        breakpoint
    questionstxt.write(question)
    q+=1