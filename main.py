import os
import shutil
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()
directory = filedialog.askdirectory(initialdir="C:\\")
if directory == "":
    quit()

result = messagebox.askquestion("File Organizer", directory + " will be organized. Continue?", icon="warning")

if result == "no":
    quit()

filelist = []
count = 0
for filename in os.listdir(directory):
    extension = os.path.splitext(filename)[1][1:]

    #ignore folders
    if os.path.isdir(directory + "/" + filename):
        continue
    #create a folder for each extension
    if not os.path.exists(directory + extension):
        os.makedirs(directory + extension)

    filelist.append([filename, directory + "/" + extension + "/" + filename])
    shutil.move(directory + "/" + filename, directory + "/" + extension + "/" + filename)
    count += 1

if count == 0:
    messagebox.showinfo("File Organizer", "No files were found in " + directory)
    quit()

okcancel = messagebox.askokcancel("File Organizer", str(count) + " files were moved. Press Cancel to undo these changes or OK to continue.")
if okcancel == False:
    for f in filelist:
        shutil.move(f[1], directory + "/" + f[0])
