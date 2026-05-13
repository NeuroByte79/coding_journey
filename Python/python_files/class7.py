# remove duplicates
nums = [1,2,2,3,3,3]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print(unique,'\n')

# or 
nums = [1,2,2,3,3,3]
print(list(set(nums)),'\n')

# use built - in function
print(sum(range(5)),'\n')

# use list comprehension
print([i*i for i in range(5)],'\n')

# use to genrator large data 
print(sum(i*i for i in range(1000)),'\n')

# Use set for fast lookups
nums = {1,2,3,4}
print(3 in nums,'\n')

# use join() for string concanation 
print("".join(["a","b","c"]),"\n")

# Use enumerate insttead of manual indexing 
items = ["a","b","c"]
for i,v in enumerate(items):
    print(i,v)


