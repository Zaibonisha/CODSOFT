import tkinter as tk

def on_button_click(value):
    current_text = result_var.get()
    if value == 'C':
        clear_result()
    elif value == '=':
        calculate_result()
    else:
        result_var.set(current_text + str(value))

def clear_result():
    result_var.set('')

def calculate_result():
    try:
        expression = result_var.get()
        result = eval(expression)
        result_var.set(result)
    except Exception as e:
        result_var.set('Error')

# Create the main window
window = tk.Tk()
window.title('Calculator')
window.geometry('400x500')  # Set a fixed window size
window.configure(bg='#f4f4f4')  # Set background color

# Create a StringVar to store the result
result_var = tk.StringVar()

# Entry widget to display the result
result_entry = tk.Entry(window, textvariable=result_var, font=('Helvetica', 18), justify='right', bd=10, bg='#ffffff', fg='#333333')
result_entry.grid(row=0, column=0, columnspan=4, sticky='nsew')  # Use sticky to expand the entry widget

# Define the button layout
button_layout = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 1, 4)  # span 4 columns for the equals button
]

# Create and place the buttons
for button_info in button_layout:
    text, row, col, *span = button_info
    button = tk.Button(window, text=text, padx=20, pady=20, font=('Helvetica', 14), command=lambda t=text: on_button_click(t), bd=5,
                       bg='#e0e0e0', fg='#333333')
    button.grid(row=row, column=col, rowspan=span[0] if span else 1, columnspan=span[1] if span else 1, sticky='nsew')

# Set row and column weights to make the entry and buttons expand proportionally
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Run the Tkinter event loop
window.mainloop()
