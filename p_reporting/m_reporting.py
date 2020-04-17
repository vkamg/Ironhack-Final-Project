import pandas as pd
import Levenshtein
import itertools
from fuzzywuzzy import process, fuzz
import webbrowser
import ast
from selenium import webdriver
import time

# reporting functions

def input_list(string):
    input_list = []
    str_split = string.split(", ")
    for x in str_split:
        input_list.append(x)
    return input_list


def matched(recipe_ingred, input_ingred):
    new_list = []
    for element in input_ingred:
        try:
            best_match = process.extract(element, recipe_ingred, scorer=fuzz.WRatio, limit=1)
            if best_match[0][1] >= 80:
                recipe_ingred.remove(best_match[0][0])
                new_list.append(best_match[0][0])
            else:
                pass
        except:
            pass
    return new_list


def num_ingred(column):
    return len(column)

def fuzzy_columns(column, input_string):
    best_match = process.extract(input_string, column, scorer=fuzz.WRatio, limit=1)
    ratio = best_match[0][1]
    if ratio > 80:
        return True
    else:
        return False

def fuzzy_analysis(column, input_string):
    dif = fuzz.token_set_ratio(column, input_string)
    return dif

def num_missing(recipe_ingred, active_ingred):
    missing_ingred = recipe_ingred - active_ingred
    return missing_ingred


def rating(match, missing):
    result = 0.50*match-0.50*missing
    return result

def normalize(string):
    lower = string.lower()
    a, b = 'áéíóú', 'aeiou'
    trans = str.maketrans(a, b)
    result = lower.translate(trans)
    return result


def pop_recipe(url_):
    ROUTE = url_
    webbrowser.open_new(ROUTE)



def result(recipe_df, input_ing):

    recipe_df["input"] = input_ing
    recipe_df["input"] = recipe_df.apply(lambda x: input_list(x["input"]), axis=1)

    """for ingred in input_ingred:
        recipe_df[ingred] = recipe_df.apply(lambda x: fuzzy_columns(x["ingredients_list"], ingred), axis=1)"""
    """recipe_df["active_ingred"] = recipe_df.select_dtypes(include=['bool']).sum(axis=1)"""

    recipe_df["matched_ingred"] = recipe_df.apply(lambda x: matched(x["ingredients_list"], x["input"])
                                                  , axis=1)

    recipe_df["num_matched"] = recipe_df.apply(lambda x: num_ingred(x["matched_ingred"]), axis=1)

    recipe_df["num_missing_ingred"] = recipe_df.apply(lambda x: num_missing(x["num_ingredients"],
                                                                                   x["num_matched"]),
                                                      axis=1)
    recipe_df["recipe_rate"] = recipe_df.apply(lambda x: rating(x["num_matched"], x["num_missing_ingred"]),
                                               axis=1)
    filter_principal = recipe_df['main_category'] == "principal"
    output = recipe_df[filter_principal].sort_values(by=["recipe_rate", "num_missing_ingred"],
                                                        ascending=[False, True]).head(10)

    """analysis_df = recipe_df.ingredients_list.apply(pd.Series) \
    .merge(recipe_df, right_index = True, left_index = True) \
    .melt(id_vars = ['recipe_image_url', 'recipe_name', 'recipe_url', 'ingredients_list',
       'time_preparation(min)', 'calories(kcal)', 'gluten_free', 'egg_free',
       'sucrose_fructose_free', 'low_sodium', 'lactose_free', 'tipo_plato',
       'main_category', 'category', 'num_ingredients', 'huevos',
       'pechiga de pollo', 'lentejas', 'pimiento', 'arroz', 'leche',
       'mantequilla', 'harina', 'sal', 'azúcar', 'aceite', 'zanahorias',
       'queso', 'bacon', 'active_ingred', 'num_missing_ingred', 'recipe_rate'], value_name = "ingredient")

    analysis_df = analysis_df[analysis_df['ingredient'].notna()]
    analysis_df.reset_index(drop=True, inplace=True)

    for ingred in input_ingred:
        analysis_df[ingred] = analysis_df.apply(lambda x: fuzzy_analysis(x["ingredient"], ingred), axis=1)

    analysis_df.to_csv(f'./data/results/pycharm_result_analysis.csv', index=False)"""



    recipe_name = output["recipe_name"].iloc[0]
    num_missing_ingred = output['num_missing_ingred'].iloc[0]
    recipe_time = output["time_preparation(min)"].iloc[0]
    print(f"La mejor receta que puedes hacer con los ingredientes que has introducido es: {recipe_name}")
    print(f"Te faltan {num_missing_ingred} ingredientes")
    print(f"El tiempo de preparación es de {recipe_time} minutos")
    go_to_recipe = input('¿Quieres ir a la receta ?')

    input_answer = normalize(go_to_recipe)

    if input_answer == 'si':
        recipe_link = output["recipe_url"].iloc[0]
        pop_recipe(recipe_link)
    elif input_answer == 'no':
        recipe_link = output["recipe_url"].iloc[0]
        print(f"Genial! Éste es el link por si quieres consultar la receta más tarde: {recipe_link}")
    else:
        print("Por favor, responde sí o no")

    return output