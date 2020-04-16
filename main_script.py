import argparse
from selenium import webdriver
from p_acquisition.m_acquisition import acquire
from p_reporting.m_reporting import result
from p_wrangling.m_wrangling import clean_data
import time


def main(path, ingred):
    data = acquire(path)
    data_cleaned = clean_data(data)
    output = result(data_cleaned, ingred)
    recipe_name = output["recipe_name"].iloc[0]
    num_missing_ingred = output['num_missing_ingred'].iloc[0]
    recipe_time = output["time_preparation(min)"].iloc[0]
    print(f"La mejor receta que puedes hacer con los ingredientes que has introducido es: {recipe_name}")
    print(f"Te faltan {num_missing_ingred} ingredientes")
    print(f"El tiempo de preparación es de {recipe_time} minutos")
    go_to_recipe = input('¿Quieres ir a la receta?')

    def normalize(string):
        lower = string.lower()
        a, b = 'áéíóú', 'aeiou'
        trans = str.maketrans(a, b)
        result = lower.translate(trans)
        return result

    input_answer = normalize(go_to_recipe)

    if input_answer == 'si':
        # Opening the Chrome and going to the Web
        recipe_link = output["recipe_url"].iloc[0]
        chromedriver = "/home/veronica/Ironhack/Final Project/Chrome Driver/chromedriver"
        driver = webdriver.Chrome(chromedriver)
        driver.get(recipe_link)
        # Enabling cookies
        time.sleep(3)
        element = driver.find_elements_by_class_name('qc-cmp-button')
        element[1].click()
    elif input_answer == 'no':
        recipe_link = output["recipe_url"].iloc[0]
        print(f"Genial! Éste es el link por si quieres consultar la receta más tarde: {recipe_link}")
    else:
        print("Por favor, responde sí o no")



if __name__ == '__main__':

    path = './data/raw/web_scraping_recipes_new.json'
    input_ingred = input('¿Qué tienes hoy en la nevera?')
    main(path, input_ingred)