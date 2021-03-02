from tkinter import *
from PIL import ImageTk, Image

main_window = Tk()


my_img = ImageTk.PhotoImage(Image.open("drop_pull.png"))
my_label = Label(image=my_img).grid(row=1, column=3)

# creating label widget
main_label = Label(main_window, text="Main problem")
choice_label = Label(main_window, text="choice 1")


def myclick():
    test_label = Label(main_window, text="clicked button").grid(row=1, column=4)
    user_input = input_box.get()
    print(user_input)

# data entry
input_box = Entry(main_window, width=50, borderwidth=2)
input_box.grid(row=1, column=1)
input_box.insert(0, ">>>> ")
user_text = input_box.get()
print(user_text)

# making a button
button_1 = Button(main_window, text="button1", command=myclick).grid(row=0, column=4)

# put it on the screen
main_label.grid(row=0, column=0)
choice_label.grid(row=2, column=0)

main_window.mainloop()
