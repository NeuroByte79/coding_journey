choice_convert = input("Enter conversion(KM_to_Miles,Kg_to_Pounds,celsius_to_fahrenheit) : ")
value = float(input("Enter value to convert : "))
if choice_convert == "KM_to_Miles" :
	miles = (1/1.6)*value
	print(f'{value}km will be equal to {miles}miles.')
elif choice_convert == 'Kg_to_Pounds':
	pounds_value = ((1/2.205)*value)
	print(f'{value}Kg will be equal to {pounds_value}Pounds.')
elif choice_convert == 'celsius_to_fahrenheit':
	fahrenheit_value = ((1/33.8)*value)
	print(f'{value} degrees celsius will be equal to {fahrenheit_value}degrees fahrenheit. ')
else:
	print('Worng choice !')
