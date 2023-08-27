# -*- coding:utf-8 -*-
#<!-- 1. 乾為天 乾.元.亨.利.貞. -->


#!/usr/bin/python

import sys
import os
import pickle
import re

#import TCM_allDBinOne

#===  class define ...

class argListOut:
 
   def __init__(self,argList):
     self.argList = argList
     self.argStr = ""


   def ListOut(self):
     for value in self.argList:
         self.argStr = self.argStr+" "+value
     print(self.argStr) 

#===  main program start ...

if len(sys.argv) != 2:
   print ("The line option is not assigned correctly : \n")
   print ("[usage] python3 "+sys.argv[0]+" [html檔] ")
   print ("[example] python3 "+sys.argv[0]+" 五苓散.html\n\n ")
   argList = (sys.argv) 
   argListOutInst = argListOut(argList)
   argListOutInst.ListOut()
   print ("EXIT ")
   exit()
else :
   argList = (sys.argv) 
   argListOutInst = argListOut(argList)
   argListOutInst.ListOut()

#=== Input File handling area ...

fileNow = open(argList[1], 'r')
listNow = fileNow.readlines()
fileNow.close()

#file2Now = open(argList[2], 'r')
#list2Now = file2Now.readlines()
#file2Now.close()

#=== Output File handling area ...

new_file = open("result.html", "w")

start = 0
#for i, item in enumerate(listNow):
for item in listNow:
    #print item.strip()
    regex0 = r"<body>"
    regex = r"<title>"
    regex2 = r"techTcmBrain\.png"
    regex3 = r"回首頁"    
    if (re.findall(regex0, item.strip())) and start==0 :
        new_file.write("<body><script src='header.js'></script>\n")
        start = 1
    elif (re.findall(regex, item.strip())):
        pass
    elif (re.findall(regex2, item.strip())):
        pass
    elif (re.findall(regex3, item.strip())):
        new_file.write("</tr>")
    else:
        new_file.write(item)
new_file.close()

