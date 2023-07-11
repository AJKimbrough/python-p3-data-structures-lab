spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    new_Arr = []
    for food in spicy_foods:
        new_Arr.append(food["name"])
    return new_Arr

def get_spiciest_foods(spicy_foods):
    new_Arr = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            new_Arr.append(food)
    return new_Arr

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(food["name"] + " (" + food["cuisine"] + ") " + "| " + "Heat Level: " + (food["heat_level"] * "🌶"))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food["cuisine"]:
            return food
    return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(food["name"] + " (" + food["cuisine"] + ") " + "| " + "Heat Level: " + (food["heat_level"] * "🌶"))

def get_average_heat_level(spicy_foods):
    new_Arr = []
    for food in spicy_foods:
        new_Arr.append(food["heat_level"])
    x = (new_Arr[0] + new_Arr[1] + new_Arr[2]) / len(spicy_foods)
    return x
        
def create_spicy_food(spicy_foods, spicy_food):
    new_Arr = spicy_foods
    new_Arr.append({
                "name": spicy_food["name"],
                "cuisine": spicy_food["cuisine"],
                "heat_level": spicy_food["heat_level"],
            })
    return new_Arr

print(create_spicy_food(spicy_foods, {
                "name": "Griot",
                "cuisine": "Haitian",
                "heat_level": 10,
            },))

