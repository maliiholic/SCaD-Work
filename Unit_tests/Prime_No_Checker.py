def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Optimized to check up to sqrt(n)
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":  # Prevents execution when imported
    num = int(input("Enter a number: "))
    print(is_prime(num))
