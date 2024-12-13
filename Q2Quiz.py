# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
import random;from datetime import datetime
questionstxt = open("questions.txt", 'r')
q=[];a=[]
txt=questionstxt.readline()
qtype=txt.strip('\n')
txt=questionstxt.readline()
while txt !='':
    q+=[txt.strip('\n')]
    txt=questionstxt.readline()
    for _ in range(5):
        a+=[txt.strip('\n')]
        txt=questionstxt.readline()
print('Welcome to the quiz!\nYou can exit the quiz by entering "EXIT"\n')
streak=0;correct=0

def exitcheck(txt):
    if txt == "EXIT":
        questionstxt.close()
        exit()
question=1
while len(q)>0:
    if qtype=='RANDOM':
        timelol=datetime.now().year*(10**17)+datetime.now().month*(10**15)+datetime.now().day*(10**13)+datetime.now().hour*(10**11)+datetime.now().minute*(10**9)+datetime.now().second*(10**7)+datetime.now().microsecond
        random.seed = timelol;rand=random.randint(0,len(q)-1)
        print('Question',str(question)+q[0+rand][1:len(q[0+rand])])
        q.pop(0+rand)
        ans = a[4+rand*5][3]
        for i in range(4):
            timelol=datetime.now().year*(10**17)+datetime.now().month*(10**15)+datetime.now().day*(10**13)+datetime.now().hour*(10**11)+datetime.now().minute*(10**9)+datetime.now().second*(10**7)+datetime.now().microsecond
            random.seed = timelol
            randans = random.randint(0,(3-i))
            if a[randans+rand*5][0] == ans:
                ans = i+1
            print(chr(65+i)+a[randans+rand*5][1:len(a[randans+rand*5])])
            a.pop(randans+rand*5)
        user=input('Your answer (letter): ')
        exitcheck(user)
        if str.upper(user) == chr(64+ans):
            streak+=1;correct+=1
            print('\nCongratulations! You got it right. Your answer streak is now',str(streak)+'!\nYour total amount of correct answers is '+str(correct)+'.\n')
        else:
            streak=0
            print("\nSorry! That's wrong. Your answer streak is back to 0!\nThe correct answer was",chr(64+ans)+'!\nYour total amount of correct answers is '+str(correct)+'.\n')
        question+=1
        a.pop(0+rand*4)
    else:
        print('Question',q[0])
        for i in range(4):
            print(chr(65+i)+a[i][1:len(a[i])])
        user=input('Your answer (letter): ')
        exitcheck(user)
        if str.upper(user) == chr(64+int(a[4][3])):
            streak+=1;correct+=1
            print('\nCongratulations! You got it right. Your answer streak is now',str(streak)+'!\nYour total amount of correct answers is '+str(correct)+'.\n')
        else:
            streak=0
            print("\nSorry! That's wrong. Your answer streak is back to 0!\nThe correct answer was",chr(64+int(a[4][3]))+'!\nYour total amount of correct answers is '+str(correct)+'.\n')
        q.pop(0)
        for _ in range(5):
            a.pop(0)
print("That's the end of the quiz! Your final answer streak is",str(streak)+'.\nYour final total amount of correct answers is '+str(correct)+'.\n')
questionstxt.close()