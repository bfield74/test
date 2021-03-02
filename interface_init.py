from tkinter import *
from PIL import ImageTk, Image
from question_bank import questions, files, description, ask_question
from teacher_comments import comments
from random import randint
from tkinter import scrolledtext

interface = Tk()
interface.title("Welcome to Physics")

#reset question counters
reset = True
ask_question(0,0,0,reset)
reset = False

#interface.geometry("900x900")
# make some frames
visual_frame = LabelFrame(interface, text="Visual")#, padx=100, pady=100)
visual_frame.grid(row=0, column=0) #pack(side = TOP) #grid(row=0, column = 0)

question_frame = LabelFrame(interface, text="Here is the question")#, padx=100, pady=50)
question_frame.grid(row=0,column=1)#pack(side = TOP) #grid(row=0, column=1)

teacher_frame = LabelFrame(interface, text="Teacher comments") #, padx=100, pady=100)
teacher_frame.grid(row=1, column=1)#pack(side = BOTTOM) #grid(row=1, column=1)

userinput_frame = LabelFrame(interface, text="Input your answers here")#, padx=100, pady=100)
userinput_frame.grid(row=2, column=1)#pack(side = BOTTOM) #grid(row=2, column=0)

button_frame = LabelFrame(interface, text="Buttons to click")
button_frame.grid(row=1, column=0)#pack(side = RIGHT) #grid(row=2, column=1)



# click commands - put these somewhere else later
def clickrandom():
    rand1 = randint(0,2)
    rand2 = randint(0, len(questions[0][image_number]) - 1)
    Label(question_frame, text=ask_question(rand1,image_number,rand2, reset)).grid(row=1, column=0)


def clickvisualize(init):
    rand = randint(0,len(questions[0][image_number])-1)
    if init == False:
        question.destroy()
    question = Label(question_frame, text=ask_question(0,image_number,rand,reset))
#    text.destroy()
    question.grid(row=1, column=0)


def clickgraphs():
    rand = randint(0,len(questions[2][image_number])-1)
    Label(question_frame, text=ask_question(2,image_number,rand,reset)).grid(row=1, column=0)

def clickcalculation():
    rand = randint(0,len(questions[1][image_number])-1)
    Label(question_frame, text=ask_question(1,image_number,rand,reset)).grid(row=1, column=0)


def clickmotivation():
    Label(button_frame, text="got to motivation").grid(row=1, column=1)


# put in the main problem
image_number = 0
img = ImageTk.PhotoImage(Image.open(files[image_number]))
place_image = Label(visual_frame, image=img).grid(row=0, column=0)
Label(visual_frame, text=description[image_number], wraplength=350).grid(row=1, column=0)
# put in the current question
suggestion=0
question_number=0
question = Label(question_frame, text=questions[image_number][suggestion][question_number], wraplength=300)
question.grid(row=1, column=0)
#Label.pack
Label(teacher_frame, text=comments[1], wraplength=300).grid(row=0, column=0)

# enter a dialoge box
scr = scrolledtext.ScrolledText(userinput_frame, width=30, height=5).grid(row=0, column=0)
#box = Entry(userinput_frame).grid(row=0, column=0)

# add buttons for quick links to different exercises
b_random = Button(button_frame, text="random Q", command=clickrandom).grid(row=0, column=0)
b_visualize = Button(button_frame, text="visualize", command=clickvisualize).grid(row=0, column=1)
b_graphs = Button(button_frame, text=" graphs  ", command=clickgraphs).grid(row=0, column=2)
b_calculation = Button(button_frame, text="calculation", command=clickcalculation).grid(row=0, column=3)
b_motivation = Button(button_frame, text="motivation", command=clickmotivation).grid(row=0, column=4)
# exit button
b_exit = Button(button_frame, text="exit program", command=interface.quit).grid(row=0, column=5)


interface.mainloop()

