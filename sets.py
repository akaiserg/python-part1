sets = {"A", "B"}

sets.add("C")
# no order
print(sets)

sets.add("C")

sets.remove("C")
print(sets)

empty = set()

my_name = {"A", "N", "D", "R", "E", "S"}
your_name = {"P", "E", "T", "E", "R"}

print(my_name.difference(your_name))
print(my_name.intersection(your_name))
print(my_name.union(your_name))