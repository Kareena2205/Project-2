from tkinter import *
import tkinter.messagebox
import math

root = Tk()
root.geometry("650x400+300+300")
root.title("Scientific Calculator")

angle_flag = None

# number button handlers

def num_one():
    if display.get() == '0':
        display.delete(0, END)
    pos = len(display.get())
    display.insert(pos, '1')

def num_two():
    if display.get() == '0':
        display.delete(0, END)
    pos = len(display.get())
    display.insert(pos, '2')

def num_three():
    if display.get() == '0':
        display.delete(0, END)
    pos = len(display.get())
    display.insert(pos, '3')

def num_four():
    if display.get() == '0':
        display.delete(0, END)
    pos = len(display.get())
    display.insert(pos, '4')

def num_five():
    if display.get() == '0':
        display.delete(0, END)
    pos = len(display.get())
    display.insert(pos, '5')

def num_six():
    if display.get() == '0':
        display.delete(0, END)
    pos = len(display.get())
    display.insert(pos, '6')

def num_seven():
    if display.get() == '0':
        display.delete(0, END)
    pos = len(display.get())
    display.insert(pos, '7')

def num_eight():
    if display.get() == '0':
        display.delete(0, END)
    pos = len(display.get())
    display.insert(pos, '8')

def num_nine():
    if display.get() == '0':
        display.delete(0, END)
    pos = len(display.get())
    display.insert(pos, '9')

def num_zero():
    if display.get() == '0':
        display.delete(0, END)
    pos = len(display.get())
    display.insert(pos, '0')

def clear_leading_zero(*args):
    if display.get() == '0':
        display.delete(0, END)

def add_plus():
    pos = len(display.get())
    display.insert(pos, '+')

def add_minus():
    pos = len(display.get())
    display.insert(pos, '-')

def add_multiply():
    pos = len(display.get())
    display.insert(pos, '*')

def add_divide():
    pos = len(display.get())
    display.insert(pos, '/')

def clear_all(*args):
    display.delete(0, END)
    display.insert(0, '0')

def calc_sin():
    try:
        result = float(display.get())
        if angle_flag is True:
            result = math.sin(math.radians(result))
        else:
            result = math.sin(result)
        display.delete(0, END)
        display.insert(0, str(result))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def calc_cos():
    try:
        result = float(display.get())
        if angle_flag is True:
            result = math.cos(math.radians(result))
        else:
            result = math.cos(result)
        display.delete(0, END)
        display.insert(0, str(result))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def calc_tan():
    try:
        result = float(display.get())
        if angle_flag is True:
            result = math.tan(math.radians(result))
        else:
            result = math.tan(result)
        display.delete(0, END)
        display.insert(0, str(result))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def calc_arcsin():
    try:
        result = float(display.get())
        if angle_flag is True:
            result = math.degrees(math.asin(result))
        else:
            result = math.asin(result)
        display.delete(0, END)
        display.insert(0, str(result))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def calc_arccos():
    try:
        result = float(display.get())
        if angle_flag is True:
            result = math.degrees(math.acos(result))
        else:
            result = math.acos(result)
        display.delete(0, END)
        display.insert(0, str(result))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def calc_arctan():
    try:
        result = float(display.get())
        if angle_flag is True:
            result = math.degrees(math.atan(result))
        else:
            result = math.atan(result)
        display.delete(0, END)
        display.insert(0, str(result))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def insert_power():
    pos = len(display.get())
    display.insert(pos, '**')

def do_round():
    try:
        result = float(display.get())
        result = round(result)
        display.delete(0, END)
        display.insert(0, str(result))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def do_log10():
    try:
        result = float(display.get())
        result = math.log10(result)
        display.delete(0, END)
        display.insert(0, str(result))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def do_factorial():
    try:
        result = float(display.get())
        result = math.factorial(result)
        display.delete(0, END)
        display.insert(0, str(result))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def do_sqrt():
    try:
        result = float(display.get())
        result = math.sqrt(result)
        display.delete(0, END)
        display.insert(0, str(result))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def insert_dot():
    pos = len(display.get())
    display.insert(pos, '.')

def insert_pi():
    if display.get() == '0':
        display.delete(0, END)
    pos = len(display.get())
    display.insert(pos, str(math.pi))

def insert_e():
    if display.get() == '0':
        display.delete(0, END)
    pos = len(display.get())
    display.insert(pos, str(math.e))

def open_paren():
    pos = len(display.get())
    display.insert(pos, '(')

def close_paren():
    pos = len(display.get())
    display.insert(pos, ')')

def do_backspace():
    pos = len(display.get())
    current_text = str(display.get())
    if current_text == '':
        display.insert(0, '0')
    elif current_text == ' ':
        display.insert(0, '0')
    elif current_text == '0':
        pass
    else:
        display.delete(0, END)
        display.insert(0, current_text[0:pos-1])

def toggle_angle_mode():
    global angle_flag
    if angle_flag is None:
        angle_flag = True
        angle_toggle_btn['text'] = "Deg"
    else:
        angle_flag = None
        angle_toggle_btn['text'] = "Rad"

def do_ln():
    try:
        result = float(display.get())
        result = math.log(result)
        display.delete(0, END)
        display.insert(0, str(result))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def insert_mod():
    pos = len(display.get())
    display.insert(pos, '%')

def evaluate(*args):
    try:
        result = display.get()
        result = eval(result)
        display.delete(0, END)
        display.insert(0, result)
    except:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# MAIN ENTRY FIELD

display = Entry(
    root,
    font="Verdana 20",
    fg="black",
    bg="#abbab1",
    bd=0,
    justify=RIGHT,
    insertbackground="#abbab1",
    cursor="arrow"
)
display.insert(0, '0')
display.pack(expand=TRUE, fill=BOTH)

# UNIVERSAL BUTTON COLOR (NAVY BLUE)
BTN_COLOR = "#001f4d"

# --- FIRST ROW ---
top_row = Frame(root, bg="#000000")
top_row.pack(expand=TRUE, fill=BOTH)

pi_btn = Button(top_row, text="π", font="Segoe 18", relief=GROOVE, bd=0,
                command=insert_pi, fg="white", bg=BTN_COLOR)
pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

fact_btn = Button(top_row, text=" x! ", font="Segoe 18", relief=GROOVE, bd=0,
                  command=do_factorial, fg="white", bg=BTN_COLOR)
fact_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sin_btn = Button(top_row, text="sin", font="Segoe 18", relief=GROOVE, bd=0,
                 command=calc_sin, fg="white", bg=BTN_COLOR)
sin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cos_btn = Button(top_row, text="cos", font="Segoe 18", relief=GROOVE, bd=0,
                 command=calc_cos, fg="white", bg=BTN_COLOR)
cos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tan_btn = Button(top_row, text="tan", font="Segoe 18", relief=GROOVE, bd=0,
                 command=calc_tan, fg="white", bg=BTN_COLOR)
tan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_1 = Button(top_row, text="1", font="Segoe 23", relief=GROOVE, bd=0,
                  command=num_one, fg="white", bg=BTN_COLOR)
button_1.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_2 = Button(top_row, text="2", font="Segoe 23", relief=GROOVE, bd=0,
                  command=num_two, fg="white", bg=BTN_COLOR)
button_2.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_3 = Button(top_row, text="3", font="Segoe 23", relief=GROOVE, bd=0,
                  command=num_three, fg="white", bg=BTN_COLOR)
button_3.pack(side=LEFT, expand=TRUE, fill=BOTH)

plus_btn = Button(top_row, text="+", font="Segoe 23", relief=GROOVE, bd=0,
                  command=add_plus, fg="white", bg=BTN_COLOR)
plus_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

# --- SECOND ROW ---
second_row = Frame(root)
second_row.pack(expand=TRUE, fill=BOTH)

e_btn = Button(second_row, text="e", font="Segoe 18", relief=GROOVE, bd=0,
               command=insert_e, fg="white", bg=BTN_COLOR)
e_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sqrt_btn = Button(second_row, text=" √x ", font="Segoe 18", relief=GROOVE, bd=0,
                  command=do_sqrt, fg="white", bg=BTN_COLOR)
sqrt_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

asin_btn = Button(second_row, text="sin−1", font="Segoe 11 bold", relief=GROOVE, bd=0,
                  command=calc_arcsin, fg="white", bg=BTN_COLOR)
asin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

acos_btn = Button(second_row, text="cos-1", font="Segoe 11 bold", relief=GROOVE, bd=0,
                  command=calc_arccos, fg="white", bg=BTN_COLOR)
acos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

atan_btn = Button(second_row, text="tan-1", font="Segoe 11 bold", relief=GROOVE, bd=0,
                  command=calc_arctan, fg="white", bg=BTN_COLOR)
atan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_4 = Button(second_row, text="4", font="Segoe 23", relief=GROOVE, bd=0,
                  command=num_four, fg="white", bg=BTN_COLOR)
button_4.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_5 = Button(second_row, text="5", font="Segoe 23", relief=GROOVE, bd=0,
                  command=num_five, fg="white", bg=BTN_COLOR)
button_5.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_6 = Button(second_row, text="6", font="Segoe 23", relief=GROOVE, bd=0,
                  command=num_six, fg="white", bg=BTN_COLOR)
button_6.pack(side=LEFT, expand=TRUE, fill=BOTH)

minus_btn = Button(second_row, text="-", font="Segoe 23", relief=GROOVE, bd=0,
                   command=add_minus, fg="white", bg=BTN_COLOR)
minus_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

# --- THIRD ROW ---
third_row = Frame(root)
third_row.pack(expand=TRUE, fill=BOTH)

angle_toggle_btn = Button(third_row, text="Rad", font="Segoe 12 bold",
                          relief=GROOVE, bd=0, command=toggle_angle_mode,
                          fg="white", bg=BTN_COLOR)
angle_toggle_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

round_btn = Button(third_row, text="round", font="Segoe 10 bold",
                   relief=GROOVE, bd=0, command=do_round,
                   fg="white", bg=BTN_COLOR)
round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

ln_btn = Button(third_row, text="ln", font="Segoe 18",
                relief=GROOVE, bd=0, command=do_ln,
                fg="white", bg=BTN_COLOR)
ln_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

log_btn = Button(third_row, text="log", font="Segoe 17",
                 relief=GROOVE, bd=0, command=do_log10,
                 fg="white", bg=BTN_COLOR)
log_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

power_btn = Button(third_row, text="x^y", font="Segoe 17",
                   relief=GROOVE, bd=0, command=insert_power,
                   fg="white", bg=BTN_COLOR)
power_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_7 = Button(third_row, text="7", font="Segoe 23",
                  relief=GROOVE, bd=0, command=num_seven,
                  fg="white", bg=BTN_COLOR)
button_7.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_8 = Button(third_row, text="8", font="Segoe 23",
                  relief=GROOVE, bd=0, command=num_eight,
                  fg="white", bg=BTN_COLOR)
button_8.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_9 = Button(third_row, text="9", font="Segoe 23",
                  relief=GROOVE, bd=0, command=num_nine,
                  fg="white", bg=BTN_COLOR)
button_9.pack(side=LEFT, expand=TRUE, fill=BOTH)

multiply_btn = Button(third_row, text="*", font="Segoe 23",
                      relief=GROOVE, bd=0, command=add_multiply,
                      fg="white", bg=BTN_COLOR)
multiply_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

# --- FOURTH ROW ---
fourth_row = Frame(root)
fourth_row.pack(expand=TRUE, fill=BOTH)

mod_btn = Button(fourth_row, text="%", font="Segoe 21",
                 relief=GROOVE, bd=0, command=insert_mod,
                 fg="white", bg=BTN_COLOR)
mod_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

open_btn = Button(fourth_row, text=" ( ", font="Segoe 21",
                  relief=GROOVE, bd=0, command=open_paren,
                  fg="white", bg=BTN_COLOR)
open_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

close_btn = Button(fourth_row, text=" ) ", font="Segoe 21",
                   relief=GROOVE, bd=0, command=close_paren,
                   fg="white", bg=BTN_COLOR)
close_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

dot_btn = Button(fourth_row, text=" • ", font="Segoe 21",
                 relief=GROOVE, bd=0, command=insert_dot,
                 fg="white", bg=BTN_COLOR)
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

clear_btn = Button(fourth_row, text="C", font="Segoe 23",
                   relief=GROOVE, bd=0, command=clear_all,
                   fg="white", bg=BTN_COLOR)
clear_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

backspace_btn = Button(fourth_row, text="⌫", font="Segoe 20",
                       relief=GROOVE, bd=0, command=do_backspace,
                       fg="white", bg=BTN_COLOR)
backspace_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

button_0 = Button(fourth_row, text="0", font="Segoe 23",
                  relief=GROOVE, bd=0, command=num_zero,
                  fg="white", bg=BTN_COLOR)
button_0.pack(side=LEFT, expand=TRUE, fill=BOTH)

equal_btn = Button(fourth_row, text="=", font="Segoe 23",
                   relief=GROOVE, bd=0, command=evaluate,
                   fg="white", bg=BTN_COLOR)
equal_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

divide_btn = Button(fourth_row, text="/", font="Segoe 23",
                    relief=GROOVE, bd=0, command=add_divide,
                    fg="white", bg=BTN_COLOR)
divide_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

root.mainloop()
