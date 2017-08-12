import os

#for each folder in the directory open the folder, and see if it contains organizer.txt
for folder in os.listdir(path="C:\Users\Raymo\AppData\Roaming\.minecraft\resourcepacks"):
    print(folder)