from selenium import webdriver
import time
import numpy as np
import json


def web_scraping(link):
    # Opening the Chrome and going to the Web
    chromedriver = "/home/veronica/Ironhack/Final Project/Chrome Driver/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    driver.get(link)
    # Enabling cookies
    time.sleep(3)
    element = driver.find_elements_by_class_name('qc-cmp-button')
    element[1].click()
    # Looping throught the categories
    time.sleep(3)
    categories = driver.find_elements_by_tag_name('h4')
    recipes_list = []
    driver.set_page_load_timeout(10)

    for x in np.arange(len(categories) - 1):
        time.sleep(3)
        categories = driver.find_elements_by_tag_name('h4')
        category = categories[x].text
        try:
            categories = driver.find_elements_by_tag_name('h4')
            driver.execute_script("arguments[0].click()", categories[x])
            time.sleep(2)
            while True:
                next_page_btn = driver.find_elements_by_class_name('next')
                if len(next_page_btn) < 1:
                    recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                    for x in np.arange(len(recipe_sumup_scrap) - 1):
                        recipe_dict = {}
                        time.sleep(2)
                        recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                        driver.execute_script("arguments[0].click()", recipe_sumup_scrap[x])
                        time.sleep(3)
                        # recipe name
                        recipe_dict["recipe_name"] = driver.find_element_by_tag_name('h1').text
                        # ingredients
                        ingredients_list = []
                        recipe_ingred = driver.find_elements_by_tag_name('td')
                        for x in np.arange(len(recipe_ingred)):
                            if x % 2 != 0:
                                ingredients_list.append(recipe_ingred[x].text)
                            else:
                                pass
                        recipe_dict["ingredients"] = ingredients_list
                        # time_preparation and calories
                        time_calor_scrap = driver.find_elements_by_class_name("metaheader-value")
                        try:
                            recipe_dict["time_preparation"] = time_calor_scrap[1].text
                        except:
                            pass
                        # calories
                        try:
                            recipe_dict["calories"] = time_calor_scrap[2].text
                        except:
                            pass
                        # intolerances
                        try:
                            intolerances = driver.find_elements_by_class_name("intolerances-item")
                            intolerances_list = [intolerance.text for intolerance in intolerances]
                            recipe_dict["intolerances"] = intolerances_list
                        except:
                            recipe_dict["intolerances"] = None
                        # recipe_url
                        recipe_dict["recipe_url"] = driver.current_url
                        # images_url
                        images = driver.find_elements_by_tag_name('img')
                        images_list = [image.get_attribute('src') for image in images]
                        recipe_image_url = images_list[1]
                        recipe_dict["recipe_image_url"] = recipe_image_url
                        # category
                        recipe_dict["category"] = category
                        # recipe_list append
                        recipes_list.append(recipe_dict)
                        driver.back()
                        time.sleep(2)
                    print(f'{category} finished')
                    break
                else:
                    recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                    for x in np.arange(len(recipe_sumup_scrap) - 1):
                        recipe_dict = {}
                        time.sleep(2)
                        recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                        driver.execute_script("arguments[0].click()", recipe_sumup_scrap[x])
                        time.sleep(3)
                        # recipe name
                        recipe_dict["recipe_name"] = driver.find_element_by_tag_name('h1').text
                        # ingredients
                        ingredients_list = []
                        recipe_ingred = driver.find_elements_by_tag_name('td')
                        for x in np.arange(len(recipe_ingred)):
                            if x % 2 != 0:
                                ingredients_list.append(recipe_ingred[x].text)
                            else:
                                pass
                        recipe_dict["ingredients"] = ingredients_list
                        # time_preparation and calories
                        time_calor_scrap = driver.find_elements_by_class_name("metaheader-value")
                        try:
                            recipe_dict["time_preparation"] = time_calor_scrap[1].text
                        except:
                            pass
                        # calories
                        try:
                            recipe_dict["calories"] = time_calor_scrap[2].text
                        except:
                            pass
                        # intolerances
                        try:
                            intolerances = driver.find_elements_by_class_name("intolerances-item")
                            intolerances_list = [intolerance.text for intolerance in intolerances]
                            recipe_dict["intolerances"] = intolerances_list
                        except:
                            recipe_dict["intolerances"] = None
                        # recipe_url
                        recipe_dict["recipe_url"] = driver.current_url
                        # images_url
                        images = driver.find_elements_by_tag_name('img')
                        images_list = [image.get_attribute('src') for image in images]
                        recipe_image_url = images_list[1]
                        recipe_dict["recipe_image_url"] = recipe_image_url
                        # category
                        recipe_dict["category"] = category
                        # recipe_list append
                        recipes_list.append(recipe_dict)
                        driver.back()
                        time.sleep(2)
                    next_page_btn = driver.find_elements_by_css_selector(".next [href]")
                    driver.execute_script("arguments[0].click()", next_page_btn[0])
                    time.sleep(2)
            main_page = driver.find_elements_by_css_selector(".left [href]")
            driver.execute_script("arguments[0].click()", main_page[1])
            time.sleep(2)
        except:
            current_link = driver.current_url
            fail_link = "https://www.lecturas.com/recetas/postres-dulces?_page=15"
            if current_link == fail_link:
                next_page = "https://www.lecturas.com/recetas/postres-dulces?_page=16"
                driver.get(next_page)
                driver.set_page_load_timeout(10)
                while True:
                    next_page_btn = driver.find_elements_by_class_name('next')
                    if len(next_page_btn) < 1:
                        recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                        for x in np.arange(len(recipe_sumup_scrap) - 1):
                            recipe_dict = {}
                            time.sleep(2)
                            recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                            driver.execute_script("arguments[0].click()", recipe_sumup_scrap[x])
                            time.sleep(3)
                            # recipe name
                            recipe_dict["recipe_name"] = driver.find_element_by_tag_name('h1').text
                            # ingredients
                            ingredients_list = []
                            recipe_ingred = driver.find_elements_by_tag_name('td')
                            for x in np.arange(len(recipe_ingred)):
                                if x % 2 != 0:
                                    ingredients_list.append(recipe_ingred[x].text)
                                else:
                                    pass
                            recipe_dict["ingredients"] = ingredients_list
                            # time_preparation and calories
                            time_calor_scrap = driver.find_elements_by_class_name("metaheader-value")
                            try:
                                recipe_dict["time_preparation"] = time_calor_scrap[1].text
                            except:
                                pass
                            # calories
                            try:
                                recipe_dict["calories"] = time_calor_scrap[2].text
                            except:
                                pass
                            # intolerances
                            try:
                                intolerances = driver.find_elements_by_class_name("intolerances-item")
                                intolerances_list = [intolerance.text for intolerance in intolerances]
                                recipe_dict["intolerances"] = intolerances_list
                            except:
                                recipe_dict["intolerances"] = None
                            # recipe_url
                            recipe_dict["recipe_url"] = driver.current_url
                            # images_url
                            images = driver.find_elements_by_tag_name('img')
                            images_list = [image.get_attribute('src') for image in images]
                            recipe_image_url = images_list[1]
                            recipe_dict["recipe_image_url"] = recipe_image_url
                            # category
                            recipe_dict["category"] = category
                            # recipe_list append
                            recipes_list.append(recipe_dict)
                            driver.back()
                            time.sleep(2)
                        print(f'{category} finished')
                        break
                    else:
                        recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                        for x in np.arange(len(recipe_sumup_scrap) - 1):
                            recipe_dict = {}
                            time.sleep(2)
                            recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                            driver.execute_script("arguments[0].click()", recipe_sumup_scrap[x])
                            time.sleep(3)
                            # recipe name
                            recipe_dict["recipe_name"] = driver.find_element_by_tag_name('h1').text
                            # ingredients
                            ingredients_list = []
                            recipe_ingred = driver.find_elements_by_tag_name('td')
                            for x in np.arange(len(recipe_ingred)):
                                if x % 2 != 0:
                                    ingredients_list.append(recipe_ingred[x].text)
                                else:
                                    pass
                            recipe_dict["ingredients"] = ingredients_list
                            # time_preparation and calories
                            time_calor_scrap = driver.find_elements_by_class_name("metaheader-value")
                            try:
                                recipe_dict["time_preparation"] = time_calor_scrap[1].text
                            except:
                                pass
                            # calories
                            try:
                                recipe_dict["calories"] = time_calor_scrap[2].text
                            except:
                                pass
                            # intolerances
                            try:
                                intolerances = driver.find_elements_by_class_name("intolerances-item")
                                intolerances_list = [intolerance.text for intolerance in intolerances]
                                recipe_dict["intolerances"] = intolerances_list
                            except:
                                recipe_dict["intolerances"] = None
                            # recipe_url
                            recipe_dict["recipe_url"] = driver.current_url
                            # images_url
                            images = driver.find_elements_by_tag_name('img')
                            images_list = [image.get_attribute('src') for image in images]
                            recipe_image_url = images_list[1]
                            recipe_dict["recipe_image_url"] = recipe_image_url
                            # category
                            recipe_dict["category"] = category
                            # recipe_list append
                            recipes_list.append(recipe_dict)
                            driver.back()
                            time.sleep(2)
                        next_page_btn = driver.find_elements_by_css_selector(".next [href]")
                        driver.execute_script("arguments[0].click()", next_page_btn[0])
                        time.sleep(2)
                main_page = driver.find_elements_by_css_selector(".left [href]")
                driver.execute_script("arguments[0].click()", main_page[1])
                time.sleep(2)

            else:
                current_link = driver.current_url
                print(f"TimeoutError at {current_link}")
                driver.get(current_link)
                driver.set_page_load_timeout(10)
                try:
                    while True:
                        next_page_btn = driver.find_elements_by_class_name('next')
                        if len(next_page_btn) < 1:
                            recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                            for x in np.arange(len(recipe_sumup_scrap) - 1):
                                recipe_dict = {}
                                time.sleep(2)
                                recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                                driver.execute_script("arguments[0].click()", recipe_sumup_scrap[x])
                                time.sleep(3)
                                # recipe name
                                recipe_dict["recipe_name"] = driver.find_element_by_tag_name('h1').text
                                # ingredients
                                ingredients_list = []
                                recipe_ingred = driver.find_elements_by_tag_name('td')
                                for x in np.arange(len(recipe_ingred)):
                                    if x % 2 != 0:
                                        ingredients_list.append(recipe_ingred[x].text)
                                    else:
                                        pass
                                recipe_dict["ingredients"] = ingredients_list
                                # time_preparation and calories
                                time_calor_scrap = driver.find_elements_by_class_name("metaheader-value")
                                try:
                                    recipe_dict["time_preparation"] = time_calor_scrap[1].text
                                except:
                                    pass
                                # calories
                                try:
                                    recipe_dict["calories"] = time_calor_scrap[2].text
                                except:
                                    pass
                                # intolerances
                                try:
                                    intolerances = driver.find_elements_by_class_name("intolerances-item")
                                    intolerances_list = [intolerance.text for intolerance in intolerances]
                                    recipe_dict["intolerances"] = intolerances_list
                                except:
                                    recipe_dict["intolerances"] = None
                                # recipe_url
                                recipe_dict["recipe_url"] = driver.current_url
                                # images_url
                                images = driver.find_elements_by_tag_name('img')
                                images_list = [image.get_attribute('src') for image in images]
                                recipe_image_url = images_list[1]
                                recipe_dict["recipe_image_url"] = recipe_image_url
                                # category
                                recipe_dict["category"] = category
                                # recipe_list append
                                recipes_list.append(recipe_dict)
                                driver.back()
                                time.sleep(2)
                            print(f'{category} finished')
                            break
                        else:
                            recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                            for x in np.arange(len(recipe_sumup_scrap)):
                                recipe_dict = {}
                                time.sleep(2)
                                recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                                driver.execute_script("arguments[0].click()", recipe_sumup_scrap[x])
                                time.sleep(3)
                                # recipe name
                                recipe_dict["recipe_name"] = driver.find_element_by_tag_name('h1').text
                                # ingredients
                                ingredients_list = []
                                recipe_ingred = driver.find_elements_by_tag_name('td')
                                for x in np.arange(len(recipe_ingred)):
                                    if x % 2 != 0:
                                        ingredients_list.append(recipe_ingred[x].text)
                                    else:
                                        pass
                                recipe_dict["ingredients"] = ingredients_list
                                # time_preparation and calories
                                time_calor_scrap = driver.find_elements_by_class_name("metaheader-value")
                                try:
                                    recipe_dict["time_preparation"] = time_calor_scrap[1].text
                                except:
                                    pass
                                # calories
                                try:
                                    recipe_dict["calories"] = time_calor_scrap[2].text
                                except:
                                    pass
                                # intolerances
                                try:
                                    intolerances = driver.find_elements_by_class_name("intolerances-item")
                                    intolerances_list = [intolerance.text for intolerance in intolerances]
                                    recipe_dict["intolerances"] = intolerances_list
                                except:
                                    recipe_dict["intolerances"] = None
                                # recipe_url
                                recipe_dict["recipe_url"] = driver.current_url
                                # images_url
                                images = driver.find_elements_by_tag_name('img')
                                images_list = [image.get_attribute('src') for image in images]
                                recipe_image_url = images_list[1]
                                recipe_dict["recipe_image_url"] = recipe_image_url
                                # category
                                recipe_dict["category"] = category
                                # recipe_list append
                                recipes_list.append(recipe_dict)
                                driver.back()
                                time.sleep(2)
                            next_page_btn = driver.find_elements_by_css_selector(".next [href]")
                            driver.execute_script("arguments[0].click()", next_page_btn[0])
                            time.sleep(2)
                    main_page = driver.find_elements_by_css_selector(".left [href]")
                    driver.execute_script("arguments[0].click()", main_page[1])
                    time.sleep(2)
                except:
                    driver.back()
                    driver.set_page_load_timeout(10)
                    time.sleep(2)
                    while True:
                        next_page_btn = driver.find_elements_by_class_name('next')
                        if len(next_page_btn) < 1:
                            recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                            for x in np.arange(len(recipe_sumup_scrap) - 1):
                                recipe_dict = {}
                                time.sleep(2)
                                recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                                driver.execute_script("arguments[0].click()", recipe_sumup_scrap[x])
                                time.sleep(3)
                                # recipe name
                                recipe_dict["recipe_name"] = driver.find_element_by_tag_name('h1').text
                                # ingredients
                                ingredients_list = []
                                recipe_ingred = driver.find_elements_by_tag_name('td')
                                for x in np.arange(len(recipe_ingred)):
                                    if x % 2 != 0:
                                        ingredients_list.append(recipe_ingred[x].text)
                                    else:
                                        pass
                                recipe_dict["ingredients"] = ingredients_list
                                # time_preparation and calories
                                time_calor_scrap = driver.find_elements_by_class_name("metaheader-value")
                                try:
                                    recipe_dict["time_preparation"] = time_calor_scrap[1].text
                                except:
                                    pass
                                # calories
                                try:
                                    recipe_dict["calories"] = time_calor_scrap[2].text
                                except:
                                    pass
                                # intolerances
                                try:
                                    intolerances = driver.find_elements_by_class_name("intolerances-item")
                                    intolerances_list = [intolerance.text for intolerance in intolerances]
                                    recipe_dict["intolerances"] = intolerances_list
                                except:
                                    recipe_dict["intolerances"] = None
                                # recipe_url
                                recipe_dict["recipe_url"] = driver.current_url
                                # images_url
                                images = driver.find_elements_by_tag_name('img')
                                images_list = [image.get_attribute('src') for image in images]
                                recipe_image_url = images_list[1]
                                recipe_dict["recipe_image_url"] = recipe_image_url
                                # category
                                recipe_dict["category"] = category
                                # recipe_list append
                                recipes_list.append(recipe_dict)
                                driver.back()
                                time.sleep(2)
                            print(f'{category} finished')
                            break
                        else:
                            recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                            for x in np.arange(len(recipe_sumup_scrap) - 1):
                                recipe_dict = {}
                                time.sleep(2)
                                recipe_sumup_scrap = driver.find_elements_by_class_name("element-header")
                                driver.execute_script("arguments[0].click()", recipe_sumup_scrap[x])
                                time.sleep(3)
                                # recipe name
                                recipe_dict["recipe_name"] = driver.find_element_by_tag_name('h1').text
                                # ingredients
                                ingredients_list = []
                                recipe_ingred = driver.find_elements_by_tag_name('td')
                                for x in np.arange(len(recipe_ingred)):
                                    if x % 2 != 0:
                                        ingredients_list.append(recipe_ingred[x].text)
                                    else:
                                        pass
                                recipe_dict["ingredients"] = ingredients_list
                                # time_preparation and calories
                                time_calor_scrap = driver.find_elements_by_class_name("metaheader-value")
                                try:
                                    recipe_dict["time_preparation"] = time_calor_scrap[1].text
                                except:
                                    pass
                                # calories
                                try:
                                    recipe_dict["calories"] = time_calor_scrap[2].text
                                except:
                                    pass
                                # intolerances
                                try:
                                    intolerances = driver.find_elements_by_class_name("intolerances-item")
                                    intolerances_list = [intolerance.text for intolerance in intolerances]
                                    recipe_dict["intolerances"] = intolerances_list
                                except:
                                    recipe_dict["intolerances"] = None
                                # recipe_url
                                recipe_dict["recipe_url"] = driver.current_url
                                # images_url
                                images = driver.find_elements_by_tag_name('img')
                                images_list = [image.get_attribute('src') for image in images]
                                recipe_image_url = images_list[1]
                                recipe_dict["recipe_image_url"] = recipe_image_url
                                # category
                                recipe_dict["category"] = category
                                # recipe_list append
                                recipes_list.append(recipe_dict)
                                driver.back()
                                time.sleep(2)
                            next_page_btn = driver.find_elements_by_css_selector(".next [href]")
                            driver.execute_script("arguments[0].click()", next_page_btn[0])
                            time.sleep(2)
                    main_page = driver.find_elements_by_css_selector(".left [href]")
                    driver.execute_script("arguments[0].click()", main_page[1])
                    time.sleep(2)
        else:
            current_link = driver.current_url
            print(f"Error at {current_link} and end of the loop")
            break

    with open('../data/raw/web_scraping_recipes_pycharm_1.json', 'w') as json_file:
        json.dump(recipes_list, json_file)

    driver.quit()


if __name__ == "__main__":

    link = 'https://www.lecturas.com/recetas/'
    web_scraping(link)
