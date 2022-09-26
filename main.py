import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_string = ""
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    global reps, check_string
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    check_string = ""
    check_text.config(text=f"{check_string}")
    title.config(text="Timer")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer_mechanism():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        counter_fun(long_break_sec)
        title.config(text="Break Time", fg=f'{PINK}')
    elif reps % 2 == 0:
        counter_fun(work_sec)
        title.config(text="Work Time", fg=f'{RED}')
    else:
        counter_fun(short_break_sec)
        title.config(text="Break Time", fg=f'{GREEN}')


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def counter_fun(count):
    global timer, check_string
    count_min = math.floor(count / 60)
    count_sec = round(count % 60)
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    elif count_min < 10:
        count_min = f"0{count_min}"
    time = f"{count_min}:{count_sec}"

    canvas.itemconfig(timer_text, text=f"{time}")
    if count > 0:
        timer = window.after(1000, counter_fun, count - 1)
    else:
        timer_mechanism()
        work_done = math.floor(reps / 2)
        for _ in range(work_done):
            check_string += "✔"
        check_text.config(text=f"{check_string}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", font=(FONT_NAME, 20, "bold"), background=YELLOW, fg=GREEN)
title.pack()

canvas = Canvas(width=200, height=223, background=YELLOW, bd=0, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.pack(pady=20)


start_btn = Button(text="Start", command=timer_mechanism)
start_btn.place(x=0, y=300)

reset_btn = Button(text="Reset", command=timer_reset)
reset_btn.place(x=160, y=300)

check_text = Label(text=f"{check_string}", fg=GREEN, bg=YELLOW, font=40)
check_text.pack()

window.mainloop()
