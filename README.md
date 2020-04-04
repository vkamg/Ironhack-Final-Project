# Final Ironhack Project


## Overview

*The goal of this project is to create a program that, when you enter the ingredients you want to cook with, returns the recipes for which you are missing the fewest ingredients and the quickest to prepare


## Results

**Input**

- The ingredients you want to use for cooking (whatever you have in your pantry or fridge, etc).
- Intolerances: You can select gluten free or lactose free recipes.
- If there is any food you do not want to cook with, you can also indicate it.

**Output**

The URL with three best recipes you can make with the input entered, sorted by:
1. Those for which you are missing fewer ingredients.
2. Those for which the preparation time is shorter.
  
## Data applied
  
Recipe data has been obtained through web scraping to a recipe page
- https://www.lecturas.com/recetas

## Procedure

  **1. Acquisition:** Create a database through data collected with web scraping.
  
  **2. Wrangling:** Data cleaning - Change the data type of the numeric columns (from object to integer or float),      Standardize the data format of each column, etc.
  
  **3. Analysis and Reporting:** Analyze the data to select the best recipes!


![Image](https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2019/08/29/15670724438459.jpg)

---


## **Suggested Structure:**

### :raising_hand: **Name** 
Self-explanatory names are best. If the name sounds too vague or unrelated, it may be a signal to move on. It also must be catchy. Images, Logo, Gif or some color is strongly recommended.

### :baby: **Status**
Alpha, Beta, 1.1, Ironhack Data Analytics Final Project, etc... It's OK to write a sentence, too. The goal is to let interested people know where this project is at.

### :running: **One-liner**
Having a one-liner that describes the pipeline/api/app is useful for getting an idea of what your code does in slightly greater detail. 

### :computer: **Technology stack**
Python, Pandas, Scipy, Scikit-learn, etc. Indicate the technological nature of the software, including primary programming language(s), main libraries and whether the software is intended as standalone or as a module in a framework or other ecosystem.

### :boom: **Core technical concepts and inspiration**
Why does it exist? Frame your project for the potential user. Compare/contrast your project with other, similar projects so the user knows how it is different from those projects. Highlight the technical concepts that your project demonstrates or supports. Keep it very brief.

### :wrench: **Configuration**
Requeriments, prerequisites, dependencies, installation instructions.

### :see_no_evil: **Usage**
Parameters, return values, known issues, thrown errors.

### :file_folder: **Folder structure**
```
└── project
    ├── __trash__
    ├── .gitignore
    ├── .env
    ├── requeriments.txt
    ├── README.md
    ├── main_script.py
    ├── notebooks
    │   ├── notebook1.ipynb
    │   └── notebook2.ipynb
    ├── package1
    │   ├── module1.py
    │   └── module2.py
    └── data
        ├── raw
        ├── processed
        └── results
```

> Do not forget to include `__trash__` and `.env` in `.gitignore` 

### :shit: **ToDo**
Next steps, features planned, known bugs (shortlist).

### :information_source: **Further info**
Credits, alternatives, references, license.

### :love_letter: **Contact info*
Getting help, getting involved, hire me please.
