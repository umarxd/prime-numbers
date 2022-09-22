def is_prime(n):
    if n == 1:
        return False

    factors = 0
    for i in range(1, n+1):
        if n % i == 0:
            factors += 1
    if factors == 2:
        return n
    return False

def write(n):
    with open("primes.txt", "a") as f:
        f.write(f"{str(n)}\n")

def loop():
    for i in range(1, 100000000000000000000000000000000000):
        number = is_prime(i)
        if number:
            print(i)
            write(i)

if __name__ == "__main__":
    loop()

