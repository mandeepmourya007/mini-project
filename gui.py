import pandas as pd
import numpy as np
from tkinter import *
import csv
import matplotlib.pyplot as plt
import csv
import time
import datetime
import os.path
from os import path

START_ROW = 25
TOTAL_STUDENT = 15
# list of  subjects
SUBJECTS = ["ADA", "PPR", "MATHS", "RM"]
SCREEN_SIZE = "710x600"
screen = Tk()
screen.title("Attendace")
subject = StringVar(screen)
# roll = StringVar(screen)
roll = [0] * len(SUBJECTS)

rows = [0] * TOTAL_STUDENT


def get_file_name():
    x = datetime.datetime.now()
    day = str(x.strftime("%x"))

    day = day.split("/")
    day = "A" + day[1] + "_" + day[0] + "_" + day[2] + ".csv"
    return day


def create_file():

    fields = SUBJECTS

    # data rows of csv file
    rows = [roll] * TOTAL_STUDENT

    # name of csv file
    filename = get_file_name()
    if path.exists(filename):
        return

    # writing to csv file
    with open(filename, "w") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        #  csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)


create_file()


# print(get_file_name())


def get_subject():
    return subject.get()


filename = PhotoImage(file="i.png")
background_label = Label(screen, image=filename)
background_label.place(x=50, y=450)


def save():
    s = get_subject()
    r = csv.reader(open(get_file_name()))  # Here your csv file

    lines = list(r)
    # lines[] = roll
    for i in range(TOTAL_STUDENT):
        print(rows[i])
        lines[i][SUBJECTS.index(s)] = rows[i]
    # print(lines, SUBJECTS.index(s))
    print(lines)
    writer = csv.writer(open("testing.csv", "w"))
    writer.writerows(lines)


def onClick(i):
    # print("present: MIT" + str(2020000 + i))
    rows[i] = 1 if rows[i] == 0 else 1

    # print((roll))
    return


def show():
    s = get_subject()
    print("call funtion to show graph of " + s)


def today_graph_show():
    print("call funtion to show graph of today ")

def get_roll():
    roll = txt_roll.get()[-3:]
    return roll
def student_graph():
    s=get_roll()
    print("graph of studnet" +s)

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
        # hegiht =
        t.grid(row=25 + i, column=1, ipadx=10)


if __name__ == "__main__":

    # Set the background colour of GUI window
    screen.configure(background="light green")

    # Set the configuration of GUI window (WidthxHeight)
    screen.geometry(SCREEN_SIZE)

    # Create welcome to Real Time Currency Convertor label
    headlabel = Label(
        screen, text="welcome to Real Attendace visualizer", fg="black", bg="red"
    )

    label2 = Label(screen, text="Select subject", fg="black", bg="dark green")

    headlabel.grid(row=1, column=1)
    label2.grid(row=2, column=0)
    start()

    # create a drop down menu using OptionMenu function
    options = OptionMenu(screen, subject, *SUBJECTS)

    options.grid(row=2, column=1, ipadx=10)
    graph = Button(screen, text="show graph", bg="red", fg="black", command=show)
    graph.grid(row=2, column=2)
    today_graph = Button(
        screen, text="show today_graph", bg="red", fg="black", command=today_graph_show
    )
    today_graph.grid(row=2, column=3)

    i = 0
    y = []
    # x=['MIT2020101','MIT2020102','MIT2020103','MIT2020104','MIT2020105','MIT2020106','MIT2020107','MIT2020108','MIT2020109','MIT2020101','MIT2020111','MIT2020112','MIT202013']

    x_pos = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def graph():
        file = open("testing.csv")
        lt = np.loadtxt(file, delimiter=",")

        # lt = [np.round(x) for x in lt]
        # print(lt)

        a = lt[:, 0]
        b = lt[:, 1]

        fig = plt.figure(figsize=(15, 2))
        plt.xticks(x_pos)
        plt.yticks([])

        plt.bar(x_pos, a, width=0.5, label="Ada")
        plt.bar(x_pos + 0.2, b, width=0.5, label="Math")
        # plt.tight_layout()
        plt.xlabel("RollNo")
        plt.ylabel("Absent-0,Present-1")
        plt.show()

    submit = Button(screen, text="Submit", bg="red", fg="black", command=save)
    submit.grid(row=3, column=1)
    l1 = Label(screen, text="Enter roll")
    l1.grid(row=3, column=2, sticky=W, pady=2)
    txt_roll = Entry(screen)

    # this will arrange entry widgets
    txt_roll.grid(row=3, column=3, pady=2)
    submit = Button(screen, text="student", bg="red", fg="black", command=student_graph)
    submit.grid(row=3, column=4)

    # mybutton = Button(text="Graph", command=graph)
    # mybutton.grid(row=530, column=320)
    screen.mainloop()
    # root.mainloop()
