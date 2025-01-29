def flames():

    name1 = input("Enter the first name: ").replace(" ", "").lower()
    name2 = input("Enter the second name: ").replace(" ", "").lower()

    for i in name1:
        if i in name2:
            name1 = name1.replace(i, "", 1)
            name2 = name2.replace(i, "", 1)

    count = len(name1) + len(name2)

    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Sibling"]
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            flames = flames[index + 1:] + flames[:index]
        else:
            flames.pop()

    print("The relationship is:", flames[0])
