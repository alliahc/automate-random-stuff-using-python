import os, random
from os import path
from PIL import Image
import shutil

#enter source folder's and destination folder's absolute path
src_path="F:/Pictures"
dst_path="d:/Users/Administrator/Pictures/wallpaper-black"
valid_ext = [".jpg",".jpeg",".png"]
files_to_pick=2
count=0
while count < files_to_pick:
    image=random.choice(os.listdir(src_path))
    ext = os.path.splitext(image)[1]
    if ext.lower() in valid_ext:
        with Image.open(os.path.join(src_path,image)) as im:
            width, height = im.size
        if (not (os.path.exists(os.path.join(dst_path,image))) and width>=700 and height>=700):
            shutil.move(os.path.join(src_path,image), dst_path)
            count+=1