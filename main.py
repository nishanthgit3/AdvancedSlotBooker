import json
import requests
import sys
import threading
import time
from tkinter import *

# Root window
root  = Tk()
root.title("Advanced Slot Booker")
root.geometry("925x300")

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
        print("getCourse: " + noCookieError)

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
        print("getCourseId: " + noCookieError)

def getSlotId():
    url = 'https://ps.bitsathy.ac.in/api/ps_v2/slots/available?id=' + str(courseId)
    try:
        r = requests.get(url, headers=headers)
        rJson = r.json()
        if not rJson:
            print("No slots available")
        else:
            l = len(rJson)
            chosenSlot = 0
            if l < int(slotNo.get()):
                chosenSlot = l - 1 
            else:
                chosenSlot = int(slotNo.get()) - 1
            global slotId
            chosenJson = rJson[chosenSlot]
            slotId = chosenJson["id"]
            print(chosenJson["label"])
    except:
        print("getSlotId: " + noCookieError)

def bookSlot():
    url = 'https://ps.bitsathy.ac.in/api/ps_v2/slots/register'
    payload = {}
    payload['slot_id'] = int(slotId)
    payload['register_id'] = int(registerId)
    r = requests.put(url, headers=headers, data=payload)

# GUI
def cookieButtonClick():
    cookieButton['state'] = DISABLED
    cookie = cookieEntry.get()
    global headers 
    headers = {'Host':'ps.bitsathy.ac.in', 'Cookie': 'PS='+cookie}
    getCourse()

def startButtonClick():
    getRegisterId()
    getCourseId()
    getSlotId()
    # Timer
    while 1:  
        t = time.localtime()
        currentTime = time.strftime("%H:%M:%S", t)
        if currentTime == "20:00:01":
            bookSlot()
            break

def threadStartButton():
    thread = threading.Thread(target=startButtonClick)
    thread.daemon = True
    thread.start()

def showCourseMenu():
    global course
    course = StringVar()
    course.set("Select a course")
    coursesMenu = OptionMenu(root, course, *allCourses)
    coursesMenu.grid(row=1, column=1)
    startButton['state'] = NORMAL

# Creating
# Row 0 Cookie
cookieText = Label(root, text="Cookie")
cookieEntry = Entry(root, width=50)
cookieButton = Button(root, text="✓", command=cookieButtonClick, state=NORMAL)
startButton = Button(root, text="Start", command=threadStartButton, state=DISABLED)

# Row 2 SlotNo
slotNo = StringVar()
slotNo.set("Select a slot number")
slotNoMenu = OptionMenu(root, slotNo, "1", "2", "3", "4", "5")

# Showing/Grids
cookieText.grid(row=0, column=0)
cookieEntry.grid(row=0, column=1)
cookieButton.grid(row=0, column=2)
slotNoMenu.grid(row=2, column=1)
startButton.grid(row=3, column=1)

root.mainloop()