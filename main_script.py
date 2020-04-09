import argparse

from p_acquisition.m_acquisition import acquire


def main():
    data = acquire('../data/raw/web_scraping_recipes.csv')




    return



if __name__ == '__main__':
    year = int(input('Enter the year: '))
    title = 'Top 10 Manufacturers by Fuel Efficiency ' + str(year)
    arguments = argument_parser()
    main(arguments)