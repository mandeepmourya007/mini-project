import pandas as pd
import numpy as np
from tkinter import *
import csv
import matplotlib.pyplot as plt
import csv
import time
import datetime
import tkinter
from tkinter import messagebox

import os.path
from os import path

# START_ROW = 25
TOTAL_STUDENT = 15
# list of  subjects
SUBJECTS = ["PPR", "ADA", "MATHS", "RM"]
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
       # print(rows[i])
        lines[i][SUBJECTS.index(s)] = rows[i]
    # print(lines, SUBJECTS.index(s))
   # print(lines)
    writer = csv.writer(open("testing.csv", "w"))
    writer.writerows(lines)


def onClick(i):
    # print("present: MIT" + str(2020000 + i))
    rows[i] = 1 if rows[i] == 0 else 1

    # print((roll))
    return


def show():
   # s = get_subject()
    #print("call funtion to show graph of " + s)

    def column(matrix, i):
        return [row[i] for row in matrix]
    sum_of_day=[]
    sub = str(input())
    print("showing graph of " + sub)
    for j in range(1,20):
        s = str(j)
        s += '.csv'
        r = np.genfromtxt(s, delimiter=',', names=True)
        Attendence = [0 for i in range(4)] 
        for i in range(110):
            Attendence[0] += r[i][0]
            Attendence[1] += r[i][1]
            Attendence[2] += r[i][2]
            Attendence[3] += r[i][3]
        sum_of_day.append(Attendence)   
    t = np.arange(0, 19 , 1)
    if(sub == 'ADA'):
      plt.plot(t,column(sum_of_day,0),'ro-',label = 'ADA')
    if(sub == 'RM'):
      plt.plot(t,column(sum_of_day,1),'ro-',label = 'RM')
    if(sub == 'MATH'):
      plt.plot(t,column(sum_of_day,2),'ro-',label = 'MATH')
    if(sub == 'PPR'):
      plt.plot(t,column(sum_of_day,3),'ro-',label = 'PPR')
    plt.xticks(t)
    plt.xlabel("Perticular Day")
    plt.ylabel("Attendence on that day for perticular subject")
    plt.show()


def today_graph_show():
    print("call funtion to show graph of today ")
    file = open("testing.csv")
    lt = np.loadtxt(file, delimiter=",")

        # lt = [np.round(x) for x in lt]
        # print(lt)
    count1=0
    global A
    a = lt[:, 0]
    A=a
    b = lt[:, 1]
    c = lt[:, 2]
    d = lt[:, 3]
    for i in range(15):
        if a[i]==1 or b[i]==1 or c[i]==1 or d[i]==1:
                count1+=1
        
    fig = plt.figure(figsize=(15,4 ))
    plt.xticks(x_pos,x,rotation='270')
    plt.yticks([])
    bar_plot=plt.bar(x_pos, a, width=0.5, label="ADA")
    bar_plot=plt.bar(x_pos , b, width=0.5, label="PPR")
    bar_plot=plt.bar(x_pos , c, width=0.5, label="MATH")
    bar_plot=plt.bar(x_pos , d, width=0.5, label="PM")
    print("Attendence Recorded Successfully")
    print("No of Students Attended the class:",count1)
       
        # plt.tight_layout()
    plt.xlabel("RollNo")
    plt.ylabel("Absent-0   Present-1")
    plt.show()


def get_roll():
    roll = txt_roll.get()[-3:]
    return roll


def student_graph():
    s = get_roll()
    print("graph of studnet" + s)
    
    student = int(input("Enter enroll no student you want attendence Details :- "))
    presence = [0,0,0,0]
    print(student)
    for j in range(1,20):
        s = str(j)
        s += '.csv'
        r = np.genfromtxt(s, delimiter=',', names=True)
        presence[0] += r[student][0]
        presence[1] += r[student][1]
        presence[2] += r[student][2]
        presence[3] += r[student][3]
    absence = [20 - presence[0] ,20 - presence[1],20 - presence[2],20 - presence[3]]
    labels = 'ADA-presence', 'ADA-absence', 'RM-presence', 'RM-absence','PPR-presence','PPR-absence', 'MATH-presence','MATH-absence'
    sizes = [100*(presence[0]/20),100*(absence[0]/20),100*(presence[1]/20),100*(absence[1]/20),
             100*(presence[2]/20),100*(absence[2]/20),100*(presence[3]/20),100*(absence[3]/20)]
    explode = (0, 0.1,0, 0.1,0, 0.1,0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=180)
    ax1.axis('equal')

    plt.show()


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
    x=['MIT2020101','MIT2020102','MIT2020103','MIT2020104','MIT2020105','MIT2020106','MIT2020107','MIT2020108','MIT2020109','MIT2020101','MIT2020111','MIT2020112','MIT202013','MIT2020114','MIT2020115']

    x_pos = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    A=1
  #  def today_graph_show():
       
    submit = Button(screen, text="Submit", bg="red", fg="black", command=save)
    submit.grid(row=3, column=1)
    l1 = Label(screen, text="Enter roll")
    l1.grid(row=3, column=2, sticky=W, pady=2)
    txt_roll = Entry(screen)

    # this will arrange entry widgets
    txt_roll.grid(row=3, column=3, pady=2)
    submit = Button(screen, text="student", bg="red", fg="black", command=student_graph)
    submit.grid(row=3, column=4)

    
    screen.mainloop()
