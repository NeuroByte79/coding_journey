# n = int(input("enter a number : "))
# sum = 0
# for i in range (1,n+1):
# 	sum+=i
# 	print("total sum ",sum)

# n = int(input("enter a number : "))
# sum = 0
# i = 0
# while i<=n :
# 	sum +=i
# 	i+=1
# 	print("total sum is ",sum )
# x = []
# n = int(input("enter the number of elements : "))
# for i in range (n):
# 	print("enter the element : ",end = '')
# 	x.append(input())
# search = input("enter the search no : ")
# for i in range (len(x)):
# 	if x[i]==search:
# 		print("no is found : ",i)
# 		break
# else :
# 	print("element no found : ")
# for i in range(10,0,-1):
# 	print(i)
# n=50
# for i in range (n):
# 	if(i%2!=0):
# 		print("number is odd",i)

# else :

# 	print ("loop end :")


# for i in range (1,50,2):
# 	print(i) 

# number = int(input("enter a number : "))
# for i in range (2000,3200):
# 	if (i%7==0)and (i%5==0):
#     	number.append(i)
# print(number)



# numbers = []

# for i in range(2000, 3201):
#     if i % 7 == 0 and i % 5 == 0:
#         numbers.append(i)

# print(numbers)

# num = int(input("enter the number : "))
# sum = 0
# for i in range (1 , n+1):
# 	sum=


dist = {}
n = int(input("enter the no of player : "))
for i in range(n):
	player  = str(input("enter the player name : "))
	score = int(input("enter the score :"))
	dist.update({player:score})
print(dist)
search  = str(input("enter the search player name "))
for key in dict :
	if key == search:
		print("score is ",dist[key])x

