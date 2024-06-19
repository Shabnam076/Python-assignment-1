"""Write a python program that generates the first n numbers in the 
Fibonacci sequence."""

n = 12
fib_sequence = [0, 1]
if n == 1:
    fib_sequence = [0]
elif n > 2:
    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)
for num in fib_sequence:
    print(num)
