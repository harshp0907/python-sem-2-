num = int(input("Enter a number: "))

if num < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
is_perfect = (sum_of_divisors == num)

digits = list(map(int, str(num)))
armstrong_sum = sum(d ** len(digits) for d in digits)
is_armstrong = (armstrong_sum == num)

is_palindrome = (str(num) == str(num)[::-1])

square = num ** 2
is_automorphic = (str(square).endswith(str(num)))

print(f"{num} is Prime: {is_prime}")
print(f"{num} is Perfect: {is_perfect}")
print(f"{num} is Armstrong: {is_armstrong}")
print(f"{num} is Palindrome: {is_palindrome}")
print(f"{num} is Automorphic: {is_automorphic}")
