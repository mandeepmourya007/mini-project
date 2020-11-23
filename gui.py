import numpy as np
from tkinter import *
import csv
import matplotlib.pyplot as plt
import time
import datetime
# import tkinter
# from tkinter import messagebox
# import os.path
from os import path
import glob


TOTAL_STUDENT = 120
# list of  subjects
SUBJECTS = ["PPR", "ADA", "MATHS", "RM"]
SCREEN_SIZE = "710x600"
roll = [0] * len(SUBJECTS)
# [0,0,0,0]
rows = [0] * TOTAL_STUDENT


def get_file_name():
    x = datetime.datetime.now()
    print(x)
    day = str(x.strftime("%x"))
    print(day)
    day = day.split("/")
    day = "A" + day[1] + "_" + day[0] + "_" + day[2] + ".csv"
    return day
# get_file_name()

def create_file():
    # fields = SUBJECTS
    # data rows of csv file
    rows = [roll] * TOTAL_STUDENT
    # name of csv file
    filename = get_file_name()
    if path.exists(filename):
        return
    # writing to csv file
    with open(filename, "w") as csvfile:
        # creating a csv writer
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(rows)


def get_subject():
    return subject.get()


def mark_attendance():
    create_file()
    s = get_subject()
    r = csv.reader(open(get_file_name()))
    lines = list(r)
    for i in range(15):
        lines[i][SUBJECTS.index(s)] = rows[i]
    writer = csv.writer(open(get_file_name(), "w"))
    writer.writerows(lines)


def get_csv():
    all_csv = glob.glob1(".", "*.csv")
    return all_csv


def onClick(i):
    
    rows[i] = 1 if rows[i] == 0 else 0
    return


def show():

    s = get_subject()

    def column(matrix, i):
        return [row[i] for row in matrix]

    sum_of_day = []
    sub = s  # str(input())
    print("showing graph of " + sub)
    csvs = get_csv()
    for j in range(len(csvs)):
        s = csvs[j]
        # txt to 2d array
        r = np.genfromtxt(s, delimiter=",", names=True)
        Attendence = [0 for i in range(4)] # [0,0,0,0]
        for i in range(119):
            Attendence[0] += r[i][0]
            Attendence[1] += r[i][1]
            Attendence[2] += r[i][2]
            Attendence[3] += r[i][3]
        
        sum_of_day.append(Attendence)
    # s of d  [ [15,85,96,65],[555],[]]
    t = np.arange(0, len(get_csv()), 1)
    if sub == "ADA":
        plt.plot(t, column(sum_of_day, 0), "ro-", label="ADA")
    if sub == "RM":
        plt.plot(t, column(sum_of_day, 1), "ro-", label="RM")
    if sub == "MATHS":
        plt.plot(t, column(sum_of_day, 2), "ro-", label="MATH")
    if sub == "PPR":
        plt.plot(t, column(sum_of_day, 3), "ro-", label="PPR")
    print(column(sum_of_day, 2))
    plt.xticks(t)
    plt.xlabel("Perticular Day")
    plt.ylabel("Attendence on that day for perticular subject")
    plt.legend()
    plt.show()


def today_graph_show():
    print("call funtion to show graph of today ")
    file = open(get_file_name())
    lt = np.loadtxt(file, delimiter=",")
    count1 = 0
    # global A
    a = lt[:15, 0]
    # print(a)
    b = lt[:15, 1]
    c = lt[:15, 2]
    d = lt[:15, 3]
    # for i in range(15):
    #     if a[i] == 1 or b[i] == 1 or c[i] == 1 or d[i] == 1:
    #         count1 += 1

    fig = plt.figure(figsize=(15, 4))
    plt.xticks(x_pos, x, rotation="270")
    plt.yticks([])
    bar_plot = plt.bar(x_pos, a , width=0.5, label="PPR")
    bar_plot = plt.bar(x_pos, b,bottom=a, width=0.5, label="ADA")
    c_graph=list(np.add(a,b))
    bar_plot = plt.bar(x_pos, c,bottom=c_graph, width=0.5, label="MATHS")
    d_graph=list(np.add(c_graph,c))
    bar_plot = plt.bar(x_pos, d,bottom=d_graph, width=0.5, label="PM")
    print("Attendence Recorded Successfully")
    # print("No of Students Attended the class:", count1)
    plt.xlabel("RollNo")
    plt.ylabel("Absent-0   Present-1")
    plt.legend()

    plt.show()



def get_roll():
    roll = txt_roll.get()[-3:]
    return roll


def student_graph():
    s = get_roll()
    student = int(s)
    presence = [0, 0, 0, 0]
    # print(student)
    csvs = get_csv()
    days = len(csvs)
    print(days)
    for j in range(days):
        s = csvs[j]
        r = np.genfromtxt(s, delimiter=",", names=True)
        presence[0] += r[student][0]
        # print(r[student][0])
        presence[1] += r[student][1]
        presence[2] += r[student][2]
        presence[3] += r[student][3]
    # print(presence[0])
    absence = [days - presence[0], days - presence[1], days - presence[2], days - presence[3]]
    labels = (
        "ADA-presence",
        "ADA-absence",
        "RM-presence",
        "RM-absence",
        "PPR-presence",
        "PPR-absence",
        "MATH-presence",
        "MATH-absence",
    )
    sizes = [
        100 * (presence[0] / days),
        100 * (absence[0] / days),
        100 * (presence[1] / days),
        100 * (absence[1] / days),
        100 * (presence[2] / days),
        100 * (absence[2] / days),
        100 * (presence[3] / days),
        100 * (absence[3] / days),
    ]
    explode = (
        0,
        0.1,
        0,
        0.1,
        0,
        0.1,
        0,
        0.1,
    )  # only "explode" the 2nd slice (i.e. 'Hogs')

    i = 0
    colors = ["red","grey", "green","grey", "yellow","grey", "blue","grey"][::-1]

    def absolute_value(val):
        print(val)
        a  = np.round(val/100.*sum(sizes), 0)
        return a
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct=absolute_value,colors=colors, startangle=180)
    ax1.axis("equal")

    plt.show()


def Attendace_button():
    for i in range(15):
        check_box = Checkbutton(
            screen,
            text="MIT" + str(2020000 + i),
            variable=lambda i=i: ADA[i],
            onvalue=1,
            offvalue=0,
            command=lambda i=i: onClick(i),
        )
        check_box.grid(row=25 + i, column=1, ipadx=10)


if __name__ == "__main__":

    screen = Tk()
    screen.title("Attendace")
    subject = StringVar(screen)

    # Set the background colour of GUI window
    screen.configure(background="#9ad3bc")
    # Set the configuration of GUI window (WidthxHeight)
    screen.geometry(SCREEN_SIZE)
    # Create welcome to Real Time Currency Convertor label
    headlabel = Label(
        screen, text="welcome to Real Attendace visualizer", fg="black", bg="#cad315"
    )
    image = PhotoImage(file="i.png")
    background_label = Label(screen, image=image)
    background_label.place(x=50, y=450)

    # setting location  for headline
    headlabel.grid(row=1, column=1)
    # lable for subject
    lbl_subject = Label(screen, text="Select subject", fg="black", bg="grey")
    # setting location  for subject
    lbl_subject.grid(row=2, column=0)
    # create a drop down menu using OptionMenu function
    options = OptionMenu(screen, subject, *SUBJECTS)
    # setting location  for dropdown
    options.grid(row=2, column=1, ipadx=10)
    graph = Button(screen, text="show graph", bg="#9ad3bc", fg="black", command=show)
    graph.grid(row=2, column=2)
    today_graph = Button(
        screen,
        text="show today_graph",
        bg="#9ad3bc",
        fg="black",
        command=today_graph_show,
    )
    today_graph.grid(row=2, column=3)

    i = 0
    y = []
    x = [
        "MIT2020101",
        "MIT2020102",
        "MIT2020103",
        "MIT2020104",
        "MIT2020105",
        "MIT2020106",
        "MIT2020107",
        "MIT2020108",
        "MIT2020109",
        "MIT2020101",
        "MIT2020111",
        "MIT2020112",
        "MIT202013",
        "MIT2020114",
        "MIT2020115",
    ]

    x_pos = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    A = 1
    submit = Button(
        screen, text="Submit", bg="#9ad3bc", fg="black", command=mark_attendance
    )
    # generating checkbox for marks attendance
    Attendace_button()
    submit.grid(row=3, column=1)
    lbl_roll = Label(screen, text="Enter roll")
    lbl_roll.grid(row=3, column=2, sticky=W, pady=2)
    txt_roll = Entry(screen)
    # this will arrange entry widgets
    txt_roll.grid(row=3, column=3, pady=2)
    submit = Button(
        screen, text="student", bg="#9ad3bc", fg="black", command=student_graph
    )
    submit.grid(row=3, column=4)
    screen.mainloop()
