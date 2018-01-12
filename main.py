import os
import shutil
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()
directory = filedialog.askdirectory(initialdir="C:\\")
result = messagebox.askquestion("File Organizer", "The directory " + directory + " will be organized. Continue?", icon="warning")

if result == "yes":
    for filename in os.listdir(directory):
        extension = os.path.splitext(filename)[1][1:]

        #ignore folders
        if os.path.isdir(directory + "/" + filename):
            continue
        #create a folder for each extension
        if not os.path.exists(directory + extension):
            os.makedirs(directory + extension)

        shutil.move(directory + "/" + filename, directory + "/" + extension + "/" + filename)
