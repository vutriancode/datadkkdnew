from os import listdir
from os.path import isfile, join
import os
mypath = "C:/Users/vutri/OneDrive/Pictures/datadkkdnew/valid/labels"

mypath1 = "C:/Users/vutri/OneDrive/Pictures/datadkkdnew/valid/images"
onlyfiles = [f.split(".")[0] for f in listdir(mypath) if os.path.getsize(join(mypath, f))!=0]
print(len(onlyfiles))
for f in listdir(mypath1):
    if f.split(".")[0] not in onlyfiles:
        os.remove(join(mypath1, f))
for f in listdir(mypath):
    if f.split(".")[0] not in onlyfiles:
        os.remove(join(mypath, f))
           