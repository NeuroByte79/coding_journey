#Write a progaram that generates float and integer random numbes.

# random number operations using random module
import random
import datetime
random.seed(datetime.datetime.now().timestamp())
print(random.random())
print(random.random())
print(random.randint(10,100)) 
