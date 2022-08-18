from tkinter import Tk, Label, Entry, Button, messagebox, Text
import time
import threading


def start(event):
    """Start the global timer."""
    global running
    global counter
    counter = 0
    if not running:
        running = True
        t = threading.Thread(target=time_thread)
        t.start()


def reset():
    """Reset timer and global variables."""
    global running
    global counter
    running = False
    counter = 0
    textbox.delete('1.0', 'end')

def time_thread():
    """Get text from text box and split it by spaces."""
    """Then divide it by seconds to calculate WPM."""
    global running
    global counter
    while running:
        time.sleep(1)
        counter += 1
        textbox.bind("<KeyPress>", start)
        if counter > 5:
            print("reset")
            reset()



window = Tk()
window.title("Keep Typing!")
window.config(padx=50, pady=50, bg="white")

label = Label(text="Keep typing or loose all your progress",
              bg="white",
              font=("Arial", 16))
label.grid(column=0, row=0)


textbox = Text(window, width=80, height=20)
textbox.grid(column=0, row=1, pady=10)
textbox.focus()
textbox.bind("<KeyPress>", start)

button = Button(text="Reset",
                command=reset,
                width=14,
                font=("Arial", 12))

button.grid(sticky='w', column=0, row=2,
            columnspan=2, pady=10)

stop = Button(text="Quit",
              command=window.destroy,
              font=("Arial", 12))

stop.grid(sticky='e', column=0, row=2,
          columnspan=2, pady=10)


counter = 0
running = False

window.mainloop()
