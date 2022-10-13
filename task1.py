import timeit

print("list:", timeit.timeit("[1,2,3,4,5,6,7,8,9,10]", number=100_000_000))
print("tuple:", timeit.timeit("(1,2,3,4,5,6,7,8,9,10)", number=100_000_000))

fib1 = 1
fib2 = 1

n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)

i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print("Значение этого элемента:", fib2)