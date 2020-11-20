from tkinter import *
import csv
import time
import datetime
import os.path
from os import path

TOTAL_STUDENT = 15
# list of  subjects
SUBJECTS = ["ADA", "PPR", "MATHS", "RM"]
# ADA = [0] * TOTAL_STUDENT
# MATHS = [0] * TOTAL_STUDENT
# PPR = [0] * TOTAL_STUDENT
# RM = [0] * TOTAL_STUDENT

screen = Tk()
screen.title("Attendace")
subject = StringVar(screen)
# roll = StringVar(screen)
roll = [0] * TOTAL_STUDENT


def create_file():

    fields = SUBJECTS

    # data rows of csv file
    rows = [roll] * len(SUBJECTS)

    # name of csv file
    filename = "testing.csv"
    if path.exists(filename):
        return

    # writing to csv file
    with open(filename, "w") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)


create_file()


def get_file_name():
    x = datetime.datetime.now()
    day = str(x.strftime("%x"))

    day = day.split("/")
    day = "A" + day[1] + "_" + day[0] + "_" + day[2]
    return day


# print(get_file_name())


def get_subject():
    return subject.get()


def save():
    s = get_subject()
    r = csv.reader(open("testing.csv"))  # Here your csv file
    lines = list(r)
    lines[SUBJECTS.index(s)] = roll
    # print(lines, SUBJECTS.index(s))
    writer = csv.writer(open("testing.csv", "w"))
    writer.writerows(lines)


def onClick(i):
    # print("present: MIT" + str(2020000 + i))
    roll[i] = 1 if roll[i] == 0 else 1

    # print((roll))
    return


def start():
    for i in range(TOTAL_STUDENT):
        t = Checkbutton(
            screen,
            text="MIT" + str(2020000 + i),
            variable=lambda i=i: ADA[i],
            onvalue=1,
            offvalue=0,
            command=lambda i=i: onClick(i),
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

    # create a drop down menu using OptionMenu function
    options = OptionMenu(screen, subject, *SUBJECTS)

    options.grid(row=2, column=1, ipadx=10)

    submit = Button(screen, text="Submit", bg="red", fg="black", command=save)
    submit.grid(row=6, column=1)

    # Start the GUI
    screen.mainloop()
