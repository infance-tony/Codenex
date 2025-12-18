import tkinter as tk
from tkinter import ttk, messagebox
import time

# Tk() - Create main window
root = tk.Tk()
root.title("Tkinter Components Examples")
root.geometry("800x600")

# mainloop() - Will be called at the end

# Label
label = tk.Label(root, text="This is a Label", font=("Arial", 12))
label.pack(pady=10)

# Button
def button_click():
    messagebox.showinfo("Button", "Button clicked!")

button = tk.Button(root, text="Click Me", command=button_click)
button.pack(pady=10)

# Entry
entry = tk.Entry(root)
entry.pack(pady=10)
entry.insert(0, "Enter text here")

# CheckButton
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Check me", variable=check_var)
checkbutton.pack(pady=10)

# RadioButton
radio_var = tk.IntVar()
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value=1)
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value=2)
radio1.pack()
radio2.pack()

# Listbox
listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.pack(pady=10)

# Scrollbar (with Listbox)
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Menu
menubar = tk.Menu(root)
root.config(menu=menubar)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Exit", command=root.quit)

# Combobox
combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo.set("Select")
combo.pack(pady=10)

# Scale
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack(pady=10)

# TopLevel
def open_toplevel():
    top = tk.Toplevel(root)
    top.title("TopLevel Window")
    tk.Label(top, text="This is a TopLevel window").pack()

top_button = tk.Button(root, text="Open TopLevel", command=open_toplevel)
top_button.pack(pady=10)

# Message
message = tk.Message(root, text="This is a Message widget with word wrapping.", width=200)
message.pack(pady=10)

# MenuButton
menubutton = tk.Menubutton(root, text="MenuButton")
menubutton.menu = tk.Menu(menubutton, tearoff=0)
menubutton["menu"] = menubutton.menu
menubutton.menu.add_command(label="Item 1")
menubutton.pack(pady=10)

# Progressbar
progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=10)

def start_progress():
    for i in range(101):
        time.sleep(0.01)
        progress['value'] = i
        root.update_idletasks()

progress_button = tk.Button(root, text="Start Progress", command=start_progress)
progress_button.pack(pady=10)

# SpinBox
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack(pady=10)

# Text
text = tk.Text(root, height=5, width=30)
text.insert(tk.END, "This is a Text widget.\nMulti-line text.")
text.pack(pady=10)

# Canvas
canvas = tk.Canvas(root, width=200, height=100, bg="white")
canvas.create_line(0, 50, 200, 50)
canvas.pack(pady=10)

# PannedWindow
paned = tk.PanedWindow(root, orient=tk.HORIZONTAL)
paned.pack(fill=tk.BOTH, expand=1)
frame1 = tk.Frame(paned, bg="red", width=100)
frame2 = tk.Frame(paned, bg="blue", width=100)
paned.add(frame1)
paned.add(frame2)

# Color Option in Tkinter (demonstrated on a label)
color_label = tk.Label(root, text="Colored Label", bg="lightblue", fg="red")
color_label.pack(pady=10)

# Tkinter Font (demonstrated on a label)
from tkinter import font
custom_font = font.Font(family="Helvetica", size=14, weight="bold")
font_label = tk.Label(root, text="Custom Font Label", font=custom_font)
font_label.pack(pady=10)

# pack() method (already used above)

# grid() method - Use a frame to avoid mixing geometry managers
grid_frame = tk.Frame(root)
grid_frame.pack(pady=10)
grid_label1 = tk.Label(grid_frame, text="Grid 1")
grid_label2 = tk.Label(grid_frame, text="Grid 2")
grid_label1.grid(row=0, column=0)
grid_label2.grid(row=0, column=1)

# place() method
place_label = tk.Label(root, text="Placed Label")
place_label.place(x=400, y=200)

# Event Handling in Tkinter
def on_key_press(event):
    print(f"Key pressed: {event.char}")

root.bind("<Key>", on_key_press)

# Events and Bindings (already demonstrated with bind)

# Key and Mouse Events
def on_mouse_click(event):
    print(f"Mouse clicked at {event.x}, {event.y}")

root.bind("<Button-1>", on_mouse_click)

# mainloop()
root.mainloop()