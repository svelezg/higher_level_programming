#!/usr/bin/python3
for i in range(0, 8):
    for j in range(i+1, 10):
        print("{0:d}".format(i), "{0:d}, ".format(j), sep='', end='')
print('89')
