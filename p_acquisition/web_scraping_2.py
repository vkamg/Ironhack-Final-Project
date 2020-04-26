from selenium import webdriver
import time
import numpy as np
import json


def web_scraping(link):
    # Opening the Chrome and going to the Web

    recipe_link = 'https://www.recetasgratis.net/'
    chromedriver = "/home/veronica/Ironhack/Final Project/Chrome Driver/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    driver.get(recipe_link)

    # Enabling cookies

    time.sleep(3)
    element = driver.find_elements_by_class_name('consent-accept')
    element[0].click()

    # Selecting cat

    time.sleep(3)
    categories = driver.find_elements_by_xpath('(/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div/a)')

    # Looping throught the categories

    recipes_list = []
    driver.set_page_load_timeout(10)

    for x in np.arange(len(categories)):
        try:
            categories = driver.find_elements_by_xpath('(/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div/a)')
            driver.execute_script("arguments[0].click()", categories[x])
            category = driver.find_elements_by_tag_name('h1')[0].text
            time.sleep(2)
            while True:
                next_page_btn = driver.find_elements_by_class_name('next.ga')
                if len(next_page_btn) < 1:
                    recipe_sumup_scrap = driver.find_elements_by_class_name("titulo.titulo--resultado")
                    for x in np.arange(len(recipe_sumup_scrap)):
                        try:
                            recipe_dict = {}
                            time.sleep(2)
                            recipe_sumup_scrap = driver.find_elements_by_class_name("titulo.titulo--resultado")
                            driver.execute_script("arguments[0].click()", recipe_sumup_scrap[x])
                            time.sleep(3)
                            # recipe name
                            recipe_dict["recipe_name"] = driver.find_elements_by_tag_name('h1')[0].text
                            # ingredients
                            recipe_dict["ingredients"] = driver.find_elements_by_class_name('ingredientes')[0].text
                            # time_preparation and calories
                            try:
                                recipe_dict["time_preparation"] = \
                                driver.find_elements_by_class_name('property.duracion')[0].text
                            except:
                                recipe_dict["time_preparation"] = None
                            # recipe_url
                            recipe_dict["recipe_url"] = driver.current_url
                            # images_url
                            images = driver.find_elements_by_xpath(
                                '(/html/body/div[1]/div[3]/div[2]/article/div[2]/div[1]/div/div/img)')
                            recipe_dict["recipe_image_url"] = images[0].get_attribute('src')
                            # category
                            recipe_dict["category"] = category
                            # extra_info
                            try:
                                more_info = driver.find_elements_by_xpath(
                                    '(/html/body/div[1]/div[3]/div[2]/article/div[2]/div[4]/div[2]/a)')
                                more_info_list = [info.text for info in more_info]
                                recipe_dict["more_info"] = more_info_list
                            except:
                                recipe_dict["more_info"] = None
                            # steps
                            try:
                                steps = driver.find_elements_by_xpath(
                                    '(/html/body/form/main/article/div[2]/div/div[3]/div[2]/div/figure/figcaption/div/p)')
                                steps_list = [step.text for step in steps]
                                recipe_dict["recipe_steps"] = steps_list
                            except:
                                recipe_dict["recipe_steps"] = None
                            # recipe_list append
                            recipes_list.append(recipe_dict)
                            driver.back()
                            time.sleep(2)
                        except:
                            driver.back()
                            pass
                    print(f"{category} finished")
                    break
                else:
                    recipe_sumup_scrap = driver.find_elements_by_class_name("titulo.titulo--resultado")
                    for x in np.arange(len(recipe_sumup_scrap)):
                        try:
                            recipe_dict = {}
                            time.sleep(2)
                            recipe_sumup_scrap = driver.find_elements_by_class_name("titulo.titulo--resultado")
                            driver.execute_script("arguments[0].click()", recipe_sumup_scrap[x])
                            time.sleep(3)
                            # recipe name
                            recipe_dict["recipe_name"] = driver.find_elements_by_tag_name('h1')[0].text
                            # ingredients
                            recipe_dict["ingredients"] = driver.find_elements_by_class_name('ingredientes')[0].text
                            # time_preparation and calories
                            try:
                                recipe_dict["time_preparation"] = \
                                driver.find_elements_by_class_name('property.duracion')[0].text
                            except:
                                recipe_dict["time_preparation"] = None
                            # recipe_url
                            recipe_dict["recipe_url"] = driver.current_url
                            # images_url
                            images = driver.find_elements_by_xpath(
                                '(/html/body/div[1]/div[3]/div[2]/article/div[2]/div[1]/div/div/img)')
                            recipe_dict["recipe_image_url"] = images[0].get_attribute('src')
                            # category
                            recipe_dict["category"] = category
                            # extra_info
                            try:
                                more_info = driver.find_elements_by_xpath(
                                    '(/html/body/div[1]/div[3]/div[2]/article/div[2]/div[4]/div[2]/a)')
                                more_info_list = [info.text for info in more_info]
                                recipe_dict["more_info"] = more_info_list
                            except:
                                recipe_dict["more_info"] = None
                            # steps
                            try:
                                steps = driver.find_elements_by_xpath(
                                    '(/html/body/form/main/article/div[2]/div/div[3]/div[2]/div/figure/figcaption/div/p)')
                                steps_list = [step.text for step in steps]
                                recipe_dict["recipe_steps"] = steps_list
                            except:
                                recipe_dict["recipe_steps"] = None
                            # recipe_list append
                            recipes_list.append(recipe_dict)
                            driver.back()
                            time.sleep(2)
                        except:
                            driver.back()
                            pass
                    next_page_btn = driver.find_elements_by_class_name('next.ga')
                    driver.execute_script("arguments[0].click()", next_page_btn[0])
                    time.sleep(2)
            main_page = driver.find_elements_by_class_name("logo-default")
            driver.execute_script("arguments[0].click()", main_page[0])
            time.sleep(2)
        except:
            current_link = driver.current_url
            print(f"TimeoutError at {current_link}")
            driver.get(current_link)
            driver.set_page_load_timeout(10)
            try:
                while True:
                    next_page_btn = driver.find_elements_by_class_name('next.ga')
                    if len(next_page_btn) < 1:
                        recipe_sumup_scrap = driver.find_elements_by_class_name("titulo.titulo--resultado")
                        for x in np.arange(len(recipe_sumup_scrap)):
                            try:
                                recipe_dict = {}
                                time.sleep(2)
                                recipe_sumup_scrap = driver.find_elements_by_class_name("titulo.titulo--resultado")
                                driver.execute_script("arguments[0].click()", recipe_sumup_scrap[x])
                                time.sleep(3)
                                # recipe name
                                recipe_dict["recipe_name"] = driver.find_elements_by_tag_name('h1')[0].text
                                # ingredients
                                recipe_dict["ingredients"] = driver.find_elements_by_class_name('ingredientes')[0].text
                                # time_preparation and calories
                                try:
                                    recipe_dict["time_preparation"] = \
                                    driver.find_elements_by_class_name('property.duracion')[0].text
                                except:
                                    recipe_dict["time_preparation"] = None
                                # recipe_url
                                recipe_dict["recipe_url"] = driver.current_url
                                # images_url
                                images = driver.find_elements_by_xpath(
                                    '(/html/body/div[1]/div[3]/div[2]/article/div[2]/div[1]/div/div/img)')
                                recipe_dict["recipe_image_url"] = images[0].get_attribute('src')
                                # category
                                recipe_dict["category"] = category
                                # extra_info
                                try:
                                    more_info = driver.find_elements_by_xpath(
                                        '(/html/body/div[1]/div[3]/div[2]/article/div[2]/div[4]/div[2]/a)')
                                    more_info_list = [info.text for info in more_info]
                                    recipe_dict["more_info"] = more_info_list
                                except:
                                    recipe_dict["more_info"] = None
                                # steps
                                try:
                                    steps = driver.find_elements_by_xpath(
                                        '(/html/body/form/main/article/div[2]/div/div[3]/div[2]/div/figure/figcaption/div/p)')
                                    steps_list = [step.text for step in steps]
                                    recipe_dict["recipe_steps"] = steps_list
                                except:
                                    recipe_dict["recipe_steps"] = None
                                # recipe_list append
                                recipes_list.append(recipe_dict)
                                driver.back()
                                time.sleep(2)
                            except:
                                driver.back()
                            pass
                        print(f"{category} finished")
                        break
                    else:
                        recipe_sumup_scrap = driver.find_elements_by_class_name("titulo.titulo--resultado")
                        for x in np.arange(len(recipe_sumup_scrap)):
                            try:
                                recipe_dict = {}
                                time.sleep(2)
                                recipe_sumup_scrap = driver.find_elements_by_class_name("titulo.titulo--resultado")
                                driver.execute_script("arguments[0].click()", recipe_sumup_scrap[x])
                                time.sleep(3)
                                # recipe name
                                recipe_dict["recipe_name"] = driver.find_elements_by_tag_name('h1')[0].text
                                # ingredients
                                recipe_dict["ingredients"] = driver.find_elements_by_class_name('ingredientes')[0].text
                                # time_preparation and calories
                                try:
                                    recipe_dict["time_preparation"] = \
                                    driver.find_elements_by_class_name('property.duracion')[0].text
                                except:
                                    recipe_dict["time_preparation"] = None
                                # recipe_url
                                recipe_dict["recipe_url"] = driver.current_url
                                # images_url
                                images = driver.find_elements_by_xpath(
                                    '(/html/body/div[1]/div[3]/div[2]/article/div[2]/div[1]/div/div/img)')
                                recipe_dict["recipe_image_url"] = images[0].get_attribute('src')
                                # category
                                recipe_dict["category"] = category
                                # extra_info
                                try:
                                    more_info = driver.find_elements_by_xpath(
                                        '(/html/body/div[1]/div[3]/div[2]/article/div[2]/div[4]/div[2]/a)')
                                    more_info_list = [info.text for info in more_info]
                                    recipe_dict["more_info"] = more_info_list
                                except:
                                    recipe_dict["more_info"] = None
                                # steps
                                try:
                                    steps = driver.find_elements_by_xpath(
                                        '(/html/body/form/main/article/div[2]/div/div[3]/div[2]/div/figure/figcaption/div/p)')
                                    steps_list = [step.text for step in steps]
                                    recipe_dict["recipe_steps"] = steps_list
                                except:
                                    recipe_dict["recipe_steps"] = None
                                # recipe_list append
                                recipes_list.append(recipe_dict)
                                driver.back()
                                time.sleep(2)
                            except:
                                driver.back()
                            pass
                        next_page_btn = driver.find_elements_by_class_name('next.ga')
                        driver.execute_script("arguments[0].click()", next_page_btn[0])
                        time.sleep(2)
                main_page = driver.find_elements_by_class_name("logo-default")
                driver.execute_script("arguments[0].click()", main_page[0])
                time.sleep(2)
            except:
                driver.back()
                driver.set_page_load_timeout(10)
                time.sleep(2)
                while True:
                    next_page_btn = driver.find_elements_by_class_name('next.ga')
                    if len(next_page_btn) < 1:
                        recipe_sumup_scrap = driver.find_elements_by_class_name("titulo.titulo--resultado")
                        for x in np.arange(len(recipe_sumup_scrap)):
                            try:
                                recipe_dict = {}
                                time.sleep(2)
                                recipe_sumup_scrap = driver.find_elements_by_class_name("titulo.titulo--resultado")
                                driver.execute_script("arguments[0].click()", recipe_sumup_scrap[x])
                                time.sleep(3)
                                # recipe name
                                recipe_dict["recipe_name"] = driver.find_elements_by_tag_name('h1')[0].text
                                # ingredients
                                recipe_dict["ingredients"] = driver.find_elements_by_class_name('ingredientes')[0].text
                                # time_preparation and calories
                                try:
                                    recipe_dict["time_preparation"] = \
                                    driver.find_elements_by_class_name('property.duracion')[0].text
                                except:
                                    recipe_dict["time_preparation"] = None
                                # recipe_url
                                recipe_dict["recipe_url"] = driver.current_url
                                # images_url
                                images = driver.find_elements_by_xpath(
                                    '(/html/body/div[1]/div[3]/div[2]/article/div[2]/div[1]/div/div/img)')
                                recipe_dict["recipe_image_url"] = images[0].get_attribute('src')
                                # category
                                recipe_dict["category"] = category
                                # extra_info
                                try:
                                    more_info = driver.find_elements_by_xpath(
                                        '(/html/body/div[1]/div[3]/div[2]/article/div[2]/div[4]/div[2]/a)')
                                    more_info_list = [info.text for info in more_info]
                                    recipe_dict["more_info"] = more_info_list
                                except:
                                    recipe_dict["more_info"] = None
                                # steps
                                try:
                                    steps = driver.find_elements_by_xpath(
                                        '(/html/body/form/main/article/div[2]/div/div[3]/div[2]/div/figure/figcaption/div/p)')
                                    steps_list = [step.text for step in steps]
                                    recipe_dict["recipe_steps"] = steps_list
                                except:
                                    recipe_dict["recipe_steps"] = None
                                # recipe_list append
                                recipes_list.append(recipe_dict)
                                driver.back()
                                time.sleep(2)
                            except:
                                driver.back()
                            pass
                        print(f"{category} finished")
                        break
                    else:
                        recipe_sumup_scrap = driver.find_elements_by_class_name("titulo.titulo--resultado")
                        for x in np.arange(len(recipe_sumup_scrap)):
                            try:
                                recipe_dict = {}
                                time.sleep(2)
                                recipe_sumup_scrap = driver.find_elements_by_class_name("titulo.titulo--resultado")
                                driver.execute_script("arguments[0].click()", recipe_sumup_scrap[x])
                                time.sleep(3)
                                # recipe name
                                recipe_dict["recipe_name"] = driver.find_elements_by_tag_name('h1')[0].text
                                # ingredients
                                recipe_dict["ingredients"] = driver.find_elements_by_class_name('ingredientes')[0].text
                                # time_preparation and calories
                                try:
                                    recipe_dict["time_preparation"] = \
                                    driver.find_elements_by_class_name('property.duracion')[0].text
                                except:
                                    recipe_dict["time_preparation"] = None
                                # recipe_url
                                recipe_dict["recipe_url"] = driver.current_url
                                # images_url
                                images = driver.find_elements_by_xpath(
                                    '(/html/body/div[1]/div[3]/div[2]/article/div[2]/div[1]/div/div/img)')
                                recipe_dict["recipe_image_url"] = images[0].get_attribute('src')
                                # category
                                recipe_dict["category"] = category
                                # extra_info
                                try:
                                    more_info = driver.find_elements_by_xpath(
                                        '(/html/body/div[1]/div[3]/div[2]/article/div[2]/div[4]/div[2]/a)')
                                    more_info_list = [info.text for info in more_info]
                                    recipe_dict["more_info"] = more_info_list
                                except:
                                    recipe_dict["more_info"] = None
                                # steps
                                try:
                                    steps = driver.find_elements_by_xpath(
                                        '(/html/body/form/main/article/div[2]/div/div[3]/div[2]/div/figure/figcaption/div/p)')
                                    steps_list = [step.text for step in steps]
                                    recipe_dict["recipe_steps"] = steps_list
                                except:
                                    recipe_dict["recipe_steps"] = None
                                # recipe_list append
                                recipes_list.append(recipe_dict)
                                driver.back()
                                time.sleep(2)
                            except:
                                driver.back()
                            pass
                        next_page_btn = driver.find_elements_by_class_name('next.ga')
                        driver.execute_script("arguments[0].click()", next_page_btn[0])
                        time.sleep(2)
                main_page = driver.find_elements_by_class_name("logo-default")
                driver.execute_script("arguments[0].click()", main_page[0])
                time.sleep(2)
        else:
            current_link = driver.current_url
            print(f"check if error at {current_link}")
            pass

    #df_recipes = pd.DataFrame(recipes_list)

    with open('../data/raw/web_scraping_recipes_recetasgratis.json', 'w') as json_file:
        json.dump(recipes_list, json_file)

    driver.quit()


if __name__ == "__main__":

    link = 'https://www.recetasgratis.net/'
    web_scraping(link)