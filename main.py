import webbrowser

import tkinterdnd2
from functions import *

global my_notebook
global root
global event
from sys import exit
import sv_ttk
import requests

# Open to see functions I used
def UInt32(f):
    intvar = (struct.unpack("<I", f.read(4))[0])
    return intvar


def Int32(f):
    intvar = (struct.unpack("<i", f.read(4))[0])
    return intvar


def UInt16(f):
    intvar = (struct.unpack("<H", f.read(2))[0])
    return intvar


def Int16(f):
    intvar = (struct.unpack("<h", f.read(2))[0])
    return intvar


def Float(f):
    intvar = (struct.unpack("<f", f.read(4))[0])
    return intvar


def UInt64(f):
    intvar = (struct.unpack("<L", f.read(8))[0])
    return intvar


def Int64(f):
    intvar = (struct.unpack("<l", f.read(8))[0])
    return intvar


def Byte(f):
    intvar = (struct.unpack("<B", f.read(2))[0])
    return intvar


def advance(f, a=1):
    f.seek(f.tell() + a)


def back(f, a=1):
    f.seek(f.tell() - a)


def newline(n=1):
    for x in range(n):
        print()


# if sys.argv[1] is None:
#     print(
#         "You didn't open this program with a file, either drag a .model onto the program to drag it as your arg in cmd")
#     input("Press Enter to close...")
#     sys.exit()

def drop_Func(event):
    dragFile(my_notebook, root, event.data, True)


# customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# root = customtkinter.CTk()
root = tkinterdnd2.Tk()
root.title('Spiderman Asset Editor')
root.withdraw()

import ctypes as ct


def dark_title_bar(window):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))


dark_title_bar(root)
sv_ttk.set_theme("dark")

# root.iconbitmap('./smpceditoricon.ico')

style = ttk.Style()
style.layout("TNotebook", [])
style.configure("TNotebook", highlightbackground="#848a98", tabmargins=0)

my_notebook = ttk.Notebook(root, padding=0, style="TNotebook")
my_notebook.pack(fill=BOTH, expand=TRUE)
my_notebook.enable_traversal()

IFrame = Frame(width=1200, height=800, bd=0, highlightthickness=0, relief='ridge')
IFrame.drop_target_register(DND_FILES)
IFrame.dnd_bind('<<Drop>>', drop_Func)
IFrame.pack_propagate(False)
my_notebook.add(IFrame, text="Startup")

menubar = Menu(root, tearoff=0, background='black', fg='black')
#menubar = NewMenuBar(root)
root.config(menu=menubar, highlightcolor='black')

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File", command=lambda: dragFile(my_notebook, root, None, False))
file_menu.add_command(label="Save File", command=lambda: saveFile(my_notebook, root, True))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)


# edit_menu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Edit", menu=edit_menu)
# edit_menu.add_command(label="Cut", command=donothing)
# edit_menu.add_command(label="Copy", command=donothing)
# edit_menu.add_command(label="Paste", command=donothing)

def light_mode():
    sv_ttk.set_theme("light")


def dark_mode():
    sv_ttk.set_theme("dark")


view_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Light Mode (Warning, flashbang)", command=light_mode)
view_menu.add_command(label="Dark Mode", command=dark_mode)


help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Report a bug/Request a feature", command=lambda: webbrowser.open(url='https://github.com/bleedn/Spiderman-Asset-Editor/issues'))


# root.grid_rowconfigure(0, weight=1)
# root.grid_rowconfigure(1, weight=1)

undo = True
autoseparators = True
maxundo = -1


global programversion
programversion = 'Beta'
def verisoning():
    global programversion
    def checkversion():
        newestversion = 'https://raw.githubusercontent.com/bleedn/Spiderman-Asset-Editor/main/versioning/versioning.txt'
        req = requests.get(newestversion)
        req = req.text
        if not programversion == req:
            update = messagebox.askquestion(title='Update Available!',
                                            message='There is an update available for the SMPC Asset Editor! Would you like to go to the releases page?')
            if update == 'yes':
                webbrowser.open(url='https://github.com/bleedn/Spiderman-Asset-Editor/releases/latest',
                                new=0, autoraise=True)
            else:
                pass
        else:
            pass
    checkversion()
    status = Label(IFrame, text="Version " + str(programversion), bg="#000000", fg="#bec2cb").pack(fill=BOTH, side=BOTTOM)

verisoning()

Startup(IFrame)

def on_closing():
    if not len(my_notebook.tabs()) > 1:
        root.destroy()
        pass
        return
    savev = saveFile(my_notebook, root, False)
    if savev.bool == True:
        root.destroy()
        pass
    else:
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            root.destroy()
        else:
            pass


root.protocol("WM_DELETE_WINDOW", on_closing)
root.configure(bg="#000000")
root.deiconify()
root.mainloop()

# try:
#     file = sys.argv[1]
#     f = open(file, 'rb')
#
#
# input("Press Enter to close...")
# f.close()
# sys.exit()
