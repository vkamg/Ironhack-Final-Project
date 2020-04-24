import webbrowser

def normalize(string):
    lower = string.lower()
    a, b = 'áéíóú', 'aeiou'
    trans = str.maketrans(a, b)
    result = lower.translate(trans)
    return result


def pop_recipe(url_):
    ROUTE = url_
    webbrowser.open_new(ROUTE)



def result(data):
    recipe_name = data["recipe_name"].iloc[0]
    num_missing_ingred = data['num_missing_ingred'].iloc[0]
    recipe_time = data["time_preparation(min)"].iloc[0]
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
        recipe_link = data["recipe_url"].iloc[0]
        pop_recipe(recipe_link)
    elif input_answer == 'no':
        recipe_link = data["recipe_url"].iloc[0]
        print(f"Genial! Éste es el link por si quieres consultar la receta más tarde: {recipe_link}")
    else:
        print("Por favor, responde sí o no")