txt = input("Enter any text : ")

freq = {}

for ch in txt:
	print(ch)
	if ch in freq :
		freq[ch] += 1

	else : 
		freq[ch] = 1

print(freq)
# for key,value in freq.items():
# 	print(key,":",value)


for key in freq :
	print(key,":",freq[key])