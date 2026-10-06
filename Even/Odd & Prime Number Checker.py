def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

print("Number is:", check_even_odd(num))

if check_prime(num):
    print("Number is Prime")
else:
    print("Number is Not Prime")