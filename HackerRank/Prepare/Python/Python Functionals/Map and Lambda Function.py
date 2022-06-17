cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    result = []
    for i in range(n):
        if i == 0:
            result.append(0)
        elif i == 1:
            result.append(1)
        else:
            result.append(result[i-1]+result[i-2])
    
    return result

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))