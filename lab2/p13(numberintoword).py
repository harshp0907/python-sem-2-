numberswords = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]

a = int(input("Enter a number between 0 and 19: "))

if 0 <= a <= 19:
    print(numberswords[a])
else:
    print("Number out of range!")

