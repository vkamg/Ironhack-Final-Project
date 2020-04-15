import pandas as pd
import re
import ast

# wrangling functions

def lowercase_ing(column):
    ingredients_list = []
    for ing in column:
        result = ing.lower()
        ingredients_list.append(result)
    return ingredients_list


def clean_more_info(list_x):
    if "Tipo Plato:" in list_x:
        i = list_x.index("Tipo Plato:")
        i2 = list_x.index("Precio:")
        result = list_x[(i+1):i2]
        return result
    else:
        return None


def main_category_clasification(cat_column, dish_column):
    dish_str = str(dish_column)
    if re.search("Postres", dish_str) != None:
        return "postre"
    elif cat_column == "postres y dulces":
        return "postre"
    else:
        return "principal"


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
    ingredients_list = []
    for ing in ingred_column:
        clean_ingred = re.sub(" para.*$", "", ing)
        ingredients_list.append(clean_ingred)
    return ingredients_list


def num_ingred(column):
    return len(column)


def clean_data(recipe_df):
    print("cleaning...")
    recipe_df["category"] = recipe_df["category"].str.lower()
    print("cleaning...1")
    recipe_df["ingredients"] = recipe_df.apply(lambda x: lowercase_ing(x["ingredients"]), axis=1)
    """recipe_df["ingredients_clean"] = recipe_df.apply(lambda x: normalize(x["ingredients"]), axis=1)"""
    print("cleaning...2")
    recipe_df.drop_duplicates(subset=["recipe_url", "category"], keep="first", inplace=True)
    recipe_df = recipe_df[recipe_df.category != 'mermeladas y confituras']
    recipe_df = recipe_df[recipe_df.category != 'salsas']
    recipe_df["tipo_plato"] = recipe_df.apply(lambda x: clean_more_info(x["more_info"]), axis=1)
    recipe_df["main_category"] = recipe_df.apply(lambda x: main_category_clasification(x["category"],
                                                                                       x["tipo_plato"]),
                                                 axis=1)
    recipe_df['time_preparation'].fillna('missing', inplace=True)
    print("cleaning...3")
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
    print("cleaning...4")
    recipe_df["ingredients_list"] = recipe_df.apply(lambda x: clean_ingredients(x['ingredients']), axis=1)
    ingredients_df = recipe_df.ingredients_list.apply(pd.Series) \
        .merge(recipe_df, right_index=True, left_index=True) \
        .melt(id_vars=['recipe_name', 'ingredients', 'ingred_quantity', 'time_preparation',
                       'calories', 'intolerances', 'recipe_url', 'recipe_image_url',
                       'category', 'more_info', 'recipe_steps', 'tipo_plato', 'main_category',
                       'time_preparation(min)', 'calories(kcal)', 'gluten_free', 'egg_free',
                       'sucrose_fructose_free', 'low_sodium', 'lactose_free',
                       'ingredients_list'], value_name="ingredient")
    print("cleaning...5")
    ingredients_df = ingredients_df[ingredients_df['ingredient'].notna()]
    ingredients_df["num_ingredients"] = ingredients_df.apply(lambda x: num_ingred(x["ingredients_list"]),
                                                             axis=1)
    print("cleaning...6")
    ingredients_df = ingredients_df[['recipe_name', 'recipe_url', 'ingredient', 'variable', 'num_ingredients',
                                     'category', 'main_category', 'tipo_plato', 'time_preparation(min)',
                                     'calories(kcal)', 'gluten_free', 'egg_free',
                                     'sucrose_fructose_free', 'low_sodium', 'lactose_free', ]]
    print("cleaning...7")
    ingredients_df.reset_index(drop=True, inplace=True)

    return ingredients_df







