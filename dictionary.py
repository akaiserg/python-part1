friend_ages = {"Jean": 34, "Jason": 45, "Peter": 41}
print(friend_ages["Jason"])

friend_ages["Peter"] = 39

print(friend_ages)

friends = (
    {"name": "Jean", "age":34},
    {"name": "Jason", "age":45},    
    {"name": "Peter", "age":41},
)

print(friends[0]["name"])
friend0 = friends[0]
print(friend0["age"])