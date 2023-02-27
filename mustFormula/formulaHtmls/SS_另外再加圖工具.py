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

if len(sys.argv) != 1:
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

new_file = open("rStemp.txt", "w")

fileNow = open("小柴胡湯.html", 'r')
listNow = fileNow.readlines()
fileNow.close()

for item in listNow:
    item = item.replace("</body></html>","<br><center><img src=\"小柴胡湯使用時機.png\" alt=\"xxx\" width=\"70%\" height=\"auto\" style=\"border:0px solid black;\"></center></body></html>")
    new_file.write(item)

cmd= "mv rStemp.txt 小柴胡湯.html"
os.system(cmd)
new_file.close()


#----------------- 桂枝湯

new_file = open("rStemp.txt", "w")

fileNow = open("桂枝湯.html", 'r')
listNow = fileNow.readlines()
fileNow.close()

for item in listNow:
    item = item.replace("</body></html>","<br><center><img src=\"桂枝湯家族譜系.png\" alt=\"xxx\" width=\"70%\" height=\"auto\" style=\"border:0px solid black;\"></center></body></html>")
    new_file.write(item)

cmd="mv rStemp.txt 桂枝湯.html"
os.system(cmd)
new_file.close()


#----------------- 小青龍湯

new_file = open("rStemp.txt", "w")

fileNow = open("小青龍湯.html", 'r')
listNow = fileNow.readlines()
fileNow.close()

for item in listNow:
    item = item.replace("</body></html>","<br><center><img src=\"小青龍湯類方.png\" alt=\"xxx\" width=\"70%\" height=\"auto\" style=\"border:0px solid black;\"></center></body></html>")
    new_file.write(item)

cmd="mv rStemp.txt 小青龍湯.html"
os.system(cmd)
new_file.close()


