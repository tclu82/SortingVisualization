import sys
import time

if sys.version_info[0] == 3:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
else:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter

def bubbleSort(lst):
    for number in range(len(lst)-1, 0, -1):
        for i in range(number):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                print(lst)
                for j in lst:
                    cv.delete([j])
                animation()
                cv.delete(ALL)
                cv.update()

def animation():
    x , y = 220, 500
    barWidth = 15

    for item in lst:
        cv.delete([item])
        bar = cv.create_rectangle(x, y, x+barWidth, y-(item*15), fill="red")
        x += barWidth + 5
        time.sleep(0.2)
        cv.update()

#Canvas
root = Tk()
root.title("Sorting Algorithm Animation")
w = 800
h = 600
cv = Canvas(width=w, height=h, bg='black')
cv.pack()
cv.update()

lst = [1,2,7,3,6,4,5,10,8,9,12,15,11,13,16,14,20,17,19,18]
bubbleSort(lst)
animation()
root.mainloop()
