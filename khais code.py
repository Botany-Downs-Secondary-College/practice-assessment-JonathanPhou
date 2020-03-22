from tkinter import*
from random import*

root= Tk()
quiz_difficulty = StringVar()
quiz_difficulty.set(1)
frame1 = Frame(root)
frame2 = Frame(root)
root.title("Screen1")
root.geometry("450x300+500+200")

#Answer Check
Easy = True
Medium = True
Hard = True

#Question Creator
x = randrange(10)
y = randrange(10)
w = randrange(10)
a = randrange(8)
z = randrange(10)

#Answer Amount
Correct_Answer = int(0)

def Move():
    global QuestionLabel, Easy, Medium, Hard, answer
    print("Easy is", Easy)
    print("Medium is", Medium)
    print("Hard is", Hard)
    if Easy == True:
        ChangeAnswers()
        problem_text = str(x) + " + " + str(y) + " = "
        QuestionLabel.configure(text = problem_text)
        Easy = False
    elif Medium == True:
        ChangeAnswers()
        n = randrange(4)
        if n == 0:
            answer = 1.5 * x + 1.5 * y
            problem_text = str(1.5 * x)  + " + " + str( 1.5 * y)  + "  = "
            QuestionLabel.configure(text = problem_text)
        if n == 1:
            answer = 1.5 * x * 1.5 * y
            problem_text = str(1.5 * x)  + " * " + str( 1.5 * y)  + "  = "
            QuestionLabel.configure(text = problem_text)
        if n == 2:
            answer = 2 * x / 2 * y
            problem_text = str(2 * x)  + " / " + str(2 * y)  + "  = "
            QuestionLabel.configure(text = problem_text)
        if n == 3:
            answer = 1.5 * x - 1.5 * y
            problem_text = str(1.5 * x)  + " - " + str( 1.5 * y)  + "  = "
            QuestionLabel.configure(text = problem_text)
        Medium = False
    elif Hard == True:
        ChangeAnswers()
        problem_text = str(x) + "x^3" + " + " + str(y) + "x^2" + " - " + str(z) + "x" + " + " + str(w) + " " + "Is divided by" + " " + "x - " + str(a)
        QuestionLabel.configure(text = problem_text)
    else:
        print("Finish the question")    

def Screen1 ():
    global main_frame

    main_frame = Frame(root)
    main_frame.pack()
    label1 = Label(main_frame, bg = "black", fg = "white", width = 20, padx = 30, pady = 10, text = "Welcome to the Maths Quiz", font = ("TImes", "24", "bold italic"))
    label1.pack()
    label2 = Label(main_frame, text = "Name", width = 20, font = ("Times", "14", "bold italic"))
    label2.pack()
    textboxl = Entry(main_frame, width = 20)
    textboxl.pack()
    textbox2 = Entry(main_frame, width = 20)
    textbox2.pack(padx = 2, pady = 10)
    rb1 = Radiobutton (main_frame, width = 20, value = 1, text = "Easy", anchor = W, variable = quiz_difficulty)
    rb1.pack()
    rb2 = Radiobutton (main_frame, width = 20, value = 2, text = "Medium", anchor = W, variable = quiz_difficulty)
    rb2.pack()
    rb3 = Radiobutton (main_frame, width = 20, value = 3, text = "Hard", anchor = W, variable = quiz_difficulty)
    rb3.pack()
    button1 = Button(main_frame, text = "Next", command = Difficulty)
    button1.pack()

def Difficulty():
    global main_frame
    main_frame.pack_forget()
    diff = quiz_difficulty.get()
    diff = int(diff)
    if diff == 1:
        easy_question()
    elif diff == 2:
        Medium_Question()
    elif diff ==3:
        Hard_question()

def delscreen1():
    global frame2, Easy, Medium, Hard
    Easy = True
    Medium = True
    Hard = True
    frame2.forget()
    Screen1()


def easy_question():
    global frame1
    global frame2
    global QuestionLabel, AnswerEntry, Easy

    frame2 = LabelFrame(root, bg= "black", fg = "white", width = 20,
                        text = "Answer Quiz Questions", font=("Times", "14", "bold italic"))
    frame2.pack()

    QuestionLabel = Label(frame2, text = "", width=15, height = 2)
    problem_text = str(x) + " + " + str(y) + "  = "
    QuestionLabel.configure(text = problem_text)
    QuestionLabel.pack()

    AnswerEntry = Entry(frame2, width = 20)
    AnswerEntry.pack()

    buttonFrame = (frame2)
    buttonFrame.pack()
    home = Button(buttonFrame, text = "Home" , anchor = W, command = delscreen1)
    home.pack(side=LEFT)

    home = Button(buttonFrame, text = "Check Answer" , anchor = W, command = lambda: print(CheckAnswers()))
    home.pack(side=LEFT)

    home = Button(buttonFrame, text = "Next Question", anchor = W, command = Move)
    home.pack(side=LEFT)
    Easy = False
    
def Medium_Question():
    global frame1
    global frame2
    global QuestionLabel, AnswerEntry, Medium

    frame2 = LabelFrame(root, bg= "black", fg = "white", width = 60,
                        text = "Answer Quiz Questions", font=("Times", "14", "bold italic"))
    frame2.pack()

    QuestionLabel = Label(frame2, text = "", width=30, height = 2)
    problem_text = str(1.5 * x)  + " - " + str( 1.5 * y)  + "  = "
    QuestionLabel.configure(text = problem_text)
    QuestionLabel.pack()

    AnswerEntry = Entry(frame2, width = 30)
    AnswerEntry.pack()

    buttonFrame = (frame2)
    buttonFrame.pack()
    home = Button(buttonFrame, text = "Home" , anchor = W, command = delscreen1)
    home.pack(side=LEFT)

    Check_Button = Button(buttonFrame, text = "Check Answer" , anchor = W, command = lambda: print(CheckAnswers()))
    Check_Button.pack(side=LEFT)

    Next_Button = Button(buttonFrame, text = "Next Question", anchor = W, command = Move)
    Next_Button.pack(side=LEFT)
    Medium = False

def Hard_question():
    global frame1
    global frame2
    global QuestionLabel, AnswerEntry, Hard

    frame2 = LabelFrame(root, bg= "black", fg = "white", width = 60,
                        text = "Answer Quiz Questions", font=("Times", "14", "bold italic"))
    frame2.pack()

    QuestionLabel = Label(frame2, text = "", width=30, height = 2)
    problem_text = str(x) + "x^3" + " + " + str(y) + "x^2" + " - " + str(z) + "x" + " + " + str(w) + "  " + "Is divided by" + "  " + "x - " + str(a)
    QuestionLabel.configure(text = problem_text)
    QuestionLabel.pack()

    AnswerEntry = Entry(frame2, width = 30)
    AnswerEntry.pack()

    buttonFrame = (frame2)
    buttonFrame.pack()
    home = Button(buttonFrame, text = "Home" , anchor = W, command = delscreen1)
    home.pack(side=LEFT)

    Check_Button = Button(buttonFrame, text = "Check Answer" , anchor = W, command = lambda: print(CheckAnswers()))
    Check_Button.pack(side=LEFT)

    Next_Button = Button(buttonFrame, text = "Next Question", anchor = W, command = Move)
    Next_Button.pack(side=LEFT)
    Hard = False
 
def ChangeAnswers():
    global x
    global y
    global w
    global a
    global z

    x = randrange(10)
    y = randrange(10)
    w = randrange(10)
    a = randrange(8)
    z = randrange(10)
    
def CheckAnswers():
    global AnswerEntry, Easy, Medium, Hard, answer
    if Easy == False:
        answer = x + y
        ans = AnswerEntry.get()
        try:
            ans = int(ans)
        except:
            return "DAS NOT NUMBER U DUM GRUAYYY"
        if ans == answer:
            Easy = True
        else:
            return False
    elif Medium == False:
        ans = AnswerEntry.get()
        try:
            ans = float(ans)
        except:
            return "DAS NOT NUMBER U DUM GRUAYYY"
        if ans == answer:
            Medium = True
        else:
            return False
    elif Hard == False:
        answer = x(aaa) + y(aa) - z(a) + w
        ans = AnswerEntry.get()
        try:
            ans = int(ans)
        except:
            return "DAS NOT NUMBER U DUM GRUAYYY"
        if ans == answer:
            Hard = True
        else:
            return False

Screen1()
