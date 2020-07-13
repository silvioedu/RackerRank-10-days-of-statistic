if __name__ == '__main__':
    n = int(input())
    x = sorted(list(map(int, input().split())))
    u = sum(x)/n

    total = 0
    for i in range(n):
        total += (x[i]-u)**2

    from math import sqrt
    total = sqrt(total/n)

    print(round(total,1))
