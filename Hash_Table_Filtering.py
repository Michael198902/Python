#Unique keys with certain values:
items = ["apple", "pear", "orange", "banana", "apple",
        "orange", "apple", "pear", "banana", "orange", 
        "apple", "kiwi", "pear", "apple", "orange"]

filter = dict()

for key in items:
    filter[key] = 0

result = set(filter.keys())
print(result)


    
