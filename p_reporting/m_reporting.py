import pandas as pd
import Levenshtein
import itertools
from fuzzywuzzy import fuzz
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


def fuzzy_columns(column, input_string):
    for ingred in input_string:
        dif = fuzz.token_set_ratio(column, ingred)
    if dif > 70:
        return True
    else:
        return False


def num_missing(recipe_ingred, active_ingred):
    missing_ingred = recipe_ingred - active_ingred
    return missing_ingred


def rating(match, missing):
    result = 0.75*match-0.25*missing
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
    input_ingred = input_list(input_ing)
    for ingred in input_ingred:
        recipe_df[ingred] = recipe_df.apply(lambda x: fuzzy_columns(x["ingredients_list"], ingred), axis=1)
    recipe_df["active_ingred"] = recipe_df.select_dtypes(include=['bool']).sum(axis=1)
    recipe_df["num_missing_ingred"] = recipe_df.apply(lambda x: num_missing(x["num_ingredients"],
                                                                                   x["active_ingred"]),
                                                      axis=1)
    recipe_df["recipe_rate"] = recipe_df.apply(lambda x: rating(x["active_ingred"], x["num_missing_ingred"]),
                                               axis=1)
    filter_principal = recipe_df['main_category'] == "principal"
    output = recipe_df[filter_principal].sort_values(by=['recipe_rate', 'num_missing_ingred'],
                                                        ascending=[False, True]).head(10)

    recipe_name = output["recipe_name"].iloc[0]
    num_missing_ingred = output['num_missing_ingred'].iloc[0]
    recipe_time = output["time_preparation(min)"].iloc[0]
    print(f"La mejor receta que puedes hacer con los ingredientes que has introducido es: {recipe_name}")
    print(f"Te faltan {num_missing_ingred} ingredientes")
    print(f"El tiempo de preparación es de {recipe_time} minutos")
    go_to_recipe = input('¿Quieres ir a la receta?')

    input_answer = normalize(go_to_recipe)

    if input_answer == 'si':
        recipe_link = output["recipe_url"].iloc[0]
        pop_recipe(recipe_link)
    elif input_answer == 'no':
        recipe_link = output["recipe_url"].iloc[0]
        print(f"Genial! Éste es el link por si quieres consultar la receta más tarde: {recipe_link}")
    else:
        print("Por favor, responde sí o no")

    return