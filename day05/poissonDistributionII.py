if __name__ == '__main__':
    avgX, avgY = [float(num) for num in input().split(" ")]

    CostX = 160 + 40 * (avgX + pow(avgX, 2))
    CostY = 128 + 40 * (avgY + pow(avgY, 2))

    print(round(CostX, 3))
    print(round(CostY, 3))
