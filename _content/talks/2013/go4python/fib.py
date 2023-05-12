#!/usr/bin/python

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b

def fib_rec(n):
    return 1 if n <= 1 else fib_rec(n-1) + fib_rec(n-2)

for x in range(10):
	print fib(x), fib_rec(x)
