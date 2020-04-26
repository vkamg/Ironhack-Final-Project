import pandas as pd
import re
from fuzzywuzzy import fuzz
import Levenshtein
from p_acquisition.m_acquisition import acquire_lecturas, acquire_recetasgratis


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
    elif re.search("Aperitivos y tapas", dish_str) != None:
        return "tapas"
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


def clean_receta(column):
    clean_string = re.sub("Recetas? de ", "", column)
    return (clean_string)

def main_category_clasification_recetasgratis(column):
    if column == "postres":
        return "postre"
    elif column == "pan y bollería":
        return "postre"
    elif column == "aperitivos y tapas":
        return "tapas"
    else:
        return "principal"


def object_tonumber_recetasgratis(column):
    if column == "missing":
        return None
    elif re.search("h", column) is not None:
        num_h = re.findall("(\d+)h", column)
        if re.search("m", column) is not None:
            num_min = re.findall("(\d+)m", column)
            total = int(num_h[0]) * 60 + int(num_min[0])
            return total
        else:
            total = int(num_h[0]) * 60
            return total
    else:
        object_split = column.split("m")
        result = int(object_split[0])
        return result


def gluten_free_recetasgratis(intolerances):
    if 'Receta sin gluten' in intolerances:
        return 1
    else:
        return 0


def egg_free_recetasgratis(intolerances):
    if 'Receta sin huevo' in intolerances:
        return 1
    else:
        return 0


def sucrose_fructose_free_recetasgratis(intolerances):
    if 'Receta sin azúcar' in intolerances:
        return 1
    else:
        return 0



def low_sodium_recetasgratis(intolerances):
    if 'Receta sin sal' in intolerances:
        return 1
    else:
        return 0


def lactose_free_recetasgratis(intolerances):
    if 'Receta sin lactosa' in intolerances:
        return 1
    else:
        return 0


def ingredients_tolist(ingred_column):
    ingredients_list = ingred_column.split("\n")
    return ingredients_list

def clean_ingredients_recetasgratis(ingred_column):
    ingredients_list = []
    for ing in ingred_column:
        if re.search("pechuga de", ing) != None:
            clean_ingred = re.sub("para.*$|\d(.*) |\d |\([^)]*\)| el peso de.*$| medi[a-z][a-z]?[a-z]? con.*$|yemas? de |claras? de |½ (.*) de |½ |¼ (.*) de |¼ ", "", ing)
            ingredients_list.append(clean_ingred)
        else:
            clean_ingred = re.sub("para.*$|\d(.*) de |\d |\([^)]*\)| el peso de.*$| medi[a-z][a-z]?[a-z]? con.*$|yemas? de |claras? de |½ (.*) de |½ |¼ (.*) de |¼ ", "", ing)
            ingredients_list.append(clean_ingred)
            if clean_ingred == "sal y pimienta":
                x = clean_ingred.split(" y ")
                ingredients_list.append(x[0])
                ingredients_list.append(x[1])
                ingredients_list.remove(clean_ingred)
            elif clean_ingred == "oliva":
                ingred_correct = "aceite de oliva"
                ingredients_list.append(ingred_correct)
                ingredients_list.remove(clean_ingred)
            elif clean_ingred == "agua":
                ingredients_list.remove(clean_ingred)
    ingredients_list = [i for i in ingredients_list if i]
    return ingredients_list


def clean_ingredients_2(column):
    new_list = []
    for i in column:
        try:
            huevo_ratio = fuzz.WRatio("huevo", i)
            if huevo_ratio >= 86:
                new_list.append("huevo")
            else:
                new_list.append(i)
        except:
            new_list.append(i)
    return new_list

def clean_ingredients_3(ingred_column):
    ingredients_list = []
    for ing in ingred_column:
        clean_ingred = re.sub(" ?unas hebras de |un tarro de |unas gotas de |un chorro de |lata |tzas |taza |cuchara sopera |c.c |una tacita de | ?mitad será ?| que se encuentre en la página| la necesaria|cucharadas |cdas | a temperatura ambiente|un poco de |cuadritos |una barra y cuarto de |cuadritos de |tbls ?|2 tipo cucharillas fritas ?|una nuez de |ud. ?| cortad[oa][s]? en.*| median[oa][s]?|  pequeñ[oa][s]?|  grand[s]?", "", ing)
        clean_ingred2 = re.sub("\d","", clean_ingred)
        ingredients_list.append(clean_ingred2)
    ingredients_list = [i for i in ingredients_list if i]
    return ingredients_list





def clean_data(path_lecturas, path_recetasgratis):

    print("cleaning data...")

    df_lecturas = acquire_lecturas(path_lecturas)

    df_lecturas["category"] = df_lecturas["category"].str.lower()

    df_lecturas["ingredients"] = df_lecturas.apply(lambda x: lowercase_ing(x["ingredients"]), axis=1)
    """recipe_df["ingredients_clean"] = recipe_df.apply(lambda x: normalize(x["ingredients"]), axis=1)"""

    df_lecturas.drop_duplicates(subset=["recipe_url", "category"], keep="first", inplace=True)
    df_lecturas = df_lecturas[df_lecturas.category != 'mermeladas y confituras']
    df_lecturas = df_lecturas[df_lecturas.category != 'salsas']
    df_lecturas["tipo_plato"] = df_lecturas.apply(lambda x: clean_more_info(x["more_info"]), axis=1)
    df_lecturas["main_category"] = df_lecturas.apply(lambda x: main_category_clasification(x["category"],
                                                                                       x["tipo_plato"]),
                                                 axis=1)
    df_lecturas['time_preparation'].fillna('missing', inplace=True)
    print("cleaning...3")
    df_lecturas['calories'].fillna('missing', inplace=True)
    df_lecturas["calories"] = df_lecturas.apply(lambda x: change_time_cal(x["time_preparation"], x["calories"]),
                                            axis=1)
    df_lecturas["time_preparation"] = df_lecturas.apply(lambda x: remove_cal_time(x["time_preparation"],
                                                                              x["calories"]), axis=1)
    df_lecturas["time_preparation(min)"] = df_lecturas.apply(lambda x: object_tonumber(x["time_preparation"]),
                                                         axis=1)
    df_lecturas["calories(kcal)"] = df_lecturas.apply(lambda x: object_tonumber(x["calories"]), axis=1)
    df_lecturas["gluten_free"] = df_lecturas.apply(lambda x: gluten_free(x["intolerances"]), axis=1)
    df_lecturas["lactose_free"] = df_lecturas.apply(lambda x: lactose_free(x["intolerances"]), axis=1)
    df_lecturas["egg_free"] = df_lecturas.apply(lambda x: egg_free(x["intolerances"]), axis=1)
    df_lecturas["sucrose_fructose_free"] = df_lecturas.apply(lambda x: sucrose_fructose_free(x["intolerances"]),
                                                         axis=1)
    df_lecturas["low_sodium"] = df_lecturas.apply(lambda x: low_sodium(x["intolerances"]), axis=1)
    print("cleaning...4")
    df_lecturas["ingredients_list"] = df_lecturas.apply(lambda x: clean_ingredients(x['ingredients']), axis=1)
    df_lecturas["num_ingredients"] = df_lecturas.apply(lambda x: num_ingred(x["ingredients_list"]),
                                                   axis=1)
    df_lecturas = df_lecturas[['recipe_image_url', 'recipe_name', 'recipe_url', 'ingredients_list',
                           'time_preparation(min)', 'gluten_free', 'egg_free',
                           'sucrose_fructose_free', 'low_sodium', 'lactose_free',
                           'main_category', 'num_ingredients']]
    df_lecturas.reset_index(drop=True, inplace=True)

    df_recetasgratis = acquire_recetasgratis(path_recetasgratis)

    df_recetasgratis["ingredients"] = df_recetasgratis["ingredients"].str.lower()
    df_recetasgratis.drop_duplicates(subset=["recipe_url", "category"],
                              keep="first", inplace=True)

    df_recetasgratis["recipe_name"] = df_recetasgratis.apply(lambda x: clean_receta(x['recipe_name']), axis=1)

    df_recetasgratis["category"] = df_recetasgratis.apply(lambda x: clean_receta(x['category']), axis=1)

    df_recetasgratis["category"] = df_recetasgratis["category"].str.lower()

    df_recetasgratis["main_category"] = df_recetasgratis.apply(lambda x: main_category_clasification_recetasgratis(x["category"]),
                                                 axis=1)
    df_recetasgratis['time_preparation'].fillna('missing', inplace=True)

    df_recetasgratis["time_preparation(min)"] = df_recetasgratis.apply(lambda x: object_tonumber_recetasgratis(x["time_preparation"]),
                                                         axis=1)

    df_recetasgratis["gluten_free"] = df_recetasgratis.apply(lambda x: gluten_free_recetasgratis(x["more_info"]),
                                               axis=1)
    df_recetasgratis["egg_free"] = df_recetasgratis.apply(lambda x: egg_free_recetasgratis(x["more_info"]), axis=1)

    df_recetasgratis["sucrose_fructose_free"] = df_recetasgratis.apply(lambda x: sucrose_fructose_free_recetasgratis(x["more_info"]),
                                                         axis=1)
    df_recetasgratis["low_sodium"] = df_recetasgratis.apply(lambda x: low_sodium_recetasgratis(x["more_info"]), axis=1)

    df_recetasgratis["lactose_free"] = df_recetasgratis.apply(lambda x: lactose_free_recetasgratis(x["more_info"]),
                                                axis=1)

    df_recetasgratis["ingredients_list"] = df_recetasgratis.apply(lambda x: ingredients_tolist(x['ingredients']),
                                                    axis=1)

    df_recetasgratis["ingredients_list"] = df_recetasgratis.apply(lambda x: clean_ingredients(x['ingredients_list']),
                                                    axis=1)

    df_recetasgratis["num_ingredients"] = df_recetasgratis.apply(lambda x: num_ingred(x["ingredients_list"]),
                                                   axis=1)

    df_recetasgratis = df_recetasgratis[['recipe_image_url', 'recipe_name', 'recipe_url', 'ingredients_list',
                           'time_preparation(min)', 'gluten_free', 'egg_free',
                           'sucrose_fructose_free', 'low_sodium', 'lactose_free',
                           'main_category', 'num_ingredients']]

    recipe_df = pd.concat([df_lecturas, df_recetasgratis], ignore_index=True)

    recipe_df["ingredients_list"] = recipe_df.apply(lambda x: clean_ingredients_2(x["ingredients_list"]),
                                                    axis=1)

    recipe_df["ingredients_list"] = recipe_df.apply(lambda x: clean_ingredients_3(x["ingredients_list"]),
                                                    axis=1)

    recipe_df.to_csv(f'../data/processed/recipe_df_demo.csv', index=False)

    ok_cleaning = "data cleaned"

    return ok_cleaning


if __name__ == '__main__':

    path_lecturas = './data/raw/web_scraping_recipes_new.json'
    path_recetasgratis = './data/raw/web_scraping_recipes_recetasgratis.json'
    clean_data(path_lecturas, path_recetasgratis)




