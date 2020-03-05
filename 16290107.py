
from tkinter import *
import tkinter.messagebox
import random
import time

window = Tk()

window.geometry("600x700")
window.title("DEEP BRAIN")
window.configure(background="sky blue")

global count 
global w
global h
global entry
global array
global lab1
global lab2
global but_1
global but_2
w = 50
h = 90
count = 5


def fight():
   global count
   flag=0
   str = entry.get()
   for i in range(0, count):
      if int(str[i]) != array[i]:
         ans = tkinter.messagebox.askquestion('WRONG', 'WRONG ANSWER\nPLAY AGAIN')
         if ans == 'yes':
            entry.destroy()
            but_2.destroy()
            lab1.destroy()
            but_1.destroy()
            array.clear()
            window.update()
            count=5
            begin()
         else:
            flag=1
            break
      else:
         continue

   if flag == 1:
      window.quit()
   else:
      ans = tkinter.messagebox.askquestion('AMAZING', 'CORRECT ANSWER\nGO TO NEXT LEVEL')

      if ans != 'yes':
         window.quit()
      else:
         entry.destroy()
         but_2.destroy()
         lab1.destroy()
         but_1.destroy()
         array.clear()
         window.update()
         count = count + 1
         begin()

def show():

   for i in range(0, count):
      n = random.randint(0, 9)
      array.append(n)
      lab2 = Label(window, text=array[i], bg="sky blue", fg="black", font=(None, 10))
      lab2.pack()
      w = random.randint(1, 600)
      h = random.randint(1, 500)
      lab2.place(x=w, y=h)
      window.update()
      time.sleep(2)
      lab2.place_forget()
      lab2.destroy()
      window.update()
   print(array)

def begin():
   global entry
   global count
   global lab1
   global lab2
   global but_1
   global but_2
   global entry
   lab1 = Label(window, text="Enter the numbers:", bg="slate gray", fg="black", font=(None, 10))
   entry = Entry(window, bg="gray75", font=(None, 12))
   but_1 = Button(window, text="CHECK", bg="plum2", fg="black", font=(None, 10), command=fight)
   but_2 = Button(window, text="QUIT", bg="gold", fg="black", font=(None, 10), command=window.quit)
   print(entry.get())
   lab1.place(x=120, y=560)
   entry.place(x=235, y=560)
   but_1.place(x=260, y=610)
   but_2.place(x=330, y=610)



   global array
   array = []
   show()




begin()

window.mainloop()