import os
import shutil
downloads_path = "C:\\Users\\Frankie\\Downloads\\"

for filename in os.listdir(downloads_path):
    extension = os.path.splitext(filename)[1][1:]
    if extension == "":
        continue

    if not os.path.exists(downloads_path + extension):
        os.makedirs(downloads_path + extension)

    shutil.move(downloads_path + filename, downloads_path + extension + "\\" + filename)
