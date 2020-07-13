if __name__ == '__main__':
    a, b = map(int,input().split())
    n = int(input())

    p = a/b
    q = 1-p
    gd = pow(q, n-1) * p

    print("%.3f"%gd)
