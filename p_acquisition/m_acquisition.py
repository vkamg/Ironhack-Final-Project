import pandas as pd

# acquisition functions

def acquire(path):
    recipe_df = pd.read_csv(path)
    return recipe_df