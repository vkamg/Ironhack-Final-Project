import argparse
import pandas as pd
from p_acquisition.acquisition_demo import acquire
from p_reporting.output_demo import result
import warnings


def main(path, ingred, intolerances, avoid):
    warnings.filterwarnings("ignore")
    data = acquire(path)
    result(data, ingred, intolerances, avoid)
    output = print("Gracias por utilizar ScrapChef")

    return output


if __name__ == '__main__':

    path = './data/processed/recipe_df_demo.csv'
    input_ingred = input('¿Qué tienes hoy en la nevera? ')
    input_intolerances = input('¿Tienes alguna intolerancia (gluten o lactosa)? ')
    input_avoid = input('¿Hay algún alimento que desees evitar? ')
    main(path, input_ingred, input_intolerances, input_avoid)