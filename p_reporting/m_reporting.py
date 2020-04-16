import pandas as pd
import Levenshtein
import itertools
from fuzzywuzzy import fuzz
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


def num_missing_ingred(recipe_ingred, active_ingred):
    missing_ingred = recipe_ingred - active_ingred
    return missing_ingred


def rating(match, missing):
    result = 0.75*match-0.25*missing
    return result



def result(recipe_df, input_ing):
    input_ingred = input_list(input_ing)
    for ingred in input_ingred:
        recipe_df[ingred] = recipe_df.apply(lambda x: fuzzy_columns(x["ingredients_list"], ingred), axis=1)
    recipe_df["active_ingred"] = recipe_df.select_dtypes(include=['bool']).sum(axis=1)
    recipe_df["num_missing_ingred"] = recipe_df.apply(lambda x: num_missing_ingred(x["num_ingredients"],
                                                                                   x["active_ingred"]),
                                                      axis=1)
    recipe_df["recipe_rate"] = recipe_df.apply(lambda x: rating(x["active_ingred"], x["num_missing_ingred"]),
                                               axis=1)
    filter_principal = recipe_df['main_category'] == "principal"
    output_df = recipe_df[filter_principal].sort_values(by=['recipe_rate'], ascending=False).head(3)
    return output_df