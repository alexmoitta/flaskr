#!/usr/bin/python
from numpy import array


#task: number of comparisons



def partition(array_numbers,pivot,r, number_comparisons):
#falta colocar o caso base de um elemento ainda e a recursao
#   r = len(array_numbers)
    i = pivot + 1
    if (r - i) < 1:
        return pivot #nao vai fazer nada com isso
    else:
        number_comparisons += r - pivot -1 # se vai ter comparacao, ja incrementa
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

    #essa partition e so para tratar os elementos que eram menores que o pivot
    #nao deve fazer diferenca na estrutura ou iteracao principal
    i_new = partition(array_numbers,pivot,i-1,number_comparisons)
    print array_numbers
    if i_new < i:
        return i
    else:
        return i_new
#    if (r - i <= 2 ): #condicao de parada ruim
#    return number_comparisons
#    else:
#    number_comparisons += partition(array_numbers,i,r,number_comparisons) #chamada para a direita


def quicksort_by_me(array_numbers,number_comparisons):
    total_size = len(array_num_input)
    start_pivot = 0
    while start_pivot < total_size-1:
        start_pivot = partition(array_num_input,start_pivot,total_size,number_comparisons)
#    print "quantidade de inversoes: " + str(r)


workdirectory = "./workdir"
name_of_file = "testePequeno.txt"
#name_of_file = "_32387ba40b36359a38625cbb397eee65_QuickSort.txt"
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

number_comparisons = 0
quicksort_by_me(array_num_input,number_comparisons)

file_pointer = open(outputnameofile,mode='w')


size_of_file = len(array_num_input)
for x in range(0,size_of_file,1):
    file_pointer.write(str(array_num_input[x]) + '\n')

file_pointer.close()

print "Output was generated"