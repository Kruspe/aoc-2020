from typing import List, NamedTuple


class Product(NamedTuple):
    ingredients: List[str]
    allergens: List[str]


def solve():
    allergen_mapping = {}
    for allergen in allergens:
        possible_ingredients = set()
        for product in products:
            if allergen in product.allergens:
                if not possible_ingredients:
                    possible_ingredients.update(product.ingredients)
                else:
                    possible_ingredients.intersection_update(product.ingredients)
        allergen_mapping[allergen] = possible_ingredients

    done_ingredients = []
    while max(len(i) for i in allergen_mapping.values()) != 1:
        for allergen, possible_ingredients in allergen_mapping.items():
            if possible_ingredients not in done_ingredients and len(possible_ingredients) == 1:
                done_ingredients.append(list(possible_ingredients)[0])
                for key, a in allergen_mapping.items():
                    if allergen != key:
                        a.difference_update(possible_ingredients)

    contaminated_ingredients = []
    for key in sorted(allergen_mapping):
        contaminated_ingredients.append(list(allergen_mapping.get(key))[0])
    free_ingredients = set(ingredients)
    free_ingredients.difference_update(contaminated_ingredients)
    counter = 0
    for product in products:
        for i in free_ingredients:
            if i in product.ingredients:
                counter += 1

    return counter, ','.join(contaminated_ingredients)


def parse(data):
    product_map = []
    ingredient_set = set()
    allergen_set = set()
    for i, line in enumerate(data):
        all_ingredients, all_allergens = line.split(' (')
        product_ingredients = all_ingredients.split(' ')
        product_allergens = all_allergens.replace('contains ', '').replace(')', '').split(', ')
        product_map.append(Product(product_ingredients, product_allergens))
        ingredient_set.update(product_ingredients)
        allergen_set.update(product_allergens)
    return product_map, ingredient_set, allergen_set


if __name__ == '__main__':
    products, ingredients, allergens = parse([line.strip() for line in open('data.txt')])
    save_count, contaminated = solve()
    print('Part 1', save_count)
    print('Part 2', contaminated)
