cube = lambda x: x**3
fibo = [0,1]

def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 0:
        return []
    else:
        for i in range(2,n):
            fibo.append(fibo[i-2]+fibo[i-1])
    return fibo

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))