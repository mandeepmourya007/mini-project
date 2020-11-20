from tkinter import *

screen = Tk()
screen.title("Attendace")
subject = StringVar(screen)
roll = StringVar(screen)
TOTAL_STUDENT=15
ADA = [0] * TOTAL_STUDENT
MATHS = [0] * TOTAL_STUDENT
PPR = [0] * TOTAL_STUDENT
RM = [0] * TOTAL_STUDENT


def save():
    s = subject.get()
    studts = roll.get("1.0", "end")
    print(s, studts)


def onClick(i):
    print("present: MIT" + str(i))
    return


def start():
    for i in range(TOTAL_STUDENT):
        t = Checkbutton(
            screen,
            text="MIT"+str(2020000+i),
            variable=i,
            onvalue=1,
            offvalue=0,
            command=lambda i=i: onClick(2020001+i),
        )
        t.grid(row=10 + i, column=1, ipadx=10)

        

if __name__ == "__main__":

    # Set the background colour of GUI window
    screen.configure(background="light green")

    # Set the configuration of GUI window (WidthxHeight)
    screen.geometry("550x550")

    # Create welcome to Real Time Currency Convertor label
    headlabel = Label(
        screen, text="welcome to Real Attendace visualizer", fg="black", bg="red"
    )

    label2 = Label(screen, text="Select subject", fg="black", bg="dark green")

    headlabel.grid(row=0, column=1)
    # label1.grid(row = 1, column = 0)
    label2.grid(row=2, column=0)
    start()
    # Create a text entry boxconfigure
    # for filling or typing the information.
    # roll = Text(screen, height=20, width=25, font="lucida 13")

    # roll.grid(row=5, column=1, ipadx="25")
    var1 = IntVar()
    var2 = IntVar()

    
    # list of  subjects
    subjects = ["RM", "ADA", "PPR", "MATHS"]

    # create a drop down menu using OptionMenu function
    options = OptionMenu(screen, subject, *subjects)

    options.grid(row=2, column=1, ipadx=10)

    submit = Button(screen, text="Submit", bg="red", fg="black", command=save)
    submit.grid(row=6, column=1)

    # Start the GUI
    screen.mainloop()
