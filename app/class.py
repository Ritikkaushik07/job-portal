def prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False

    return True

N=int(input('enter range to check prime number : '))

for i in range(1, N + 1):
    if prime(i):
        print(i, end=" ")
