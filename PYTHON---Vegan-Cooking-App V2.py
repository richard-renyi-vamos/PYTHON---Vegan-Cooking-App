import json
import random

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

    def to_dict(self):
        return {
            "name": self.name,
            "ingredients": self.ingredients,
            "steps": self.steps,
            "category": self.category
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["ingredients"], data["steps"], data["category"])


class VeganCookingApp:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def edit_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                new_name = input("New name (leave blank to keep): ")
                new_category = input("New category (leave blank to keep): ")
                new_ingredients = input("New ingredients (comma-separated, leave blank to keep): ")
                new_steps = input("New steps (comma-separated, leave blank to keep): ")

                if new_name: recipe.name = new_name
                if new_category: recipe.category = new_category
                if new_ingredients: recipe.ingredients = [i.strip() for i in new_ingredients.split(',')]
                if new_steps: recipe.steps = [s.strip() for s in new_steps.split(',')]

                print("Recipe updated!")
                return
        print("Recipe not found.")

    def delete_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                self.recipes.remove(recipe)
                print(f"'{name}' deleted successfully.")
                return
        print("Recipe not found.")

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

    def save_recipes_to_file(self, filename='recipes.json'):
        with open(filename, 'w') as f:
            json.dump([r.to_dict() for r in self.recipes], f)
        print("Recipes saved to file.")

    def load_recipes_from_file(self, filename='recipes.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.recipes = [Recipe.from_dict(d) for d in data]
            print("Recipes loaded from file.")
        except FileNotFoundError:
            print("No saved file found.")

    def suggest_random_recipe(self):
        if not self.recipes:
            print("No recipes available.")
        else:
            random.choice(self.recipes).display()

    def run(self):
        print("🌱 Welcome to the Vegan Cooking App! 🌿")
        while True:
            print("\n1. Show all recipes")
            print("2. Show recipes by category")
            print("3. View a recipe")
            print("4. List categories")
            print("5. Edit a recipe")
            print("6. Delete a recipe")
            print("7. Suggest a random recipe")
            print("8. Save recipes")
            print("9. Load recipes")
            print("10. Exit")
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
                name = input("Enter recipe name to edit: ")
                self.edit_recipe(name)
            elif choice == '6':
                name = input("Enter recipe name to delete: ")
                self.delete_recipe(name)
            elif choice == '7':
                self.suggest_random_recipe()
            elif choice == '8':
                self.save_recipes_to_file()
            elif choice == '9':
                self.load_recipes_from_file()
            elif choice == '10':
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
