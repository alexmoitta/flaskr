#!/usr/bin/python

def fastpower(a,b):
    if b == 1:
        return a
    else:
        c = a*a
        ans = fastpower(c,b/2)
    if b % 2 != 0: #b e impar
        return a * ans
    else:
        return ans


result = fastpower(2,16)


print "o resultado e " + str(result)

