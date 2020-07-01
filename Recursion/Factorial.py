def findFactorialRecursive(value):
    if value == 2:
        return 2
    return value * findFactorialRecursive(value-1)

def findFactorialIterative(value):
    answer = 1
    if value == 2:
        return 2
    for i in range(2,value+1):
        answer = answer * i
    return answer

print(findFactorialRecursive(5))
print(findFactorialIterative(6))