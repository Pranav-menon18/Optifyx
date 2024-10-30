import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import random
import string
import pyperclip 


def on_move_gen(e):
    button_generate.config(bg='#007ACC')

def on_leave_gen(e):
    button_generate.config(bg='#005A99')

def on_move_copy(e):
    button_copy.config(bg='#FFD700')

def on_leave_copy(e):
    button_copy.config(bg='#B8860B')

def check_for_length():
    try:
        length = int(entry_length.get())
        if(length < 4):
            messagebox.showwarning("Warning", "Password must be at least 4 characters long.")
        elif (length > 32):
            messagebox.showwarning("Warning", "Length should be 32 or less.")
        else:
            return length

    except Exception as e:
        messagebox.showerror("Error", "Please enter a valid number!")
    return 0

def generate_password():
    length = check_for_length()
    has_upper = var_uppercase.get()
    has_lower = var_lowercase.get()
    has_digit = var_digits.get()
    has_special = var_special.get()
    buffer = ''

    if has_upper:
        buffer += string.ascii_uppercase
    if has_lower:
        buffer += string.ascii_lowercase
    if has_digit:
        buffer += string.digits
    if has_special:
        buffer += string.punctuation
    if not buffer:
        messagebox.showwarning("Warning", "At least one character type must be selected")
        password = ''

    else:       
        password = '' if not length else ''.join([random.choice(buffer) for _ in range(length)])
        if password:
            if has_upper:
                password = random.choice(string.ascii_uppercase) + password[1:]
            if has_lower:
                password = password[0] + random.choice(string.ascii_lowercase) + password[2:]
            if has_digit:
                password = password[0:2] + random.choice(string.digits) + password[3:]
            if has_special:
                password = password[0:3] + random.choice(string.punctuation) + password[4:] if (length > 4) else  password[0:3] + random.choice(string.punctuation) 
     
            shuffle_pass = list(password)
            random.shuffle(shuffle_pass)
            password = ''.join(shuffle_pass)   
    result_entry.config(state=tk.NORMAL)
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)
    result_entry.config(state=tk.DISABLED)

def copy_password():
    password = result_entry.get()
    if password:
        pyperclip.copy(password)
        

app = tk.Tk()
app.title("Random Password Generator GUI")
app.geometry("400x400+350+40")
app.configure(bg='#1E1E1E')
app.resizable(False, False)
app.iconbitmap('assets/key.ico')


checkbox_font = ('Arial', 9,  'bold')
label_title_font = ('Helvetica', 18, 'bold')
length_font = ('Arial', 12)
button_font = ('Arial', 11, 'bold')


label_title = tk.Label(app, text="Password Generator", font=label_title_font, bg='#1E1E1E', fg='#00FF00')
label_title.pack(pady=20)


label_length = tk.Label(app, text="Enter password length", font=length_font, bg='#1E1E1E', fg='#43f043')
label_length.pack()


entry_length = tk.Entry(app, font=length_font, justify='center', insertbackground="white", width=10, bg='#2A2A2A', fg='#FFFFFF')
entry_length.pack(pady=10)
entry_length.focus_set()


var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_special = tk.BooleanVar()

check_uppercase = tk.Checkbutton(app, text="Include Uppercase", font=checkbox_font, variable=var_uppercase, bg='#1E1E1E', fg='#43f043', selectcolor='#2A2A2A')
check_uppercase.pack(padx=5, anchor='w')

check_lowercase = tk.Checkbutton(app, text="Include Lowercase", font=checkbox_font, variable=var_lowercase, bg='#1E1E1E', fg='#43f043', selectcolor='#2A2A2A')
check_lowercase.pack(padx=5, anchor='w')

check_digits = tk.Checkbutton(app, text="Include Digits", font=checkbox_font, variable=var_digits, bg='#1E1E1E', fg='#43f043', selectcolor='#2A2A2A')
check_digits.pack(padx=5, anchor='w')

check_special = tk.Checkbutton(app, text="Include Special Characters", font=checkbox_font, variable=var_special, bg='#1E1E1E', fg='#43f043', selectcolor='#2A2A2A')
check_special.pack(padx=5, anchor='w')


button_generate = tk.Button(app, text="Generate Password", command=generate_password, width=17, borderwidth=2, highlightbackground='#003F5C', font=button_font, bg='#005A99', fg='#FFFFFF', relief='raised' )
button_generate.place(x=25, y=270)
button_generate.bind("<Enter>", on_move_gen)
button_generate.bind("<Leave>", on_leave_gen)


button_copy = tk.Button(app, text="Copy Password", command=copy_password, width=17, borderwidth=2, highlightbackground='#8B5A2B', font=button_font, bg='#B8860B', fg='#191c19', relief='raised')
button_copy.place(x=215, y=270)
button_copy.bind("<Enter>", on_move_copy)
button_copy.bind("<Leave>", on_leave_copy)


label_result = tk.Label(app, text="G e n e r a t e d   P a s s w o r d", font=button_font, justify='center', bg='#1E1E1E', fg='#43f043')
label_result.place(x=85, y=330)

result_entry = tk.Entry(app,  font=length_font, width=32,  justify='center', disabledbackground='#2A2A2A', disabledforeground='#00FFFF', state='disabled')
result_entry.place(x=53, y=360)


app.mainloop()
