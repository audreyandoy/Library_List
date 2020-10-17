print("*** WELCOME TO THE LIBRARY ***")

catalogue = [
    "The Lord of the Rings", 
    "Harry Potter", 
    "Hunger Games", 
    "The Lion, the Witch, and the Wardrobe", 
    "Becoming", 
    "I am Malala", 
    "Cooking for Dummies", 
    "The Joy of Cooking"
]

fantasy = [
    "The Lord of the Rings", 
    "Harry Potter", 
    "Hunger Games", 
    "The Lion, the Witch, and the Wardrobe"
]

non_fiction = [
    "Becoming", 
    "I am Malala"
]

cooking = [
    "Cooking for Dummies", 
    "The Joy of Cooking"
]

genres = ["FANTASY", "NON-FICTION", "COOKING"]

user_activity = input("What would you like to do? \n [A]Browse [B]Checkout a book \n").upper()

if user_activity == "A":
    print("Here are all of our book genres: ")
    for i in genres:
        print(i)
    
    genre_select = input("What genre would you like to see? \n").upper()
    # input validation
    while genre_select not in genres:
        genre_select = input("Not a genre we have. What genre would you like to see in our catalogue? \n").upper()

    if genre_select == "FANTASY":
        for i in fantasy:
            print(i)
    elif genre_select == "NON-FICTION":
        for i in non_fiction:
            print(i)
    elif genre_select == "COOKING":
        for i in cooking:
            print(i)
