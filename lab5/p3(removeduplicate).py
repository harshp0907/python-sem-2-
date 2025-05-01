# import random
# list=[]
# for ele in range(0,11):
#   list.append(random.randint(1,80))
# print(list)

# a=set(list)
# print(a)



# x = 5
# while x < 10:
#     print(x)



numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)