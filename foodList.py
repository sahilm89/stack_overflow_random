#!/usr/bin/python
''' This program takes in a relations file and a food text files as inputs
and can be used to update the food text file based on changes in either of these'''

relations = {}
foodDict = {}

# Mapping ingredients to each other in the relations dictionary
with open("relations.txt") as r:
    relationlist=r.read().splitlines()
    for relation in relationlist:
        item, equatedTo = relation.split(': ')
        ingredientsAndCoefficients = equatedTo.split(' + ')
        listIngredients = []
        for ingredient in ingredientsAndCoefficients:
            coefficient, item2 = ingredient.split(' x ')
            # A list of sets of amount and type of ingredient
            listIngredients.append((float(coefficient),item2))
        relations.update({item:listIngredients})


# Creating a food dictionary with values from food.txt and mapping to the relations dictionary
with open("food.txt") as g:
    foodlist=g.read().splitlines()
    for item in foodlist:
        food,value = item.split(': ')
        foodDict.update({food:value})
    for food in relations.keys():
        # Raw ingredients will not change here.
        value = 0.
        for item2 in range(len(relations[food])):
            # Calculating new value for complex here.
            value += relations[food][item2][0]* float(foodDict[relations[food][item2][1]])
        foodDict.update({food: value })

# Altering the food.txt with the new dictionary values 
with open("food.txt",'w') as g:
    for key in sorted(foodDict.keys()):
        g.write(key + ': ' + str (foodDict[key])+ '\n')
        print key + ': ' + str(foodDict[key])
