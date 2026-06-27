# ==========================================
# 1. RECIPES (The List of Recipes)
# ==========================================
print("=== RECIPES ===")

recipes = {
    "Arrabiata": ["Pasta", "Tinned Tomatoes", "Garlic", "Chili Flakes", "Olive Oil"],

    "Potaje de Garbanzos": ["Chickpeas", "Spinach", "Garlic", "Onions", "Paprika", "Olive Oil"],

    "Mujadara": ["Lentils", "Rice", "Onions", "Cumin", "Olive Oil"],

    "Dahl Makhani": ["Black Lentils", "Kidney Beans", "Butter", "Cream", "Ginger", "Garlic",
                     "Garam Masala"],

    "Vegetarian Keema": ["Soya Mince", "Peas", "Onions", "Tomatoes", "Ginger", "Garlic",
                         "Garam Masala"],

    "Sopa de Lentejas": ["Lentils", "Carrots", "Celery", "Onions", "Garlic", "Vegetable Broth",
                         "Cumin"],

    "Gallo Pinto": ["Rice", "Black Beans", "Onions", "Bell Peppers", "Cilantro",
                    "Worcestershire Sauce"],

    "Mangú": ["Plantains", "Butter", "Water", "Salt"],

    "Chana Masala": ["Chickpeas", "Onions", "Tomatoes", "Ginger", "Garlic", "Chana Masala Spice Mix"],

    "Habichuelas Guisadas": ["Red Kidney Beans", "Tinned Tomatoes", "Onions", "Garlic",
                             "Cilantro", "Water", "Butternut Squash"]
}

recipe_names = list(recipes.keys())

while True:
        print("\n" + "="*20)
        for index, name in enumerate(recipe_names, start =1):
            print(f"{index}.{name}")
        print("="*20 + "\n")
        print("0. Exit")


        user_input = input("Which recipe would you like to make? ")
        if user_input == "0":
            print("Goodbye")
            break

        choice = int(user_input)
        selected_recipe = recipe_names[choice - 1]

        ingredients_list = recipes[selected_recipe]
        print(f"Ingredients: {', '.join(ingredients_list)}")

        again = input("Would you like to make another recipe? (y/n): ")
        if again.lower() == "n":
            print("Happy Cooking! 🍳")
            break
