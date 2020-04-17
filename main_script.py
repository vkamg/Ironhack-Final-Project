import argparse
import pandas as pd
from p_acquisition.m_acquisition import acquire
from p_reporting.m_reporting import result
from p_wrangling.m_wrangling import clean_data



def main(path, ingred):
    data = acquire(path)
    data_cleaned = clean_data(data)
    result_df = result(data_cleaned, ingred)
    result_df.to_csv(f'./data/results/recipe_df.csv', index=False)
    output = print("Gracias por utilizar FastCooking")

    return output


if __name__ == '__main__':

    path = './data/raw/web_scraping_recipes_new.json'
    input_ingred = input('¿Qué tienes hoy en la nevera? ')
    main(path, input_ingred)