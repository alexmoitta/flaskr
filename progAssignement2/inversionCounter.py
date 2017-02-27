#!/usr/bin/python

#from array import array
from numpy import array
import orderLists

#from pylab import *

#high level algorithm
#Sort-and-Count (array A, length n)
#if n=1, return 0
#else
#    (B,X) = Sort-and-Count(1st half of A, n/2) (C,Y) = Sort-and-Count(2nd half of A, n/2) (D,Z) = CountSplitInv(A,n)
#return X+Y+Z
#Goal : implement CountSplitInv in linear (O(n)) .me
#=> then Count will run in O(nlog(n)) .me [just like Merge Sort ]



## read file and put it on a list or vector, something indexed by intger
## split it in pairs analisysSize = 2
## order each pair when it is necessary
## multiply analysSize by 2
## merge again



## memory has alre
#def copyArray(origin,destiny):
#    tmpList = []





workdirectory = "/Users/alex/Dropbox/dev/python/src/progAssignement2"
nameoffile = "testePequeno"
#nameoffile = "_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt"
numbersfile = workdirectory + "/" + nameoffile
outputnameofile = workdirectory + "/" + "outputorderednumbers"


filepointer = open (numbersfile,mode='r')

print filepointer





numberlist = []




for line in filepointer:
    if  line != "\n":
        numberlist.append(int(line))
        print line

filepointer.close()


arraynumoutput = orderLists.orderlist(numberlist)





print "terminou a ordenacao"


print "gerando o arquivo de saida"

filepointer = open (outputnameofile,mode='w')

print filepointer

sizeOfFile = len(arraynumoutput)
for x in range(0,sizeOfFile,1):
    filepointer.write(str(arraynumoutput[x]) + '\n')


filepointer.close()


print "terminou de escrever o arquivo de saida"
