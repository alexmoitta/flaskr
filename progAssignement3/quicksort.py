#!/usr/bin/python
from numpy import array
import ComparisonCounter

#task: number of comparisons



def partition(array_numbers,pivot,r, number_comparisons):
    i = pivot + 1
    if (r-pivot-1) >= 1: #so incrementa se fizer sentido
        number_comparisons.add_value(r - pivot -1) # se vai ter comparacao, ja incrementa
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

    print array_numbers
    return i




def quicksort_by_the_book(array_num_input, p, r, number_comparisons):
    if p < r:
        q = partition(array_num_input,p,r,number_comparisons)
        quicksort_by_the_book(array_num_input,p,q-1,number_comparisons)
        quicksort_by_the_book(array_num_input,q,r,number_comparisons)
#    quicksort_by_the_book(array_num_input,q+1,r,number_comparisons)


def swap_first_last(array_numbers,p,r):
    tmp_swap = array_numbers[r-1]
    array_numbers[r-1] = array_numbers[p]
    array_numbers[p] = tmp_swap

def quicksort_by_the_book_last(array_num_input_last, p, r, number_comparisons_last):
    if p < r:
        swap_first_last(array_num_input_last,p,r)
        q = partition(array_num_input_last,p,r,number_comparisons_last)

#        swap_first_last(array_numbers,p,q-1)
        quicksort_by_the_book_last(array_num_input_last,p,q-1,number_comparisons_last)

#        swap_first_last(array_numbers,q,r)
        quicksort_by_the_book_last(array_num_input_last,q,r,number_comparisons_last)


# se vier impar, p ex 5, 5 / 2 = 2 de 0th, 1th, 2th, 3th, 4th
# se vier par, p ex 4, 4 / 2 = 2 ele pede que seja o 1th e nao 2th
def swap_first_median(array_num_input_median,p,r):
    if (r - p) % 2 == 0: #nro elementos pares
#        pos_first_median = (r-1-p)/2
        pos_first_median = (r-1-p)/2+p
        first_median = array_num_input_median[pos_first_median]
    else:
#        pos_first_median = (r-p)/2
        pos_first_median = (r-p)/2+p
        first_median = array_num_input_median[pos_first_median]

    #median selecionado para comparar com o ultimo e o primeiro
    first_element = array_num_input_median[p]
    last_element = array_num_input_median[r-1]

    if first_median <= last_element:
        if first_median >= first_element:
            real_median = first_median
            #iniciando o swap com o primeiro elemento
            tmp_swap = array_num_input_median[p]
            array_num_input_median[p] = real_median
            array_num_input_median[pos_first_median] = tmp_swap
            return
    if first_median >= last_element:
        if first_median <= first_element:
            real_median = first_median
            #iniciando o swap com o primeiro elemento
            tmp_swap = array_num_input_median[p]
            array_num_input_median[p] = real_median
            array_num_input_median[pos_first_median] = tmp_swap
            return

    if last_element <= first_median:
        if last_element >= first_element:
            real_median = last_element
            tmp_swap = array_num_input_median[p]
            array_num_input_median[p] = real_median
            array_num_input_median[r-1] = tmp_swap
            return
    if last_element >= first_median:
        if last_element <= first_element:
            real_median = last_element
            tmp_swap = array_num_input_median[p]
            array_num_input_median[p] = real_median
            array_num_input_median[r-1] = tmp_swap
            return
    #else
    #continua do jeito que esta porque o primeiro elemento ja deve ser a mediana




def quicksort_by_the_book_median(array_num_input_median, p, r, number_comparisons_median):
    if p < r:
        swap_first_median(array_num_input_median,p,r)
        q = partition(array_num_input_median,p,r,number_comparisons_median)

        #        swap_first_last(array_numbers,p,q-1)
        quicksort_by_the_book_median(array_num_input_median,p,q-1,number_comparisons_median)

        #        swap_first_last(array_numbers,q,r)
        quicksort_by_the_book_median(array_num_input_median,q,r,number_comparisons_median)




workdirectory = "./workdir"
#name_of_file = "10.txt"
#name_of_file = "100.txt"
#name_of_file = "1000.txt"
#name_of_file = "testePequeno.txt"
name_of_file = "_32387ba40b36359a38625cbb397eee65_QuickSort.txt"
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
array_num_input_last = array(number_list, dtype = 'L')
array_num_input_median = array(number_list, dtype = 'L')


print "File loading ended."

number_comparisons = ComparisonCounter.ComparisonCounter()
number_comparisons_last = ComparisonCounter.ComparisonCounter()
number_comparisons_median = ComparisonCounter.ComparisonCounter()

#quicksort_by_the_book(array_num_input,0, len(array_num_input), number_comparisons)
#quicksort_by_the_book_last(array_num_input_last,0, len(array_num_input_last), number_comparisons_last)
quicksort_by_the_book_median(array_num_input_median,0,len(array_num_input_median),number_comparisons_median)


file_pointer = open(outputnameofile,mode='w')

print "number of comparisons is: " + str(number_comparisons.get_value())

print "number of comparisons swaping first with last is: " + str(number_comparisons_last.get_value())

size_of_file = len(array_num_input)
for x in range(0,size_of_file,1):
    file_pointer.write(str(array_num_input[x]) + '\n')

file_pointer.close()

print "Output was generated"