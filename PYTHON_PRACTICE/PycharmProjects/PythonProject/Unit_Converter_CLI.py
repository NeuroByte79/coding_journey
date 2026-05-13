def unit_converter():
    print("\n🔄 UNIT CONVERTER")
    print("1. Distance (km ↔ miles)")
    print("2. Temperature (C ↔ F)")
    print("3. Weight (kg ↔ pounds)")
    print("4. Currency (INR ↔ USD)")

    choice = input("Choose conversion type (1-4): ")

    # Conversion factors
    KM_TO_MILES = 0.621371
    KG_TO_POUNDS = 2.20462
    INR_TO_USD = 0.012  # Example rate (can update)

    if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        miles = km * KM_TO_MILES
        print(f"{km} km = {miles:.2f} miles")

    elif choice == "2":
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9 / 5) + 32
        print(f"{c}°C = {f:.2f}°F")

    elif choice == "3":
        kg = float(input("Enter weight in kg: "))
        pounds = kg * KG_TO_POUNDS
        print(f"{kg} kg = {pounds:.2f} pounds")

    elif choice == "4":
        inr = float(input("Enter amount in INR: "))
        usd = inr * INR_TO_USD
        print(f"₹{inr} = ${usd:.2f}")

    else:
        print("❌ Invalid choice")


# Run
unit_converter()