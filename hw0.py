import os.path,time
from pathlib import Path
from datetime import datetime

home = str(Path.home())


os.chdir(home)
os.mkdir('os_lab_0')
os.chdir('os_lab_0')

fdir=open("merve1.txt","w+")
fdir=open("merve2.txt","w+")
fdir=open("python.py","w+")
f.close()


for root,dirs,files in os.walk("."):
	for filename in files:
		print(filename,  time.ctime(os.path.getmtime(filename))) 



for file in os.listdir("."):
	if file.endswith(".txt"):
		print (os.path.join("os_lab_0",file))
