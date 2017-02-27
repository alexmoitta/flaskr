#!/usr/bin/python

'''To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers. You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.

So: what's the product of the following two 64-digit numbers?

3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627


Fazendo com  12345 and 6789 para entender





'''


# caso basico
x = 12345
y = 6789
base = 2
expn1 = 32
expn2 = expn1 * 2

a = (x / base ** expn1)
b = (y / base ** expn1)
z2 = a * b

c = (x - (a * base ** expn1))
d = (y - (b * base ** expn1))

z0 = c * d
z1 = ((a + c) * (b + d)) - z2 - z0

result = (z2 * base ** expn2) + (z1 * base ** expn1) + z0

print "caso basico"
print z2
print z0
print z1
print result

# exercicio da aula

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
base = 2
expn1 = 32
expn2 = expn1 * 2

a = (x / base ** expn1)
b = (y / base ** expn1)
z2 = a * b

c = (x - (a * base ** expn1))
d = (y - (b * base ** expn1))

z0 = c * d
z1 = ((a + c) * (b + d)) - z2 - z0

result = (z2 * base ** expn2) + (z1 * base ** expn1) + z0

print "\nexercicio da aula "
print z2
print z0
print z1

print result


