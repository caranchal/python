Largest_number = -9999999999
number = int(input("введите 1"))
while number != -1:
    if number > Largest_number:
        Largest_number = number
    number = int(input("нипишите -1 что бы остановить програму"))
print("наибольшее введёное число", Largest_number)
