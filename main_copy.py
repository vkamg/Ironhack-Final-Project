import pandas as pd
import time

from p_reporting.output_copy import result


def main(path, ingred, intolerances, avoid):
    data = pd.read_csv(path)
    print("buscando la mejor receta...")
    time.sleep(60)
    result(data)
    output = print("Gracias por utilizar ScrapChef")

    return output


if __name__ == '__main__':

    path = './data/processed/df_demo.csv'
    input_ingred = input('¿Qué tienes hoy en la nevera? ')
    input_intolerances = input('¿Tienes alguna intolerancia (gluten o lactosa)? ')
    input_avoid = input('¿Hay algún alimento que desees evitar? ')
    main(path, input_ingred, input_intolerances, input_avoid)