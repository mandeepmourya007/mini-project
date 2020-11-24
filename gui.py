import numpy as np
from tkinter import *
import csv
import matplotlib.pyplot as plt
import datetime
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
    """
    TO get filename of current day
    """
    x = datetime.datetime.now()
    day = str(x.strftime("%x"))
    day = day.split("/")
    day = "A" + day[1] + "_" + day[0] + "_" + day[2] + ".csv"
    return day


def create_file():
    """
    To Create a csv file for today attendance
    """
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
    """
    To get subject from GUI
    """

    return subject.get()


def mark_attendance():
    """
    Mark the attendance of selected subject
    """

    create_file()
    s = get_subject()
    r = csv.reader(open(get_file_name()))
    lines = list(r)
    for i in range(15):
        lines[i][SUBJECTS.index(s)] = rows[i]
    writer = csv.writer(open(get_file_name(), "w"))
    writer.writerows(lines)


def get_csv():

    """
    To get all CSV files
    """
    allCsv = glob.glob1(".", "*.csv")
    return allCsv


def onClick(i):
    """
    On click mark attendance after collecting data from GUI to a list names row
    """
    rows[i] = 1 if rows[i] == 0 else 0
    return


def show():
    """
    To show graph of selected subjects
    """
    s = get_subject()

    def column(matrix, i):
        return [row[i] for row in matrix]

    sumOfDay = []
    sub = s  # str(input())
    print("showing graph of " + sub)
    csvs = get_csv()
    for j in range(len(csvs)):
        s = csvs[j]
        # txt to 2d array
        r = np.genfromtxt(s, delimiter=",", names=True)
        Attendence = [0 for i in range(4)]  # [0,0,0,0]
        for i in range(119):
            Attendence[0] += r[i][0]
            Attendence[1] += r[i][1]
            Attendence[2] += r[i][2]
            Attendence[3] += r[i][3]

        sumOfDay.append(Attendence)  # s of d  [ [15,85,96,65],[555],[]]

    t = np.arange(1, len(get_csv()) + 1, 1)
    if sub == "ADA":
        plt.plot(t, column(sumOfDay, 0), "ro-", label="ADA")
    if sub == "RM":
        plt.plot(t, column(sumOfDay, 1), "ro-", label="RM")
    if sub == "MATHS":
        plt.plot(t, column(sumOfDay, 2), "ro-", label="MATH")
    if sub == "PPR":
        plt.plot(t, column(sumOfDay, 3), "ro-", label="PPR")
    plt.xticks(t)
    plt.xlabel("Day")
    plt.ylabel("Attendence of " + sub)
    plt.legend()
    plt.show()


def today_graph_show():
    """
    to show graph of today attendance
    """
    print("show graph of today ")
    file = open(get_file_name())
    lt = np.loadtxt(file, delimiter=",")
    a = lt[:15, 0]
    b = lt[:15, 1]
    c = lt[:15, 2]
    d = lt[:15, 3]
    fig = plt.figure(figsize=(15, 4))
    plt.xticks(xPos, x, rotation="270")
    plt.yticks([])
    barPlot = plt.bar(xPos, a, width=0.5, label="PPR")
    barPlot = plt.bar(xPos, b, bottom=a, width=0.5, label="ADA")
    c_graph = list(np.add(a, b))
    barPlot = plt.bar(xPos, c, bottom=c_graph, width=0.5, label="MATHS")
    d_graph = list(np.add(c_graph, c))
    barPlot = plt.bar(xPos, d, bottom=d_graph, width=0.5, label="PM")
    print("Attendence Recorded Successfully")
    plt.xlabel("RollNo")
    plt.ylabel("Present")
    plt.legend()

    plt.show()


def get_roll():
    """
    To get roll number of student from GUI
    """
    roll = txtRoll.get()[-3:]
    return roll


def student_graph():
    """
    To show data of the student
    """
    s = get_roll()
    student = int(s)
    presence = [0, 0, 0, 0]
    csvs = get_csv()
    days = len(csvs)
    for j in range(days):
        s = csvs[j]
        r = np.genfromtxt(s, delimiter=",", names=True)
        presence[0] += r[student][0]
        # print(r[student][0])
        presence[1] += r[student][1]
        presence[2] += r[student][2]
        presence[3] += r[student][3]
    # print(presence[0])
    absence = [
        days - presence[0],
        days - presence[1],
        days - presence[2],
        days - presence[3],
    ]
    labels = (
        "ADA-absence",
        "ADA-presence",
        "RM-absence",
        "RM-presence",
        "PPR-absence",
        "PPR-presence",
        "MATH-absence",
        "MATH-presence",
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
    colors = ["red", "grey", "green", "grey", "yellow", "grey", "blue", "grey"][::-1]

    def absolute_value(val):
        print(val)
        a = np.round(val / 100.0 * sum(sizes), 0)
        return a

    fig1, ax1 = plt.subplots()
    ax1.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct=absolute_value,
        colors=colors,
        startangle=180,
    )
    ax1.axis("equal")

    plt.show()


def Attendace_button():
    """
    Buttons to marks attendance
    """
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
    headLabel = Label(
        screen, text="welcome to Real Attendace visualizer", fg="black", bg="#cad315"
    )
    image = PhotoImage(file="i.png")
    backgroundLabel = Label(screen, image=image)
    backgroundLabel.place(x=50, y=450)
    # setting location  for headline
    headLabel.grid(row=1, column=1)
    # lable for subject
    lblSubject = Label(screen, text="Select subject", fg="black", bg="grey")
    # setting location  for subject
    lblSubject.grid(row=2, column=0)
    # create a drop down menu using OptionMenu function
    options = OptionMenu(screen, subject, *SUBJECTS)
    # setting location  for dropdown
    options.grid(row=2, column=1, ipadx=10)
    graph = Button(screen, text="show graph", bg="#9ad3bc", fg="black", command=show)
    graph.grid(row=2, column=2)
    todayGraph = Button(
        screen,
        text="show today_graph",
        bg="#9ad3bc",
        fg="black",
        command=today_graph_show,
    )
    todayGraph.grid(row=2, column=3)

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

    xPos = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    A = 1
    submit = Button(
        screen, text="Submit", bg="#9ad3bc", fg="black", command=mark_attendance
    )
    # generating checkbox for marks attendance
    Attendace_button()
    submit.grid(row=3, column=1)
    lblRoll = Label(screen, text="Enter roll")
    lblRoll.grid(row=3, column=2, sticky=W, pady=2)
    txtRoll = Entry(screen)
    # this will arrange entry widgets
    txtRoll.grid(row=3, column=3, pady=2)
    submit = Button(
        screen, text="student", bg="#9ad3bc", fg="black", command=student_graph
    )
    submit.grid(row=3, column=4)
    screen.mainloop()
