import Levenshtein
from fuzzywuzzy import process, fuzz
import webbrowser
import ast

def input_list(string):
    input_list = []
    str_split = string.split(", ")
    for x in str_split:
        input_list.append(x)
    return input_list


def ingred_list(column):
    ingred_list = ast.literal_eval(column)
    return ingred_list


def matched_avoid(ingred_list, input_ingred):
    new_list = []
    for element in input_ingred:
        try:
            best_match = process.extract(element, ingred_list, scorer=fuzz.WRatio, limit=1)
            if element == "sal" or element == "harina" or element == "azúcar" or element == "pimienta":
                if best_match[0][1] >= 90:
                    ingred_list.remove(best_match[0][0])
                    new_list.append(best_match[0][0])
            elif element == "harina":
                if best_match[0][1] >= 90:
                    ingred_list.remove(best_match[0][0])
                    new_list.append(best_match[0][0])
            elif element == "azúcar":
                 if best_match[0][1] >= 90:
                    ingred_list.remove(best_match[0][0])
                    new_list.append(best_match[0][0])
            elif element == "pimienta":
                if best_match[0][1] >= 90:
                    ingred_list.remove(best_match[0][0])
                    new_list.append(best_match[0][0])
            else:
                if best_match[0][1] >= 86:
                    ingred_list.remove(best_match[0][0])
                    new_list.append(best_match[0][0])
        except:
            pass
    return len(new_list)


def matched(ingred_list, input_ingred):
    new_list = []
    for element in input_ingred:
        try:
            best_match = process.extract(element, ingred_list, scorer=fuzz.WRatio, limit=1)
            if element == "sal" or element == "harina" or element == "azúcar" or element == "pimienta":
                if best_match[0][1] >= 90:
                    ingred_list.remove(best_match[0][0])
                    new_list.append(best_match[0][0])
            elif element == "harina":
                if best_match[0][1] >= 90:
                    ingred_list.remove(best_match[0][0])
                    new_list.append(best_match[0][0])
            elif element == "azúcar":
                 if best_match[0][1] >= 90:
                    ingred_list.remove(best_match[0][0])
                    new_list.append(best_match[0][0])
            elif element == "pimienta":
                if best_match[0][1] >= 90:
                    ingred_list.remove(best_match[0][0])
                    new_list.append(best_match[0][0])
            else:
                if best_match[0][1] >= 86:
                    ingred_list.remove(best_match[0][0])
                    new_list.append(best_match[0][0])
        except:
            pass
    return new_list


def num_ingred(column):
    return len(column)

def num_missing(recipe_ingred, active_ingred):
    missing_ingred = recipe_ingred - active_ingred
    return missing_ingred

def missing_ing(matched, ingred_list):
    missing_list = []
    for i in ingred_list:
        if i in matched:
            pass
        else:
            missing_list.append(i)
    return missing_list

def rating(match, missing):
    result = 0.70*match-0.30*missing
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




def result(df, input_ing, intolerance, avoid):

    filter_principal = df['main_category'] == "principal"
    df_clean = df[filter_principal]
    df_clean["ingredients"] = df_clean.apply(lambda x: ingred_list(x["ingredients_list"]), axis=1)
    df_clean["input_string"] = input_ing
    df_clean["input"] = df_clean.apply(lambda x: input_list(x["input_string"]), axis=1)
    if avoid == "no":
        pass
    else:
        df_clean["input_avoid"] = avoid
        df_clean["avoid"] = df_clean.apply(lambda x: input_list(x["input_avoid"]), axis=1)
        df_clean["avoid_match"] = df_clean.apply(lambda x: matched_avoid(x["ingredients"],
                                                                           x["avoid"]), axis=1)
        filter_avoid = df_clean["avoid_match"] == 0
        recipe_df = df_clean[filter_avoid]

    recipe_df["matched_ingred"] = recipe_df.apply(lambda x: matched(x["ingredients"], x["input"])
                                                  , axis=1)

    recipe_df["num_matched"] = recipe_df.apply(lambda x: num_ingred(x["matched_ingred"]), axis=1)

    recipe_df["num_missing_ingred"] = recipe_df.apply(lambda x: num_missing(x["num_ingredients"],
                                                                            x["num_matched"]), axis=1)

    recipe_df["missing_ingred"] = recipe_df.apply(lambda x: missing_ing(x["matched_ingred"],
                                                                        x["ingredients_list"]), axis=1)

    recipe_df["recipe_rate"] = recipe_df.apply(lambda x: rating(x["num_matched"], x["num_missing_ingred"]),
                                               axis=1)


    output = recipe_df.sort_values(by=["recipe_rate", "num_missing_ingred"],
                                                       ascending=[False, True]).head(10)

    recipe_name = output["recipe_name"].iloc[0]
    num_missing_ingred = output['num_missing_ingred'].iloc[0]
    recipe_time = output["time_preparation(min)"].iloc[0]
    print(f"La mejor receta que puedes hacer con los ingredientes que has introducido es: {recipe_name}")
    if num_missing_ingred != 0:
        print(f"Te faltan {num_missing_ingred} ingredientes")
    else:
        print("Genial! No te falta ningún ingrediente!")
    if recipe_time != None:
        print(f"El tiempo de preparación es de {recipe_time} minutos")
    else:
        pass
    go_to_recipe = input('¿Quieres ir a la receta? ')

    input_answer = normalize(go_to_recipe)

    if input_answer == 'si':
        recipe_link = output["recipe_url"].iloc[0]
        pop_recipe(recipe_link)
    elif input_answer == 'no':
        recipe_link = output["recipe_url"].iloc[0]
        print(f"Genial! Éste es el link por si quieres consultar la receta más tarde: {recipe_link}")
    else:
        print("Por favor, responde sí o no")





    """for ingred in input_ingred:
        recipe_df[ingred] = recipe_df.apply(lambda x: fuzzy_columns(x["ingredients_list"], ingred), axis=1)"""
    """recipe_df["active_ingred"] = recipe_df.select_dtypes(include=['bool']).sum(axis=1)

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

    recipe_name = output["recipe_name"].iloc[0]
    num_missing_ingred = output['num_missing_ingred'].iloc[0]
    recipe_time = output["time_preparation(min)"].iloc[0]
    print(f"La mejor receta que puedes hacer con los ingredientes que has introducido es: {recipe_name}")
    print(f"Te faltan {num_missing_ingred} ingredientes")
    print(f"El tiempo de preparación es de {recipe_time} minutos")
    go_to_recipe = input('¿Quieres ir a la receta? ')

    input_answer = normalize(go_to_recipe)

    if input_answer == 'si':
        recipe_link = output["recipe_url"].iloc[0]
        pop_recipe(recipe_link)
    elif input_answer == 'no':
        recipe_link = output["recipe_url"].iloc[0]
        print(f"Genial! Éste es el link por si quieres consultar la receta más tarde: {recipe_link}")
    else:
        print("Por favor, responde sí o no")"""


