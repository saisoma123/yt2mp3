#Deletes any file ending with mp4
import os
z = ""
dir_path = os.path.dirname(os.path.realpath(__file__)) 
for root, dirs, files in os.walk(dir_path): 
    for file in files:  
        if file.endswith('.mp4'): 
            z = str(file)
os.remove(z)