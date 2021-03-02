
files = ["drop_pull_basic.png", "drop_pull_velocity_left.png", "drop_pull_velocity_right.png"]

description = ["Two masses, each of mass M are connected by a very light string."
                "a frictionless and very light pully is used to hang on mass over the "
                "edge of the table. Two masses, each of mass M are connected by a very light string."
                "a frictionless and very light pully is used to hang on mass over the "
                "edge of the table, at this instant M1 is moving to the left and M2 is moving upward",
                "Two masses, each of mass M are connected by a very light string."
                "a frictionless and very light pully is used to hang on mass over the "
                "edge of the table, at this instant M1 is moving to the right and M2 is moving downward"]

# 3-D array:  0: visualize  2: calculation 3: graphs
questions = [[["Describe all object that move together with the same "
               "velocity and acceleration.", "question1_vis2", "question1_vis3"],
             ["question2_vis1", "question2_vis2", "question2_vis3"],
            ["question3_vis1", "question3_vis2", "question3_vis3"]],
             [["question1_calc1", "question1_calc2", "question1_calc3"],
             ["question2_calc1", "question2_calc2", "question2_calc3"],
            ["question3_calc1", "question3_calc2", "question3_calc3"]],
            [["question1_graph1", "question1_graph2", "question1_graph3"],
             ["question2_graph1", "question2_graph2", "question2_graph3"],
            ["question3_graph1", "question3_graph2", "question3_graph3"]]]

# find a question to ask
def ask_question(type, visual, question, reset):

    if reset == True:
        print("in reset")
        w=3
        h=3
        global question_tracker
        question_tracker = {}
        for i in range(0, len(questions[:][0][0])):
           for j in range(0, len(questions[0][:][0])):
                for k in range(0, len(questions[0][0][:])):
                    question_tracker[i,j,k] = 0
    if question_tracker[type,visual,question] == 1:
        print("going to next question")
        i = 0
        while i < len(questions[type][visual][:]):
            print("in while",i)
            if question_tracker[type,visual,i] == 0:
                question = i
                print("renaming question")
                break
            i = i + 1
            if i == len(questions[type][visual][:]):
                return "no more questions of this type"



    print(type,visual,question)
    print(question_tracker[type,visual,question])
    print(questions[type][visual][question])
    question_tracker[type, visual, question] = 1

    return questions[type][visual][question]



