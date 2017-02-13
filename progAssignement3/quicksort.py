#!/usr/bin/python
from numpy import array

workdirectory = "./workdir"
nameoffile = "testePequeno"
#nameoffile = "_32387ba40b36359a38625cbb397eee65_QuickSort.txt"
numbersfile = workdirectory + "/" + nameoffile
outputnameofile = workdirectory + "/" + "outputorderednumbers.txt"


filepointer = open (numbersfile,mode='r')

print filepointer

number_list = []

for line in filepointer:
    if  line != "\n":
        number_list.append(int(line))
        print line

filepointer.close()

array_num_input = array(numberlist, dtype = 'L')