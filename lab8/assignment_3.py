
import os
import json
import shutil
import random


#find data.json


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")) as data_file:


   data = json.loads(data_file.read())

class Info:


   def __init__(self, type_, extension, mime):


       self.type = type_


       self.extension = extension


       self.mime = mime

def get(obj):


   if not isinstance(obj, bytes):


       raise TypeError("error")


   info = {


       "type": dict(),


       "extension": dict(),


       "mime": dict()  }


   stream = " ".join(['{:02X}'.format(byte) for byte in obj])


   for element in data:


       for signature in element["signature"]:


           offset = element["offset"] * 2 + element["offset"]


           if signature == stream[offset:len(signature) + offset]:


               for key in ["type", "extension", "mime"]:


                   info[key][element[key]] = len(signature)


                  


   for key in ["type", "extension", "mime"]:


       info[key] = [element for element in sorted(info[key], key=info[key].get, reverse=True)]


   return Info(info["type"], info["extension"], info["mime"])








merve = list()


current_directory_2 = os.getcwd()


for file in os.listdir(current_directory_2):


   with open(file, "rb") as file2:


       m = get(file2.read(128))


   if (m.extension == []):


       merve.append("['ASCI txt']")


   else:


       merve.append(sy.extension)


   if (m.extension == []):


       print(file, "['ASCI txt']")


   else:


       print(file, m.extension)







def unique(list1):


   unique_list = []


   for m in list1:


       if m not in unique_list:


           unique_list.append(m)


   print (len(unique_list))


unique(merve)


