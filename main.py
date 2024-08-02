from tkinter import *

# When press any button on the calculator, the operator or operating
# appear on the calculator screen
def button_press(num):
  global equation_text
  equation_text = equation_text + str(num)
  equation_label.set(equation_text)

# Define equals operating 
def equals():
  global equation_text
  try:
    total = str(eval(equation_text))
    equation_label.set(total)
    equation_text = total
  except SyntaxError:
    equation_label.set('syntax error')
    equation_text = ""
  except ZeroDivisionError:
    equation_label.set('arithmetic error')
    equation_text = ""

# Clear the calculator screen
def clear():
  global equation_text
  equation_label.set("")
  equation_text = ""

# Create a number button
def createButton(frame, text, row, col):
  button = Button(frame, text=text, height=4, width=9, font=35, command=lambda: button_press(text))
  button.grid(row=row, column=col)

# Creates all numbers buttons
def createNumberButtons(frame):
  for i in range(1, 10):
    row = (i - 1) // 3
    col = (i -1) % 3
    createButton(frame, str(i), row, col)

  createButton(frame, '0', 3, 0)

# Creates operators
def createOperatorButtons(frame, operators):
  for i, operator in enumerate(operators):
    createButton(frame, operator, i, 3)

  buttonDecimal = Button(frame, text='.', height=4, width=9, font=35, command=lambda: button_press('.'))
  buttonDecimal.grid(row=3, column=1)

  buttonEquals = Button(frame, text='=', height=4, width=9, font=35, command=equals)
  buttonEquals.grid(row=3, column=2)

window = Tk()
window.title("Calculator")
window.geometry("500x500")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

createNumberButtons(frame)
createOperatorButtons(frame, operators=['+', '-', '*', '/'])

buttonClear = Button(window, text='clear', height=4, width=9, font=35, command=clear)
buttonClear.pack()

window.mainloop()