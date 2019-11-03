import moviepy.editor as mp
import os
f = open('ytidentity.txt', 'r')
x = f.read()
y = 'python dlytvids.py ' + x
#os.system('cd Desktop')
#os.system('cd yt2mp3')
os.system(y)
z = ""
dir_path = os.path.dirname(os.path.realpath(__file__)) 
for root, dirs, files in os.walk(dir_path): 
    for file in files:  
        if file.endswith('.mp4'): 
            z = str(file)
clip = mp.VideoFileClip(z)
c = list(z)
c[len(c) - 1] = 3
newstring = ""
for q in range(0, len(c)):
    newstring += str(c[q])
clip.audio.write_audiofile(newstring)

