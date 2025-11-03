import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple UI Example")

# Create a label and button
label = tk.Label(root, text="Hello, Ivann!")
label.pack()

def on_click():
    label.config(text="You clicked the button!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

# Run the app
root.mainloop()
