def phone(brand_input,quantity):

    brand = {
        "redmi" : 15000,
        "vivo" : 20000,
        "oppo" : 35000
    }
    # brand_input = input("Enter the brand :")
    # quantity = int(input("Enter the quantity : "))
    output = print(quantity*brand[brand_input])

def state():

    dictionary = {
        "tamilnadu":{"erode":{"perundurai":6000, "pidariyur" :5000, "chennimalai":8000}, 
                    "coimbatore":{"saravanampatti":3000, "gandhipuram":10000, "thudiyalur":2000}, 
                    "madurai":{"arapalayam":5000, "maatuthavani":6000}
    }
    }

    state = input("Enter the state : ")
    district = input("Enter the district : ")
    place_1 = input("Enter the place : ")
    place_2 = input("Enter the place : ")
    place_3 = input("Enter the place : ")
    result = print((dictionary[state][district][place_1]+dictionary[state][district][place_2]+dictionary[state][district][place_3])*250)

