import sys 

while True :
	print("\n🌡 Temperature Converter")
	print("1. Celsius -> Fahrenheit")
	print("2. Celsius -> Kelvin")
	print("3. Fahrenheit -> Celsius")
	print("4. Fahrenheit -> Kelvin")
	print("5. Kelvin -> Celsius")
	print("6. Kelvin -> Fahrenheit")
	print("7. Exit")

	choice = input("Choose option : ")

	if choice == "7":
		print("Goodbye 👋")
		break 
	try: 
		temp = float(input("Enter temperature : "))

		if choice == "1"  :
			result = (temp * 9/5) + 32
			print("Result:", result, "°F")

		elif choice == "2" :
			result = temp + 273.15
			print("Result:", result, "K")
		
		elif choice == "3" :
			result = (temp - 32) * 5/9
			print("Result:", result, "°C")

		elif choice == "4" :
			result = (temp - 32) * 5/9 + 273.15
			print("Result:", result, "K")

		elif choice == "5" :
			result = temp - 273.15
			print("Result:", result, '°C')

		elif choice == "6" :
			result = (temp - 273.15) * 9/5 + 32
			print("Result:", result, "°F")

		else:
			print("❌ Invalid choice!")

	except ValueError :
		print("❌please enter a valid number")

