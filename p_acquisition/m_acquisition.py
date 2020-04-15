import pandas as pd

# acquisition functions

def acquire(path):
    print("charging json file...")
    recipe_df = pd.read_json(path)

    return recipe_df