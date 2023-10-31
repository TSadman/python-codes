from PIL import Image
import os

print("img to pdf")
folder= input("folder: ")

imglist= list()
ImgList=os.listdir(folder)

for ii in ImgList:
    file=f"{folder}\\{ii}"
    im = Image.open(file)
    im1 = im.convert('RGB')
    imglist.append(im1)

name=folder+".pdf"

im1= imglist[0]
imglist.pop(0)

im1.save(name ,save_all=True, append_images=imglist)
