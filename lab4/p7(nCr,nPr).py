n = int(input("Enter n: "))
r = int(input("Enter r: "))

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

fact_n = factorial(n)
fact_r = factorial(r)
fact_n_r = factorial(n - r)

nPr = fact_n // fact_n_r
nCr = fact_n // (fact_r * fact_n_r)

print(f"nPr: {nPr}")
print(f"nCr: {nCr}")
