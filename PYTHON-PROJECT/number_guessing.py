import random

# generate randome number between 1 to 100
target = random.randint(1,100)

attempts = 0
high_score = None    # store best score (lowest attempts)

print("🎯Welcome to Number Guessing Game")
print("Guess a number between 1 and 100")

while True :
	guess = int(input("Enter a number between 1 and 100 : "))
	attempts += 1

	if guess == target :
		print(f'✅ Correct! You guessed in {attempts} attempts.')

		# Update high score 
		if high_score is None or attempts < high_score: 
			high_score = attempts 
			print("🏆 New High Score!")

		print(f'Your Bset Score : {high_score}')
		break

	elif guess > target:
	    print("📈 Too high! Try again.")

	else:
	    print("📉 Too low! Try again")