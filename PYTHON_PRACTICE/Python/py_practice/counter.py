data = ["apple","banana","apple","mango","apple","banana","apple"]

freq = {}

for items in data:
	if items in freq:
		freq[items] += 1
	else:
		freq[items] = 1

print(freq)



# in short use built in function 

from collections import Counter

count = Counter(data)

print(count)