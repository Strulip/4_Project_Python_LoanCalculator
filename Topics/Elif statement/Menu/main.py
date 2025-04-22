food = {
    'pizza': 'Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy',
    'salad': 'Caesar salad, Green salad, Tuna salad, Fruit salad',
    'soup': 'Chicken soup, Ramen, Tomato soup, Mushroom cream soup'
}

def show_menu():
    select_food = input()
    if select_food in food.keys():
        print(food.get(select_food))

    else:
        print("Sorry, we don't have it on the menu")

show_menu()
