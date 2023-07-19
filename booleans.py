truthy = True
falsy = False
age = 20
is_over_age = age >= 18
print(is_over_age)
print(age == 20)
my_number = 5
user_number = int(input("Enter a number: "))
matched = my_number == user_number
print(f"You got it right: {matched}")


default_greeting = "there"
name = input("Enter your name: (optional)")
user_name = name or default_greeting
print(f"Hello, {user_name}!")