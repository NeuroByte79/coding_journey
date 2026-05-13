# Write a program which will find all such numbers which are divisible by 7 but not are a multiple of 5, between 2000 and 3200 (both included). The number obtained should be printed in comma-separated squence on a single line 
lst = []
for num in range(2000,3201):
    if num % 7 == 0 and num % 5 != 0 :
        lst.append(str(num))
print(','.join(lst))


