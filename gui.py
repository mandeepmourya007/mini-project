from tkinter import *
import csv
#main
def run():
    name1 = lecture.get()
    print(name1)
    # for i in :
    a=text_box.get("1.0", END).split()
    print(a)
    rows = []
    for i in a:
        rows+=[[i]]
    
    with open("test.csv", 'w') as csvfile: 
    
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow([name1]) 
    
        csvwriter.writerows(rows)
  
screen = Tk()
screen.title("Attendance")
screen.geometry("500x500")

welcome_text = Label(text = "Welcome to our Attendance program ", fg = "red", bg = "yellow")
welcome_text.pack()

click_me = Button(text = "Click me", fg = "red", bg = "yellow", command = run)
click_me.place(x = 10, y =20)

lecture = StringVar()
lecture_name = Entry(textvariable = lecture)
lecture_name.pack()
text_box = Text()
text_box.pack()

# T = Text(screen, height = 20, width = 25) 


# T.insert(END, "") 
# T.pack() 
screen.mainloop()