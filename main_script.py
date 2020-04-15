import argparse

from p_acquisition.m_acquisition import acquire
from p_wrangling.m_wrangling import clean_data


def main(path):
    data = acquire(path)
    data_cleaned = clean_data(data)
    data_cleaned.to_csv(f'./data/processed/ingredients_df_pycharm.csv', index=False)
    ok = print("script working :)")
    return ok



if __name__ == '__main__':

    path = './data/raw/web_scraping_recipes_new.json'
    main(path)