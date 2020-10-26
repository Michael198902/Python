#Hash table creation
items1 = dict({"key 1":1, "key 2":2, "key 3": "Three"})
print(items1)

#create a hash table progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)

#replace an item

items2["key2"] = "two"
print(items2)

#iterate the keys and values 

for key,value in items2.items():
    print("key: ", key, "value: ", value)
    