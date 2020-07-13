if __name__ == '__main__':
    n = int(input())
    q1 = sorted(list(map(int, input().split())))
    q3 = sorted(list(map(int, input().split())))

    from statistics import median

    print(int(median(q1[:n//2])))
