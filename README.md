# Final Ironhack Project


## Overview

*The goal of this project is create a recipe dataset using web scraping and then use that dataset in a script that, when you enter the ingredients you want to cook with, returns the recipe for which you have the fewest missing ingredients using most of the introduced ingredients.


## Results

**Input**

- The ingredients you want to use for cooking (whatever you have in your pantry or fridge, etc).
- Intolerances: You can select gluten free or lactose free recipes.
- If there is any food you do not want to cook with, you can also indicate it.

**Output**

- The script searches through more than 18,000 recipes and gives you back  the one where you use most of the ingredients you entered and for which you have the fewest missing ingredients. You can choose if you want to see the recipe at the time of the search (a page will open in your browser with the recipe) or if you want to see it later (the URL of the recipe will appear in the terminal for you to visit the page whenever you want)
  
## Data applied
  
Recipe data has been obtained through web scraping to two different recipes pages:
- https://www.lecturas.com/recetas
- https://www.recetasgratis.net/

## Procedure

  **1. Acquisition:** Create a database through data collected with web scraping.
  
  **2. Wrangling:** Data cleaning - Change the data type of the numeric columns (from object to integer or float),      Standardize the data format of each column, etc.
  
  **3. Analysis and Reporting:** Analyze the data to select the best recipes!


![Image](https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2019/08/29/15670724438459.jpg)

