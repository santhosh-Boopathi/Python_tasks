def inr_convertion(conversion,user_input):

    # conversion=input("Enter your choice from [INR-USD or INR-EUR or INR-YEN or ALL] :")
    # user_input=float(input("Enter the amount to be converted : "))

    if (conversion=='INR-USD'):
        inr=0.012
        money=user_input*inr
        print("Your INR-USD conversion is ",money)
        
    elif (conversion=='INR-EUR'):
        inr=0.011
        money=user_input*inr
        print("Your INR-EUR conversion is ",money)

    elif (conversion=='INR-YEN'):
        inr=1.84
        money=user_input*inr
        print("Your INR-YEN conversion is ",money)

    elif (conversion=='ALL'):
        inr=0.012
        money=user_input*inr
        print("Your INR-USD conversion is ",money)
        inr=0.011
        money=user_input*inr
        print("Your INR-EUR conversion is ",money)
        inr=1.84
        money=user_input*inr
        print("Your INR-YEN conversion is ",money)


    else:
        print("Enter the valid input..")
        
        