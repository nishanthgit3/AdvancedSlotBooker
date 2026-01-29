import json
import requests
from tkinter import *

# Root window
root  = Tk()
root.title("Advanced Slot Booker")
icon = PhotoImage(file="logo.png")
root.iconphoto(True, icon)
root.geometry("925x400")

# Functions
# Logics
allCourses = ["No courses available"]
noCookieError = "Please enter a cookie before requesting for the courses"
def getCourse():
    url = 'https://ps.bitsathy.ac.in/api/ps_v2/my-course?tab=personalizedSkills'
    try:
        r = requests.get(url, headers=headers)
        global data
        data = r.json()
        global allCourses
        allCourses = []
        for i in data:
            allCourses.append(i["name"])
        showCourseMenu()
    except:
        print(noCookieError)

def getRegisterId():
    courseText = course.get()
    for i in data:
        if i["name"] == courseText:
            global registerId
            registerId = i["id"]

def getCourseId():
    url = 'https://ps.bitsathy.ac.in/api/ps_v2/my-course/details?id=' + str(registerId) + '&courseMaterial=1'
    try:
        r = requests.get(url, headers=headers)
        rJson = r.json()
        global courseId
        courseId = rJson["course_id"]
    except:
        print(noCookieError)

def getSlotId():
    url = 'https://ps.bitsathy.ac.in/api/ps_v2/slots/available?id=775' + str(courseId)
    try:
        r = requests.get(url, headers=headers)
        rJson = r.json()
        global courseId
        courseId = rJson["course_id"]
    except:
        print(noCookieError)

# GUI
def cookieButtonClick():
    cookie = cookieEntry.get()
    global headers 
    headers = {'Host':'ps.bitsathy.ac.in', 'Cookie': 'PS='+cookie}
    getCourse()

def startButtonClick():
    getRegisterId()
    getCourseId()

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
startButton = Button(root, text="Start", command=startButtonClick)

# Showing/Grids
cookieText.grid(row=0, column=0)
cookieEntry.grid(row=0, column=1)
cookieButton.grid(row=0, column=2)
startButton.grid(row=2, column=1)

root.mainloop()