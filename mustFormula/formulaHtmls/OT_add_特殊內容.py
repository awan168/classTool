# -*- coding:utf-8 -*-
#<!-- 1. 乾為天 乾.元.亨.利.貞. -->


#!/usr/bin/python

import sys
import os
import pickle
import re

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
   print "The line option is not assigned correctly : \n"
   print "[usage] python "+sys.argv[0]+" [??] "
   print "[example] python "+sys.argv[0]+" ??\n\n "
   argList = (sys.argv) 
   argListOutInst = argListOut(argList)
   argListOutInst.ListOut()
   print "EXIT "
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

new_file = open("rStemp.txt", "w")

for item in listNow:
    #print item.strip()
    regex = r""
    regex2 = r""
    if (re.findall(regex, item.strip())):
        match = re.search(regex, item)
        #print match.group(1)
        new_file.write("%s  Wow%s -> Yoo%s %s\n" % (match.group(1), match.group(2), match.group(3), match.group(4)))
    elif (re.findall(regex2, item.strip())):
        match = re.search(regex2, item)
 
    else : 
        new_file.write(item)
new_file.close()

