import math


def cdf(x, mu, sigma):
    Z = (x - mu) / sigma
    return 0.5 * (1 + math.erf(Z / (math.sqrt(2))))


if __name__ == '__main__':
    x = int(input())
    n = int(input())
    mu = int(input())
    sigma = int(input())

    mu_sum = n * mu
    sigma_sum = math.sqrt(n) * sigma

    print(round(cdf(x, mu_sum, sigma_sum), 4))
