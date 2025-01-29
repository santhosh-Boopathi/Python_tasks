def metric_imperial(choice):
    
    print("1. Length (meters to feet and inches)")
    print("2. Weight (kilograms to pounds)")
    print("3. Volume (liters to gallons and fluid ounces)")

    # choice = input("Choose a category (1/2/3): ")
    print()
    if choice == "1":
        meters = float(input("Enter length in meters: "))
        feet = meters * 3.28084
        inches = meters / 39.37
        print(f"{meters} meters = {feet} feet and {inches} inches")

    elif choice == "2":
        kilograms = float(input("Enter weight in kilograms: "))
        pounds = kilograms * 2.20462
        print(f"{kilograms} kilograms = {pounds} pounds")

    elif choice == "3":
        liters = float(input("Enter volume in liters: "))
        gallons = liters * 0.264172
        fluid_ounces = liters * 33.814
        print(f"{liters} liters = {gallons} gallons and {fluid_ounces} fluid ounces")

    else:
        print("Please enter valid option")