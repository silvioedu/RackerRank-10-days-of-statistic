from math import factorial, exp

if __name__ == '__main__':
    m = float(input())
    x = int(input())
    poisson_prob = ((m ** x) * exp(-m)) / factorial(x)
    print("%.3f" %poisson_prob)
