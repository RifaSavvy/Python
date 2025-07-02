my_list = [1, 2, 2, 3, 4, 4, 5]

# Without preserving order:
unique1 = list(set(my_list))
print(unique1)  
# e.g. [1,2,3,4,5] (order unpredictable)

# Preserve order – concise:
unique2 = list(dict.fromkeys(my_list))
print(unique2) 

# Preserve order – explicit:
seen = set()
unique3 = [x for x in my_list if not (x in seen or seen.add(x))]
print(unique3)

