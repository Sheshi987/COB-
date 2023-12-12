from collections import defaultdict
# Dummy data for demonstration
recipes = [
    {'title': 'Macaroni and Cheese', 'ingredients': ['macaroni', 'cheese', 'milk']},
    {'title': 'Tacos', 'ingredients': ['tortillas', 'chicken', 'lettuce', 'tomatoes']},
    {'title': 'Chicken Parmesan', 'ingredients': ['chicken breasts', 'all-purpose flour', 'egg', 'parmesan cheese']},
    {'title': 'Caesar Salad', 'ingredients': ['romaine lettuce', 'chicken', 'caesar dressing']},
]
def find_recipes(ingredients):
    recipe_map = defaultdict(list)
    for recipe in recipes:
        for ingredient in recipe['ingredients']:
            recipe_map[ingredient].append(recipe['title'])

    recipe_titles = []
    for ingredient in ingredients:
        recipe_titles.extend(recipe_map[ingredient])

    return list(set(recipe_titles)) # remove duplicates

def search_recipes():
    print("Please enter a comma-separated list of ingredients:")
    ingredients = input().split(',')
    recipe_titles = find_recipes(ingredients)
    if not recipe_titles:
        print("No recipes found for the provided ingredients.")
    else:
        print("\nHere are the recipes that can be made with the provided ingredients:")
        for title in recipe_titles:
            print(title)

if __name__ == "__main__":
    search_recipes()