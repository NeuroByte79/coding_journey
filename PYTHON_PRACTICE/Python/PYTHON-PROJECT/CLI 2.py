# Read file 
file = open("sample.txt", "r")
text = file.read().lower()

# Split word 
words = text.split()

# Count

total_word = len(words)
unique_word = len(set(words))
freq = {}
for word in words:
	if word in freq :
		freq[word] += 1
	else:
		freq[word] = 1


# Converting dictionary to list

items = list(freq.items())

# Manual sorting 
n = len(items)

for i in range(n):
	for j in range(0,n - i - 1):
		if items[j][1] < items[j  + 1][1]:
			# swap
			items[j],items[j + 1] = items[j + 1],items[j]



# output 

print("Total Words:",total_word)
print()
print("Unique Words:",unique_word)
print()
print("Top 10 words:",items[:10])

file.close()