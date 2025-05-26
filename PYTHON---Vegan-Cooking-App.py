# vegan_cooking_app.py

class Recipe:
    def __init__(self, name, ingredients, steps, category):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.category = category

    def display(self):
        print(f"\n--- {self.name} ---")
        print("Category:", self.category)
        print("\nIngredients:")
        for ing in self.ingredients:
            print(f"- {ing}")
        print("\nSteps:")
        for i, step in enumerate(self.steps, 1):
            print(f"{i}. {step}")
        print("-" * 30)


class VeganCookingApp:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def list_categories(self):
        categories = set(recipe.category for recipe in self.recipes)
        print("\nAvailable Categories:")
        for cat in categories:
            print(f"- {cat}")

    def list_recipes(self, category=None):
        print("\nAvailable Recipes:")
        for recipe in self.recipes:
            if category is None or recipe.category.lower() == category.lower():
                print(f"- {recipe.name} ({recipe.category})")

    def find_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                recipe.display()
                return
        print("Recipe not found.")

    def run(self):
        print("🌱 Welcome to the Vegan Cooking App! 🌿")
        while True:
            print("\n1. Show all recipes")
            print("2. Show recipes by category")
            print("3. View a recipe")
            print("4. List categories")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.list_recipes()
            elif choice == '2':
                cat = input("Enter category: ")
                self.list_recipes(cat)
            elif choice == '3':
                name = input("Enter recipe name: ")
                self.find_recipe(name)
            elif choice == '4':
                self.list_categories()
            elif choice == '5':
                print("Thanks for cooking vegan! See you next time! 🌸")
                break
            else:
                print("Invalid option. Try again.")


# Sample vegan recipes
app = VeganCookingApp()
app.add_recipe(Recipe(
    "Vegan Pancakes",
    ["1 cup flour", "1 tbsp sugar", "1 tbsp baking powder", "1 cup oat milk", "1 tbsp oil"],
    ["Mix all ingredients.", "Heat a pan and pour batter.", "Cook until golden brown."],
    "Breakfast"
))

app.add_recipe(Recipe(
    "Chickpea Salad",
    ["1 can chickpeas", "1 cucumber", "1 tomato", "Lemon juice", "Olive oil", "Salt"],
    ["Drain chickpeas.", "Chop veggies.", "Mix all ingredients in a bowl."],
    "Lunch"
))

app.run() 
