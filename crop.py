from PIL import Image
import os

print("shrink image")
folder= input("folder: ")
wtop = 106
htop = 175
wdown = 848
hdown = 647
for ii in os.listdir(folder):
    file=f"{folder}\\{ii}"
    im = Image.open(file)
    im=im.crop((wtop,htop,wdown,hdown))
    im.save(file)
