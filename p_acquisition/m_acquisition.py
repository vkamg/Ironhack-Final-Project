import pandas as pd

# acquisition functions

def acquire(path):
    recipe_df = pd.read_json(path)
    return recipe_df