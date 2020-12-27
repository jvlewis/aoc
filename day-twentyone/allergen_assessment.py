def countNonAllergenicFoods(allergens, foodCounts):
    foodsWithAllergens = str(allergens.values())
    total = 0
    
    for food, count in foodCounts.items():
        if food not in foodsWithAllergens:
            total += count 

    return total

# return dict of foods and times they appear
def countFoods(foods):
    uniqueFood = set()
    foodCounts = {}
    
    for item in foods:
        for food in item[0]:
            if food not in uniqueFood:
                uniqueFood.add(food)
                foodCounts[food] = 1 
            else:
                foodCounts[food] = foodCounts[food] + 1   
    return foodCounts


# returns dict with all allergens as keys, and the one ingredient that contains each
def getAllergens(foods):
    possibleAllergy = {}

    for item in foods:
        for allergen in item[1]:
            if allergen not in possibleAllergy:
                possibleAllergy[allergen] = set(item[0])
            else:
                possibleAllergy[allergen] &= set(item[0])

    found = set()
    notReduced = True

    while notReduced:
        notReduced = False
        for food in possibleAllergy.values():
            if len(food) == 1:
                found.update(food)
            elif len(food) > 1:
                food.difference_update(found)
                notReduced = True 

    return possibleAllergy
    

def readFoodsAndAllergens(file):
    list = []

    for f in open(file, 'r').read().splitlines():
        foods, allergens = f.split(' (contains ')
        list.append([foods.split(' '), allergens.replace(')', '').split(', ')])
    return list
    

if __name__ == '__main__':
    result = []
    foodsContain = readFoodsAndAllergens('foods.txt') 
    allergens = getAllergens(foodsContain)
    counts = countFoods(foodsContain)
    foodsWithoutAllergens = countNonAllergenicFoods(allergens, counts)

    # Solution 1
    print("There are %d appearances of ingredients without allergens." % foodsWithoutAllergens)

    for x in sorted(allergens.items()):
        result.append("".join(x[1]))
    
    # Solution 2
    print("These are the inredients to avoid %s" % ','.join(result))