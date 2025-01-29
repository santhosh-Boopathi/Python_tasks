def greetings(who,timing):

    # who = input("Enter who you are : ")
    # timing = int(input("Enter the timing : "))
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    weekend = ['saturday','sunday']

    if who=='HR' or who=='hr':
        day=input("Enter the day : ")
        if timing>=9 and timing<12:
            print("Good Morning ")
        elif timing>=12 and timing<3:
            print("Good Afternoon ")
        elif timing>=3 and timing<=6:
            print("Good Evening ")
        if day in weekdays:
            print("Standup Meeting is scheduled at 11 AM\nCommon Meeting is scheduled at 2.30 PM") 
        elif day in weekend:
            print("It's Off")

    elif who=='employee' or who=='Employee':
        if timing>=9 and timing<12:
            print("Good Morning ")
        elif timing>=12 and timing<3:
            print("Good Afternoon ")
        elif timing>=3 and timing<6:
            print("Good Evening ")
        print("Your Meetings are scheduled by HR")


    
    
