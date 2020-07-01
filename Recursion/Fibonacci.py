'''
Given a number N return the index value of the Fibonacci sequence,
where the sequence is:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
'''
def fibonacciIterative(value):
    arr = [0, 1]
    for i in range(2,value+1):
        arr.append(arr[i-2]+ arr[i-1])
    return arr[value]

def fibonacciRecursive(value):
    if value < 2:
        return value
    return fibonacciRecursive(value-1) + fibonacciRecursive(value-2)

print(fibonacciIterative(2))
print(fibonacciRecursive(8))