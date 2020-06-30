from win10toast import ToastNotifier
import tkinter as tk
import time
from matplotlib import pyplot


def checkTime():
    current_time = time.strftime('%H:%M:%S')

    if current_time == '20:00:00':
        notify.show_toast('Track Your Mood!', 'Time to update your mood tracker!', duration=5, threaded=True)

    root.after(1000, checkTime)


def printMood(mood):
    current_time = int(time.time())

    with open('data.txt', 'a') as f:
        f.write(str(current_time) + ' ' + str(mood) + '\n')


def readFile():
    with open('data.txt', 'r') as f:
        content = [line.rstrip() for line in f]

    times = []
    moods = []

    for entry in content:
        split_string = entry.split(' ')
        times.append(int(split_string[0]))
        moods.append(int(split_string[1]))

    return times, moods


def plotData():
    times_moods = readFile()
    x = times_moods[0]
    y = times_moods[1]

    pyplot.plot(x, y, 'b-')
    pyplot.show()


notify = ToastNotifier()

root = tk.Tk()
root.resizable(0, 0)
root.title('Mood Tracker')

canvas = tk.Canvas(root, bg='black', width=900, height=300)
canvas.pack()

button_1 = tk.Button(root, bg='red', text='1', command=lambda: printMood(1))
button_1.place(width=100, height=100, x=25, y=50)
button_2 = tk.Button(root, bg='orange', text='2', command=lambda: printMood(2))
button_2.place(width=100, height=100, x=150, y=50)
button_3 = tk.Button(root, bg='gold', text='3', command=lambda: printMood(3))
button_3.place(width=100, height=100, x=275, y=50)
button_4 = tk.Button(root, bg='yellow', text='4', command=lambda: printMood(4))
button_4.place(width=100, height=100, x=400, y=50)
button_5 = tk.Button(root, bg='pale green', text='5', command=lambda: printMood(5))
button_5.place(width=100, height=100, x=525, y=50)
button_6 = tk.Button(root, bg='green2', text='6', command=lambda: printMood(6))
button_6.place(width=100, height=100, x=650, y=50)
button_7 = tk.Button(root, bg='green4', text='7', command=lambda: printMood(7))
button_7.place(width=100, height=100, x=775, y=50)
button_plot = tk.Button(root, bg='white', text='Plot Data', command=plotData)
button_plot.place(width=200, height=50, x=350, y=200)

checkTime()

root.mainloop()
