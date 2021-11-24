#! /usr/bin/python3
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter
import webbrowser



#create main window

root = tkinter.Tk()

screen_width = int(root.winfo_screenwidth())
screen_height = int(root.winfo_screenheight())

root.title('Techst Editor')

root.geometry("+-8+0")
root.maxsize(screen_width, screen_height-80)
root.minsize(screen_width, screen_height-80)
root.config(bg = "#2596be")


#make text input box

text = Text(root)
text.place(height=screen_height-175, width=screen_width-40, x=20, y=55)

#create icon and menu bar

menu_bar = Canvas(root)  
menu_bar.place(x=205, y=0, height=20, width=screen_width-205)


def file():
    save_btn = Button(root, text = 'Save', font=("Default", 10), borderwidth="0", command = lambda : [save()])
    open_btn = Button(root, text ='Open', font=("Default", 10), borderwidth="0", command = lambda : [open_file(text)])
    save_btn.place(x=0, y=20, height=30, width=45)
    open_btn.place(x=0, y=50, height=30, width=45)
    file_btn.place_forget()
    file_redo_btn = Button(root, text="File", font=("Default", 10), borderwidth="0", command = lambda: [file_btn.place(x=0, y=0, height=20, width=45), file_redo_btn.place_forget(), save_btn.place_forget(), open_btn.place_forget()])
    file_redo_btn.place(x=0, y=0, height=20, width=45)

def settings():
    credits_btn = Button(root, text="Credits", font=("Default", 10), borderwidth="0", command = lambda : [credits()])
    credits_btn.place(x=45, y=20, height=30, width=75)
    dark_mode_btn = Button(root, text="Dark Mode", font=("Default", 10), borderwidth="0", command = lambda : [dark_mode_run()])
    dark_mode_btn.place(x=45, y=50, height=30, width=75)
    light_mode_btn = Button(root, text="Light Mode", font=("Default", 10), borderwidth="0", command = lambda : [light_mode_run()])
    light_mode_btn.place(x=45, y=80, height=30, width=75)
    settings_btn.place_forget()
    settings_redo_btn = Button(root, text="Settings", font=("Default", 10), borderwidth="0", command = lambda : [settings_btn.place(x=45, y=0, height=20, width=75), credits_btn.place_forget(), dark_mode_btn.place_forget(), light_mode_btn.place_forget(), settings_redo_btn.place_forget()])
    settings_redo_btn.place(x=45, y=0, height=20, width=75)
    def dark_mode_run():
        root.config(bg="black")
        text.config(bg="black", foreground="white", insertbackground="white")
        zoom_in_btn.config(bg="black", foreground="white")
        zoom_out_btn.config(bg="black", foreground="white")
        normal_size_btn.config(bg="black", foreground="white")
    def light_mode_run():
        root.config(bg="#2596be")
        text.config(bg="white", foreground="black", insertbackground="black")
        zoom_in_btn.config(bg="white", foreground="black")
        zoom_out_btn.config(bg="white", foreground="black")
        normal_size_btn.config(bg="white", foreground="black")

def tools():
    word_search_btn = Button(root, text = "Word Search", borderwidth="0", font=("Default", 10), command = lambda : [word_search()])
    word_search_btn.place(x=120, y=20, height=30, width=85)
    find_btn = Button(root, text="Find", borderwidth="0", font=("Default", 10), command = lambda : [find(text)])
    find_btn.place(x=120, y=50, height=30, width=85)
    tools_btn.place_forget()
    tools_redo_btn = Button(root, text="Tools", font=("Default", 10), borderwidth="0", command = lambda : [tools_btn.place(x=120, y=0, height=20, width=85), word_search_btn.place_forget(), find_btn.place_forget(), tools_redo_btn.place_forget()])
    tools_redo_btn.place(x=120, y=0, height=20, width=85)

file_btn = Button(root, text="File", font=("Default",  10), borderwidth="0", command = lambda : [file()])
settings_btn = Button(root, text="Settings", font=("Default", 10), borderwidth="0", command = lambda : [settings()])
tools_btn = Button(root, text="Tools", font=("Default", 10), borderwidth="0", command = lambda : [tools()])
file_btn.place(x=0, y=0, height=20, width=45)
settings_btn.place(x=45, y=0, height=20, width=75)
tools_btn.place(x=120, y=0, height=20, width=85)

#copy paste cut function

def make_menu(w):
    global the_menu
    the_menu = tkinter.Menu(w, tearoff=0)
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")

def show_menu(e):
    w = e.widget
    the_menu.entryconfigure("Cut",
    command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Copy",
    command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Paste",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)

make_menu(root)

text.bind_class("Text", "<Button-3><ButtonRelease-3>", show_menu)

#save function

def save():
    files = [('All Files', '*.*'), ('Python Files', '*.py'), ('Txt Files', '*.txt')]
    file = fd.asksaveasfile(filetypes = files, defaultextension = files)
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()


#open function

def open_file(text):
    file = fd.askopenfile(mode ='r', filetypes =[('All Files', '*.*'), ('Python Files', '*.py'), ('Txt Files', '*.txt')])
    content = file.read()
    text.insert(END, content)



#zoom in and out function and button

size = 15
text.config(font=("Courier", size))
def normal_size(size):
    text.config(font=("Courier", size))

def zoom_in():
    text.config(font=("Courier", 20))

def zoom_out():
    text.config(font=("Courier", 10))

zoom_in_btn = Button(root, text = "+", bg="white", font=("Default", 18), command = lambda : [zoom_in()])
zoom_out_btn = Button(root, text = "-", bg="white", font=("Default", 18), command = lambda : [zoom_out()])
normal_size_btn = Button(root, text = "normal", bg="white", command = lambda : [normal_size(size)])

zoom_in_btn.place(x=screen_width-30, y=screen_height-115, height=20, width=20)
zoom_out_btn.place(x=screen_width-110, y=screen_height-115, height=20, width=20)
normal_size_btn.place(x=screen_width-90, y=screen_height-115, height=20, width=60)

#credits function

def credits():
    root = tkinter.Tk()
    root.title('Techst Editor Credits')
    root.geometry("350x150+500+300")
    root.maxsize(350, 150)
    root.minsize(350, 150)
    root.config(bg="white")
    l1 = Label(root, text = "Techst Editor", font=("Default", 15), bg="white")
    l2 = Label(root, text = "Developer: BeetJuice101", font=("Default", 15), bg="white")
    l3 = Label(root, text = "Programming Language: Python", font=("Default", 15), bg="white")
    l1.pack()
    l2.pack()
    l3.pack()
    url = "https://github.com/BeetJuice101/Techst-Editor"
    def openwebsite():
        webbrowser.open(url,new=1)
    GitHub_btn = Button(root, text="GitHub Page", padx=25, borderwidth="0", bg="#2596be", command = lambda : [openwebsite()])
    GitHub_btn.place(x=125, y=100, width=100)


#word search function and button

def word_search():
    root = tkinter.Tk()
    root.title('Techst Editor Word Search')
    root.geometry("350x150+500+300")
    root.maxsize(350, 150)
    root.minsize(350, 150)
    root.config(bg="white")
    search = Label(root, text = "Online Speelcheck", font=("Default", 15), bg="white")
    search.pack()
    url = "https://www.reverso.net/spell-checker/english-spelling-grammar/"
    def openwebsite():
        webbrowser.open(url,new=1)
    Wordweb_btn = Button(root, text="Reverso", font=("Default", 15), borderwidth="0", bg="#2596be", command = lambda : [openwebsite()])
    Wordweb_btn.place(x=125, y=80, width=100)


#Find text function

def find(text):
    root = tkinter.Tk()
    root.title('Techst Editor Find Word')
    root.geometry("400x200+500+300")
    root.maxsize(400, 200)
    root.minsize(400, 200)
    root.config(bg="white")
    words = str(text.get(1.0, END))
    words = list(words.split(" "))
    info = Label(root, text="Find A Word In Text", font=("Default", 15), bg="white")
    info.pack()
    word_entry = Entry(root, width=20)
    word_entry.pack()
    word_get_btn = Button(root, text="CHECK", command = lambda : [word_get(words)])
    word_get_btn.place(x=150, y=125, width=100)
    def word_get(words):
        find_word = str(word_entry.get())
        for words in words:
            found = False
            if words == find_word:
                answer = Label(root, text="Found", font=("Default", 15), bg="white")
                answer.pack()
                found = True
            if found is True:
                break
        
def techst_api(background_color, button_color, font_color):
    if background_color == "Z":
        pass
    if background_color == "green":
        root.config(bg="green")
    if background_color == "blue":
        root.config(bg="blue")
    if background_color == "black":
        root.config(bg="black")
    if background_color == "white":
        root.config(bg="white")
    if background_color == "pink":
        root.config(bg="pink")
    if background_color == "red":
        root.config(bg="red")
    if background_color == "yellow":
        root.config(bg="yellow")
    if background_color == "purple":
        root.config(bg="purple")
    if background_color == "orange":
        root.config(bg="orange")
    if background_color == "brown":
        root.config(bg="brown")
    if background_color == "grey":
        root.config(bg="grey")
    if button_color == "Z":
        pass
    if button_color == "green":
        zoom_in_btn.configure(bg="green", foreground="white")
        zoom_out_btn.configure(bg="green", foreground="white")
        normal_size_btn.configure(bg="green", foreground="white")
    if button_color == "blue":
        zoom_in_btn.configure(bg="blue", foreground="white")
        zoom_out_btn.configure(bg="blue", foreground="white")
        normal_size_btn.configure(bg="blue", foreground="white")
    if button_color == "black":
        zoom_in_btn.configure(bg="black", foreground="white")
        zoom_out_btn.configure(bg="black", foreground="white")
        normal_size_btn.configure(bg="black", foreground="white")
    if button_color == "white":
        zoom_in_btn.configure(bg="white", foreground="black")
        zoom_out_btn.configure(bg="white", foreground="black")
        normal_size_btn.configure(bg="white", foreground="black")
    if button_color == "pink":
        zoom_in_btn.configure(bg="pink", foreground="white")
        zoom_out_btn.configure(bg="pink", foreground="white")
        normal_size_btn.configure(bg="pink", foreground="white")
    if button_color == "red":
        zoom_in_btn.configure(bg="red", foreground="white")
        zoom_out_btn.configure(bg="red", foreground="white")
        normal_size_btn.configure(bg="red", foreground="white")
    if button_color == "yellow":
        zoom_in_btn.configure(bg="yellow", foreground="black")
        zoom_out_btn.configure(bg="yellow", foreground="black")
        normal_size_btn.configure(bg="yellow", foreground="black")
    if button_color == "purple":
        zoom_in_btn.configure(bg="purple", foreground="white")
        zoom_out_btn.configure(bg="purple", foreground="white")
        normal_size_btn.configure(bg="purple", foreground="white")
    if button_color == "orange":
        zoom_in_btn.configure(bg="orange", foreground="black")
        zoom_out_btn.configure(bg="orange", foreground="black")
        normal_size_btn.configure(bg="orange", foreground="black")
    if button_color == "brown":
        zoom_in_btn.configure(bg="brown", foreground="white")
        zoom_out_btn.configure(bg="brown", foreground="white")
        normal_size_btn.configure(bg="brown", foreground="white")
    if button_color == "grey":
        zoom_in_btn.configure(bg="grey", foreground="black")
        zoom_out_btn.configure(bg="grey", foreground="black")
        normal_size_btn.configure(bg="grey", foreground="black")
    if font_color == "Z":
        pass
    if font_color == "green":
        text.config(fg="green")
    if font_color == "blue":
        text.config(fg="blue")
    if font_color == "black":
        text.config(fg="black")
    if font_color == "white":
        text.config(fg="white")
    if font_color == "pink":
        text.config(fg="pink")
    if font_color == "red":
        text.config(fg="red")
    if font_color == "yellow":
        text.config(fg="yellow")
    if font_color == "purple":
        text.config(fg="purple")
    if font_color == "orange":
        text.config(fg="orange")
    if font_color == "brown":
        text.config(fg="brown")
    if font_color == "grey":
        text.config(fg="grey")

root.mainloop()