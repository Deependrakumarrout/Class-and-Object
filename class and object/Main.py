
                                    #Reading to files
                                    #hello.txt files in folder class and object

#Here r is to read the file only. w is to write the file or change the file by writing new information.
# a stand for append we can modifily information at the end of the file.And we can add new information.
# r+ we can read and write both of a file and change the file too.

#This is showing the only a boolen value which can be readable.

'''Empty_file=open("hello.txt","r")
print(Empty_file.readable())
Empty_file.close()

#This is reading the whole file so i have implement the read()
Empty_file=open("hello.txt","r")
print(Empty_file.read())
Empty_file.close()'''


#Implementing the (.readlines()) This will take all of our line and put inside of a list.
'''Empty_file=open("hello.txt","r")
#print(Empty_file.readlines())
#To excess the specific line we can refer to it by index in the array
#print(Empty_file.readlines()[0])
#We can also use this readlines function with a for loop
for Empty in Empty_file.readlines():
    print(Empty)
Empty_file.close()'''



                                           #Writing to files
                                           #Same file (hello.txt)
#Using the hello.txt file
#It will print all the code that we have written the text file.

#hello_ar=open("hello.txt","r")
#Here we can append and can add any extra information the our code
'''hello_ar=open("hello.txt","a")
#hello_ar.write("\nVivo-Known as smartphone")
#hello_ar.close()
#Adding another data in text file
hello_ar.write("\nOne plus 8 as super")
hello_ar.close()'''

#if we get a w which is write function
#This will only gona show a new line in the text file
'''hello_ar=open("hello.txt","w")
hello_ar.write("pixcel-sony")
hello_ar.close()'''


#We can also use w to create new file
'''hello_ar=open("hello1.txt","w")
hello_ar.write("Gone-london")
hello_ar.close()'''

#Ceated a python file
'''hello_ar=open("modules.py","w")
hello_ar.close()'''


                                            # Modules and pip
                                            #Another file importing file


#Modules are the huge part of a python you defenely gona indlude them in the python stack
#importing is the file name and importing it so one more thing is that roll_dice is the function which is define in importing file.
#This is importing funcanility from external python file.
#And also search about (list of python modules) in Google

'''import importing
print(importing.roll_dice(10))'''


                                            #Class and objects
                                            #Creating a new file Sumit.py

#So here from the file we are importing the people class
'''from Sumit import People
people1=People("Ragav",44,"Rg road mumbai",893453566)
people2=People("Ravi",53,"Ai colony Bhawanipatna",463990903)
print(people1.phone_num)
print(people2.address)'''


                                                #Making a Quiz game
                                                #These all are in Question.py file

'''How we can write a quize in python explain'''
# Array with question seperted by comma
#open in anohter file and make a class def __init__(self,prompt,anser):
#Then the name of the class and the name of the array which will be mension there Question(updat[0],"a"),
#make a function and give a parameter
#then create a variable to store when it get the correct answer
#create a for loop to get the question continue step by step like for que in the function parameter
#a variable to input the value which will be look like answer is a variable answer=input(que.prompt) que is in the for loop
#a variable which help it to get repet
#if variable - answer==i.answer (here i is in for loop and the answer is in new python file)
#then the score +=1 it will get increment
#Then print the value first str(len(which will be the parameter)+"correct"
#call the function as well


#def restat():
    from Question import Question
    question_prompts=[
        "what is your hobbies?\n (a)Playing games\n (b)Reading\n (c)Coding\n\n",
        "What is your moto?\n (a)To make something\n (b)To give this world a better thing\n (c)Nothing\n\n",
        "what you want in your life?\n (a)To get poor and stay happy\n (b)To get rich and sad\n (c)To get rich and happy\n\n",
        "How many spoke in our national flag's wheel?\n (a)33\n (b)24\n (c)26\n\n",
        "What is the colour of water?\n (a)blue\n (b)white\n (c)No colour\n\n"
    ]
    '''
    questions =  [
        Question(question_prompts[0], "c"),
        Question(question_prompts[1], "b"),
        Question(question_prompts[2], "a"),
        Question(question_prompts[3], "b"),
        Question(question_prompts[4], "c"),
    ]

    def run_test(questions):
        score=0
        for Que in questions:
            answer=input(Que.prompt)
            if answer == Que.answer:
                score+=1
        print("You have score"+str(score)+"/"+str(len(questions))+"correct")
    run_test(questions)



    var= str(input("Do you want to practice again[TYPE - Yes/NO]:"))
    if var=='yes'.lower():
        print("restating")

        restat()
    elif var=='no'.lower():
        print('User want to stop..')

    else:
        print("invalid input")


restat()


'''



from Question import Subject

Define=[
    "what is your name?\n (a)john\n (b)Rony\n (c)Sony\n (d)Tony\n\n",
    "What you do?\n (a)Riding bike\n (b)Travelling\n (c)Gaming\n (d)Conding\n\n",
    "Why you want to go with programming?\n (a)Its supprot me\n (b)I love to do it\n (c)Because i don't know\n (d)It have something\n\n",
    "What is your goal? (a)To be a doctor\n (b)To be a programmer\n (c)Driver\n (d)Sunmicro\n\n"
]

question=[
    Subject(Define[0],"b"),
    Subject(Define[1],"d"),
    Subject(Define[2],"b"),
    Subject(Define[3],"b"),
]

def run_ques(question):
    score = 0
    for questions in question:
        answer=input(questions.que)
        if answer==questions.ans:
            score+=1
    print("You have scored "+str(score)+"/"+str(len(question))+" correct...")
run_ques(question)





                                                #Object Function
                                                #This is in Student.py file

'''from Student import Deepak
result=Deepak(79,12)
result1=Deepak(14,12)
print(result.roll_on())
print(result1.roll_on())'''


                                                #Inheritance
                                                #Same file (student)
                                                #And working with another file which is inheritance

'''
from Inheritance import android
from Student import Ios


sam=Ios()
sam.camara()
sam.chat_box()



var1=android()
var1.camara()
var1.chat_box()


'''
