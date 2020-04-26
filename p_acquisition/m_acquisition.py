import pandas as pd

# acquisition functions

def acquire_lecturas(path):
    lecturas_df = pd.read_json(path)

    return lecturas_df


def acquire_recetasgratis(path):
    recetasgratis_df = pd.read_json(path)

    return recetasgratis_df