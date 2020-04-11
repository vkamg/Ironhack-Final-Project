import pandas as pd
import re
import ast

# wrangling functions

def lowercase_data(recipe_df):
    recipe_df["category"] = recipe_df["category"].str.lower()
    recipe_df["ingredients"] = recipe_df["ingredients"].str.lower()
    return recipe_df

def normalize(string_column):
    a,b = 'áéíóú','aeiou'
    trans = str.maketrans(a,b)
    return string_column.translate(trans)


def add_main_category(category_column):
    if category_column != 'postres y dulces':
        return "principal"
    else:
        return "postre"


def change_time_cal(time, cal):
    if re.search("Cal", time) is not None:
        return time
    else:
        return cal


def remove_cal_time(time,cal):
    if re.search("Cal", time) is not None:
        return "missing"
    else:
        return time


def object_tonumber(column):
    if column == "missing":
        return None
    else:
        object_split = column.split(" ")
        result = int(object_split[0])
        return result


def gluten_free(intolerances):
    if 'Sin gluten' in intolerances:
        return 1
    else:
        return 0

def lactose_free(intolerances):
    if 'Sin lactosa' in intolerances:
        return 1
    else:
        return 0

def egg_free(intolerances):
    if 'Sin huevo' in intolerances:
        return 1
    else:
        return 0

def sucrose_fructose_free(intolerances):
    if 'Sin sacarosa o fructosa' in intolerances:
        return 1
    else:
        return 0

def low_sodium(intolerances):
    if 'Baja en sodio' in intolerances:
        return 1
    else:
        return 0


def clean_ingredients(ingred_column):
    ingred = ast.literal_eval(ingred_column)
    ingredients_list = []
    for ing in ingred:
        clean_ingred = re.sub(" para.*$", "", ing)
        ingredients_list.append(clean_ingred)
    return ingredients_list

def num_ingred(column):
    return len(column)



def wrangle(df,year):
    filtered = df[df['Year']==year]
    return filtered


def clean_data(dataset):
    recipe_df = lowercase_data(dataset)
    recipe_df["ingredients_clean"] = recipe_df.apply(lambda x: normalize(x["ingredients"]), axis=1)
    recipe_df.drop_duplicates(subset=["recipe_url", "category"], keep="first", inplace=True)
    recipe_df["main_category"] = recipe_df.apply(lambda x: add_main_category(x["category"]), axis=1)
    recipe_df['time_preparation'].fillna('missing', inplace=True)
    recipe_df['calories'].fillna('missing', inplace=True)
    recipe_df["calories"] = recipe_df.apply(lambda x: change_time_cal(x["time_preparation"], x["calories"]),
                                            axis=1)
    recipe_df["time_preparation"] = recipe_df.apply(lambda x: remove_cal_time(x["time_preparation"],
                                                                              x["calories"]), axis=1)
    recipe_df["time_preparation(min)"] = recipe_df.apply(lambda x: object_tonumber(x["time_preparation"]),
                                                         axis=1)
    recipe_df["calories(kcal)"] = recipe_df.apply(lambda x: object_tonumber(x["calories"]), axis=1)
    recipe_df["gluten_free"] = recipe_df.apply(lambda x: gluten_free(x["intolerances"]), axis=1)
    recipe_df["lactose_free"] = recipe_df.apply(lambda x: lactose_free(x["intolerances"]), axis=1)
    recipe_df["egg_free"] = recipe_df.apply(lambda x: egg_free(x["intolerances"]), axis=1)
    recipe_df["sucrose_fructose_free"] = recipe_df.apply(lambda x: sucrose_fructose_free(x["intolerances"]),
                                                         axis=1)
    recipe_df["low_sodium"] = recipe_df.apply(lambda x: low_sodium(x["intolerances"]), axis=1)
    recipe_df["ingredients_list"] = recipe_df.apply(lambda x: clean_ingredients(x["ingredients_clean"]),
                                                    axis=1)
    recipe_df["num_ingredients"] = recipe_df.apply(lambda x: num_ingred(x["ingredients_list"]), axis=1)







