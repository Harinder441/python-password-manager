# format the fillle enter comments
# ui of show passsword
# change to ninja pass

# Learnings
## use if else over try and except
from password_genorater import pass_generator
import pyperclip
from tkinter import messagebox
from tkinter import *
import json

PINK = "#F7CA9E"
RED = "#D4483B"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_password():
    password = pass_generator()
    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data ={website:{
        "email": email,
        "password": password
    }}
    if not website:
        messagebox.showerror(message="Please enter website name")
    elif not email:
        messagebox.showerror(message="Please enter email Id")
    elif not password:
        messagebox.showerror(message="Please enter password or generate one.")
    else:
        confirmation = messagebox.askquestion(message=f"Website: {website}\n"
                                                      f"Email: {email}\n"
                                                      f"Password: {password}\n"
                                                      f"_____Is this ok?_______",
                                              )
        if confirmation != "yes":
            return
        else:
            try:
                with open("passwords.json", mode="r") as file:
                    data=json.load(file)
            except FileNotFoundError:
                with open("passwords.json", mode="w") as file:
                    json.dump(new_data,file,indent=4)
            else:
                data.update(new_data)
                # file.write(f"{website},{email},{password}\n")
                with open("passwords.json", mode="w") as file:
                    json.dump(data,file,indent=4)
            finally:
                reset()

def search():
    try:
        with open("passwords.json", mode="r") as file:
            data=json.load(file)
            website = website_entry.get()
            web_data= data[website]

    except FileNotFoundError:
        messagebox.showinfo(message="You have not saved any password")
    except KeyError as key:
        messagebox.showerror(message=f"{key} not found")
    else:
        messagebox.showinfo(message=f"Email:  {web_data['email']}\n"
                                    f"Password: {web_data['password']}",title=website)

def reset():
    website_entry.delete(0, END)
    password_entry.delete(0, END)

def show_passwords():
    top= Toplevel(window)
    top.geometry("750x250")
    top.title("Saved passwords")
    with open("passwords.json", mode="r") as file:
            data=json.load(file)

    Label(top,text=f"S.No, Website,  email, passwords").grid(row=0,sticky=W)

    for i in range(len(data)):
        Label(top,text=f"{i+1}, {list(data.keys())[i]}, {list(data.values())[i]['email']}, {list(data.values())[i]['password']}").grid(row=i+1,sticky=W)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

ENTRY_GRID_OPT = {"pady": 3}
ENTRY_OPT = {}


# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(bg=YELLOW, height=200, width=189, highlightthickness=0)
canvas_bg = PhotoImage(file="logo.png")
canvas.create_image(95, 100, image=canvas_bg)
canvas.grid(row=0, column=1)
website_label = Label(text="Website", font=(FONT_NAME, 16, "bold"), fg=RED, bg=YELLOW)
website_label.grid(row=1, column=0)
website_entry = Entry(font=(FONT_NAME, 14, "normal"), fg=RED, bg="white", width=20, **ENTRY_OPT)
website_entry.grid( row=1, column=1, **ENTRY_GRID_OPT)
website_search_button= Button(text="Search", font=(FONT_NAME, 12, "bold"), fg=RED, bg=PINK,
                         borderwidth=0, activebackground=YELLOW, activeforeground=RED
                         , command=search, width= 9)
website_search_button.grid(row=1, column=2)

email_label = Label(text="Email", font=(FONT_NAME, 16, "bold"), fg=RED, bg=YELLOW)
email_label.grid(row=2, column=0)
email_entry = Entry(font=(FONT_NAME, 14, "normal"), fg=RED, bg="white", width=30, **ENTRY_OPT)
email_entry.grid(columnspan=2, row=2, column=1, **ENTRY_GRID_OPT)
email_entry.insert(END, "xyz@abc.com")
password_label = Label(text="Password", font=(FONT_NAME, 16, "bold"), fg=RED, bg=YELLOW)
password_label.grid(row=3, column=0)
password_entry = Entry(font=(FONT_NAME, 14, "normal"), fg=RED, bg="white", width=20, **ENTRY_OPT)
password_entry.grid(row=3, column=1, **ENTRY_GRID_OPT)
password_button = Button(text="Generate", font=(FONT_NAME, 12, "bold"), fg=RED, bg=PINK,
                         borderwidth=0, activebackground=YELLOW, activeforeground=RED
                         , command=get_password)
password_button.grid(row=3, column=2)

blank_line = Label(font=(FONT_NAME, 16, "bold"), bg=YELLOW)
blank_line.grid(row=4, column=0, columnspan=3)
save_button = Button(text="Add Password", font=(FONT_NAME, 16, "bold"), fg=RED, bg=PINK,
                     borderwidth=0, activebackground=YELLOW, activeforeground=RED
                     , command=save, pady=3, padx=6)
save_button.grid(row=5, column=1)
or_label = Label( font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg =RED)
or_label.grid(row=6, column=1 ,pady= 5)

show_password_button = Button(text="Show all passwords", font=(FONT_NAME, 16, "bold"), fg=RED, bg=PINK,
                     borderwidth=0, activebackground=YELLOW, activeforeground=RED
                     , command= show_passwords, pady=3, padx=6)
show_password_button.grid(row=7, column=1)

window.mainloop()
