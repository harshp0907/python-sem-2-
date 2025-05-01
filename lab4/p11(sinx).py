degrees = float(input("Enter x in degrees: "))

x = degrees * (3.14159 / 180)

sinx = 0
term = x
sign = 1
i = 1

while abs(term) > 0.000001:  
    sinx = sinx + (sign * term)
    i = i + 2
    term = term * (x * x) / (i * (i - 1))
    sign = sign * -1

print("sin(" + str(degrees) + ") ≈ " + str(sinx))
