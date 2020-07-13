from win10toast import ToastNotifier
import tkinter as tk
import time as _time
from matplotlib import pyplot


# Check current time, send windows notification if time is 8:00PM
def check_time():
    current_time = _time.strftime('%H:%M:%S')

    if current_time == '20:00:00':
        notify.show_toast('Track Your Mood!', 'Time to update your mood tracker!', duration=5, threaded=True)

    # Call self 1 second later
    root.after(1000, check_time)


# Log mood and timestamp to data.txt
def print_mood(mood):
    current_time = int(_time.time())

    with open('data.txt', 'a') as f:
        f.write(str(current_time) + ' ' + str(mood) + '\n')


# Read data.txt line by line, separate into timestamp and mood, return all time and seven day moods and times
def read_file():
    with open('data.txt', 'r') as f:
        content = [line.rstrip() for line in f]

    times = []
    moods = []
    times_sd = []
    moods_sd = []

    for entry in content:
        time, mood = entry.split(' ')
        times.append(int(time))
        moods.append(int(mood))

        if int(time) > _time.time() - 604800:
            times_sd.append(int(time))
            moods_sd.append(int(mood))

    return times, moods, times_sd, moods_sd


# Plot all time data, all time average and seven day average
def plot_at():
    times, moods, _, moods_sd = read_file()

    sd_avg = sum(moods_sd) / len(moods_sd)
    at_avg = sum(moods) / len(moods)

    pyplot.plot(times, moods, 'bo-')
    pyplot.axhline(sd_avg, color='r')
    pyplot.axhline(at_avg, color='y')

    pyplot.legend(['Mood', '7 Day Average', 'All Time Average'])
    pyplot.show()


# Plot seven day data and seven day average
def plot_sd():
    _, _, times_sd, moods_sd = read_file()

    sd_avg = sum(moods_sd) / len(moods_sd)

    pyplot.plot(times_sd, moods_sd, 'bo-')
    pyplot.axhline(sd_avg, color='r')

    pyplot.legend(['Mood', '7 Day Average'])
    pyplot.show()


# Initialize Toast Notifier
notify = ToastNotifier()

# Initialize tkinter root, lock size and set title
root = tk.Tk()
root.resizable(0, 0)
root.title('Mood Tracker')

# Initialize tkinter canvas
canvas = tk.Canvas(root, bg='black', width=900, height=300)
canvas.pack()

# Initialize buttons for mood logging
button_1 = tk.Button(root, bg='red', text='1', command=lambda: print_mood(1))
button_1.place(width=100, height=100, x=25, y=50)
button_2 = tk.Button(root, bg='orange', text='2', command=lambda: print_mood(2))
button_2.place(width=100, height=100, x=150, y=50)
button_3 = tk.Button(root, bg='gold', text='3', command=lambda: print_mood(3))
button_3.place(width=100, height=100, x=275, y=50)
button_4 = tk.Button(root, bg='yellow', text='4', command=lambda: print_mood(4))
button_4.place(width=100, height=100, x=400, y=50)
button_5 = tk.Button(root, bg='pale green', text='5', command=lambda: print_mood(5))
button_5.place(width=100, height=100, x=525, y=50)
button_6 = tk.Button(root, bg='green2', text='6', command=lambda: print_mood(6))
button_6.place(width=100, height=100, x=650, y=50)
button_7 = tk.Button(root, bg='green4', text='7', command=lambda: print_mood(7))
button_7.place(width=100, height=100, x=775, y=50)

# Initialize buttons for plotting
button_plot_at = tk.Button(root, bg='white', text='Plot All Time Data', command=plot_at)
button_plot_at.place(width=200, height=50, x=225, y=200)
button_plot_sd = tk.Button(root, bg='white', text='Plot 7 Day Data', command=plot_sd)
button_plot_sd.place(width=200, height=50, x=475, y=200)

# Call check_time once to initialize call loop
check_time()

# tkinter main loop
root.mainloop()
