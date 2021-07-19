import os
import json
import shutil
import Encoding as Ec
from tkinter import Tk
from tkinter.filedialog import askopenfilename

if os.path.isfile("Train_Data/.DS_Store"):
    os.remove("Train_Data/.DS_Store")


choice = int(input("1. Add New Face\n2. ReTrain\nEnter Your Choice: "))

if choice == 1:
    Tk().withdraw()
    filename = askopenfilename()
    shutil.copy(filename, 'Train_Data')
    F = filename.split("/")
    F_ex = F[-1].split(".")
    os.rename("Train_Data/"+str(F[-1]), "Train_Data/"+str(input("Enter the Person Name: "))+"."+str(F_ex[-1]))

images, className = Ec.initiate()
eLK = Ec.UpdateEncoding(images)

update = {"name": className, "data": eLK}

with open("metadata.json", "w") as F1:
    json.dump(update, F1)