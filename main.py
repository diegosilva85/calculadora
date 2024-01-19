from tkinter import *

# Setup
BLUE = "#C5FFF8"
FONT = ("Arial", 30, "bold")
WIDTH_BUTTON = 6
HEIGHT_BUTTON = 4
screen = Tk()
screen.title("Calculator App")
screen.geometry("340x400")
screen.resizable(width=False, height=False)
screen.config(padx=50, pady=50)
operand = ""
operator = ""
result = None


# Calculator Functions
def clear():
    global operand
    operand = ""
    label.config(text="0")


def press_num(num):
    global operand
    global result
    if operand == result:
        operand = ""
    if len(operand) < 12:
        operand = operand + num
        label.config(text=operand)
    else:
        pass


def press_operator(op):
    global operand
    global operator
    global result
    operator = op
    result = float(operand)
    operand = ""


def equal():
    global operand
    global operator
    global result
    second_operand = float(operand)
    # Operations
    if operator == "+":  # Add
        result += second_operand
    elif operator == "-":  # Subtract
        result -= second_operand
    elif operator == "X":  # Multiply
        result *= second_operand
    elif operator == "/":  # Divide
        if second_operand == 0:  # Test division by zero
            result = "error"
        else:
            result /= second_operand
    elif operator == "%":  # Percentage
        result *= second_operand / 100
    elif operator == "exp":  # Exponential
        result **= second_operand
    result = str(result)
    # Remove floating point from an integer result
    if result[-1] == "0" and result[-2] == ".":
        result = result.replace(".0", "")
    # Maximum length of characters
    if len(result) <= 12:
        pass
    else:
        result = result[0:12]
        if "." not in result:
            result = "error"
    label.config(text=result)
    operand = result
    operator = ""


# Label for calculations
label = Label(text="0", font=FONT, bg=BLUE, width=11, justify=RIGHT, anchor="e")
label.grid(row=0, columnspan=5)

# Setting buttons
buttons = []
row = 0
column = 0
# Buttons 1 - 9
for i in range(1, 10):
    if i < 4:
        column = i
        row = 3
    elif i < 7:
        column = i - 3
        row = 2
    elif i < 10:
        column = i - 6
        row = 1
    new_button = Button(screen, text=i, width=6, height=4, command=lambda i=i: press_num(str(i)))
    new_button.grid(column=column, row=row)


# Buttons for operators
operators = ["/", "X", "-", "+"]
for i in range(0, len(operators)):
    new_operator = Button(text=operators[i], width=6, height=4, command=lambda i=i: press_operator(operators[i]))
    new_operator.grid(column=4, row=i + 1)


# Buttons on last row
last_row = ["C", "0", ".", "="]
for i in range(len(last_row)):
    new_button = Button(text=last_row[i], width=6, height=4)
    new_button.grid(row=4, column=i)
    buttons.append(new_button)
buttons[0].config(command=lambda: clear())
buttons[1].config(command=lambda: press_num("0"))
buttons[2].config(command=lambda: press_num("."))
buttons[3].config(command=lambda: equal())

# Buttons on the left column
button_off = Button(text="OFF", width=6, height=4, command=screen.destroy)
button_off.grid(column=0, row=1)
button_perc = Button(text="exp", width=6, height=4, command=lambda: press_operator("exp"))
button_perc.grid(column=0, row=3)
button_perc = Button(text="%", width=6, height=4, command=lambda: press_operator("%"))
button_perc.grid(column=0, row=2)

screen.mainloop()
