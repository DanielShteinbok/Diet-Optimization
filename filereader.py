import csv

nutrients_list = ["Calories (kcal)","Protein (g)","Sodium (mg)","Potassium (mg)","Calcium (mg)","Magnesium (mg)","Zinc (mg)","Iron (mg)","Vitamin A (µg)","Vitamin B1 (Thiamin) (mg)","Vitamin B2 (Riboflavin) (mg)","Vitamin B3 (Niacin) (mg)","Vitamin B6 (mg)","Vitamin B12 (µg)","Vitamin C (mg)","Vitamin E (mg)"]

def read_grocery_info(filename="./grocery_info.csv"):
    # grocery_list = []
    # chose to neglect order and just go by item name
    grocery_dict = {}
    with open(filename, mode='r', encoding='utf-8-sig') as grocery_info_file:
        reader = csv.DictReader(grocery_info_file)

        for row in reader:
            grocery_info = {"nutrients": {}}
            for k,v in row.items():
                if k in nutrients_list:
                    grocery_info["nutrients"][k] = float(v)
                elif k == "Item":
                    pass
                else:
                    grocery_info[k] = float(v)
            # grocery_list.append(grocery_info)
            grocery_dict[row["Item"]] = grocery_info

    # return grocery_list
    return grocery_dict

def read_recipes(filename="./recipe_info.csv"):
    # recipe_list = []
    recipe_dict = {}
    with open(filename, mode='r', encoding='utf-8-sig') as recipe_info_file:
        reader = csv.DictReader(recipe_info_file)

        for row in reader:
            recipe_info = {}
            for k, v in row.items():
                if not(k == "Recipe" or float(v) == 0):
                    recipe_info[k] = float(v)
            recipe_dict[row["Recipe"]] = recipe_info
    return recipe_dict

def read_nutrition(filename="./nutrient_requirements_extended.csv"):
    nutrient_dict = {}
    with open(filename, mode='r', encoding='utf-8-sig') as nutrient_file:
        reader = csv.DictReader(nutrient_file)

        for row in reader:
            nutrient_dict[row["Nutrient"]] = float(row["Daily Requirement"])
    return nutrient_dict