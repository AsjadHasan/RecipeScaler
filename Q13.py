def scale_recipe():
    ingredients = []

    number_of_ingredients = int(input("Number of ingredients: "))

    for i in range(number_of_ingredients):
        name = input("Ingredient name: ")
        amount = float(input("Amount: "))
        unit = input("Unit: ")

        ingredients.append((name, amount, unit))

    scaling_factor = float(input("Scaling factor: "))

    print("\nScaled Recipe:")

    for name, amount, unit in ingredients:
        scaled_amount = amount * scaling_factor
        print(f"{name}: {scaled_amount} {unit}")


scale_recipe()