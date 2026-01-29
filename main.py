import json
import requests
from tkinter import *

# Root window
root  = Tk()
root.title("Advanced Slot Booker")
icon = PhotoImage(file="logo.png")
root.iconphoto(True, icon)
root.geometry("925x800")

# Functions
# Logics
allCourses = ["No courses available"]
def getCourse():
    url = 'https://ps.bitsathy.ac.in/api/ps_v2/my-course?tab=personalizedSkills'
    try:
        r = requests.get(url, headers=headers)
        data = r.json()
        global allCourses
        allCourses = []
        for i in data:
            allCourses.append(i["name"])
        showCourseMenu()
    except:
        print("Please enter a cookie before requesting for the courses")

def getRegisterId():
    for i in data:
        if i["name"] == course:
            global registerId
            registerId = i["id"]

# GUI
def cookieButtonClick():
    cookie = cookieEntry.get()
    global headers 
    headers = {'Host':'ps.bitsathy.ac.in', 'Cookie': 'PS='+cookie}
    getCourse()

def showCourseMenu():
    global course
    course = StringVar()
    course.set("Select a course")
    coursesMenu = OptionMenu(root, course, *allCourses)
    coursesMenu.grid(row=1, column=1)

# Creating
# Row 1
cookieText = Label(root, text="Cookie")
cookieEntry = Entry(root, width=50)
cookieButton = Button(root, text="✓", command=cookieButtonClick)


# Showing/Grids
cookieText.grid(row=0, column=0)
cookieEntry.grid(row=0, column=1)
cookieButton.grid(row=0, column=2)

root.mainloop()