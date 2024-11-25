import tkinter as tk
from tkinter import ttk
from images import *
from tkinter.messagebox import showinfo


root = tk.Tk()
root.title('Questionnaire')
window_width = 1000
window_height = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

root.iconbitmap('images/icone.ico')

# menu déroulant
#1
label = ttk.Label(text="Entrez votre nom :")
label.place(x=20, y=20)
signin = ttk.Frame(root)
selected_name = tk.StringVar()
name_entry = ttk.Entry(signin, textvariable=selected_name)
name_entry.focus()


name_entry.place(x=120, y=20)

#2
label = ttk.Label(text="Entrez votre âge :")
label.place(x=20, y=70)

selected_age = tk.StringVar()
age_cb = ttk.Combobox(root, textvariable=selected_age)

age_cb['values'] = ["14","15","16","17","18", "42"]
age_cb['state'] = 'readonly'

age_cb.place(x=120, y=70)

root.mainloop()


