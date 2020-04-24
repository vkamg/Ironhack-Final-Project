import pandas as pd

# acquisition functions

def acquire(path):
    recipe_df = pd.read_csv(path)
    print("buscando la mejor receta...")

    return recipe_df