if __name__ == '__main__':
    n = int(input())
    values    = list(map(float, input().split()))
    frequency = list(map(int, input().split()))

    all_data  = []
    for i in range(n):
        for f in range(frequency[i]):
            all_data.append(values[i])

    all_data.sort()

    m = len(all_data)//2

    L_half = all_data[:m]
    U_half = all_data[-m:]

    import statistics as st
    q1 = st.median(L_half)
    q3 = st.median(U_half)

    print(q3 - q1)