#!/usr/bin/python
from numpy import array


#task: number of comparisons



def partition(array_numbers,pivot,r):
#falta colocar o caso base de um elemento ainda e a recursao
#   r = len(array_numbers)
    i = pivot + 1
    if r - i <= 1:
        return
    tmp_swap = 0
    for j in range(pivot+1,r,1):
        if array_numbers[j] < array_numbers[pivot]:
            tmp_swap = array_numbers[i]
            array_numbers[i] = array_numbers[j]
            array_numbers[j] = tmp_swap
            i += 1
    tmp_swap = array_numbers[pivot]
    array_numbers[pivot] = array_numbers[i-1]
    array_numbers[i-1] = tmp_swap
    partition(array_numbers,i,r) #chamada para a direita
    partition(array_numbers,0,i-1) #chamada para a esquerda
    print array_numbers
    return









workdirectory = "./workdir"
name_of_file = "testePequeno.txt"
#nameoffile = "_32387ba40b36359a38625cbb397eee65_QuickSort.txt"
numbers_file = workdirectory + "/" + name_of_file
outputnameofile = workdirectory + "/" + "outputorderednumbers.txt"


file_pointer = open (numbers_file,mode='r')

print file_pointer

number_list = []

for line in file_pointer:
    if line != "\n":
        number_list.append(int(line))
        print line

file_pointer.close()

array_num_input = array(number_list, dtype = 'L')

print "File loading ended."

partition(array_num_input,0,len(array_num_input))

