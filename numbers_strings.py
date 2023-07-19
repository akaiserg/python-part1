# NUMBERS 
age = 30
PI = 3.14159 # PI value
print(age)
print(PI)
print(23 // 3)
print(23 % 3)

string_with_quotes1 = "Hello World"
string_with_quotes2 = 'Hello World'
string_with_quotes3 = '"Hello World"'
string_with_quotes4 = 'Hello \nWorld'
print(string_with_quotes4, "\n",string_with_quotes3)
multiline = """ Hello 


#STRINGS

world
"""
print(multiline)
print("You are " + str(41))

name = "Andrés"
greeting = f"How are you, {name}"
print(greeting)

#Format template

name = "Jose"
final_greeting = "How are you {}?"
jose_greeting = final_greeting.format(name)
#jose_greeting = final_greeting.format(name="Jose") # with default value
print(jose_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)