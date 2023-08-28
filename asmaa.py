my_name = input("enter your name :")
my_age = int(input("enter your age :"))
print(f"my name is {my_name} and I am {my_age} years old")
first_number =int(input("enter first number :"))
second_number =int(input("enter second number :"))
operation = input("what is the operation? (+ - * /) :")
if operation == '+' :
    print(first_number + second_number)
elif operation == '-' :
    print(first_number - second_number)
elif operation == '*' :
    print(first_number * second_number)
elif operation == '/' :
    print(first_number / second_number)
bus_capacity = 20
people_inbus = int(input("who many people are in the bus ? :"))
waiting = int(input("how many peopl are waiting ?"))
empty_seats = bus_capacity - people_inbus
if empty_seats >= waiting :
    print("join")
else :
    print("the bus is full")