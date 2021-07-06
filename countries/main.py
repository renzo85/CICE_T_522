# COUNTRIES
# https://restcountries.eu/
# https://requests.readthedocs.io/en/master/
# Instalar la librería requests

# Hacer una request a la url que nos traiga todos los países del mundo
# Crear una pequeña aplicación con las siguientes características:
# Buscar país
# Cada uno de los países buscados debe quedar escrito en un archivo tipo csv que solo admitirá los siguientes valores: name, capital, region, population, area, idioma (el primero), flag A su vez estos valores acturán como cabeceros
# Buscar continente
# Cuando se busquen países por continente, estos deben ser escritos en un archivo json con nombre dinámico EJ. dinámico --> Si se busca "africa", el archivo deberá llamarse --> africa.json
# Además entregar la población total del continente
# Paises por idioma
# Devolver una lista con todos los paises que hablan el idioma indicado por el usuario
# Descargar bandera
# Permita al usuario descargar la bandera del país que quiera.
# Estas imágenes serán guardadas en una carpeta aparte con el nombre del país

# Historial
# Devolvera una lista de los paises buscados de la siguiente manera:
# name: value - population: value

# Encontrar los 10 paises más grandes
# Encontrar los 10 paises más densamente poblados
# ¿Cuál es el idioma oficial más hablado en más países?

#-------------------------------------------

import requests as req
import funcs



# res = req.get("https://restcountries.eu/rest/v2/all").json()
# print (res[0])



user = "0"
while user != "q":
    funcs.menu()
    user = input("Choose: ")

    if user == "1":
        country_name = input("CountryName: ")
        country = funcs.get_by_name (country_name)
        funcs.export_countries(country)
        print (country)
        
    elif user == "2":
        region_name = input("Type RegionName (Africa, Americas, Asia, Europe, Oceania): ")
        #region = funcs.get_countries_by_continent(region_name)
        #funcs.export_region(region, region_name)
        #print (region)
        try:
            poblacion_total = funcs.total_population("s", region_name)
            print(poblacion_total)
        
        except FileNotFoundError:
            region = funcs.get_countries_by_continent(region_name)
            funcs.export_region(region, region_name)
            poblacion_total = funcs.total_population(region, region_name)
            print(poblacion_total)

    # elif user == "3":
    #     language_name = input("Type Language (es: for spanish, en: for english, fr: for french, pt: for portuguese...): ")
    #     language = funcs.get_by_languages(language_name)
    #     print (len(language))

    elif user == "3":
        language_name = input("Search by language: ").lower()
        print (funcs.get_iso(language_name))
        iso_language = funcs.get_iso(language_name)
        print (funcs.get_by_language(iso_language))

    elif user == "4":
        country_name = input("CountryName: ")
        country = funcs.get_flag (country_name)
        print (country)
    
    elif user == "5":
        funcs.history()
        user = input("Continue...")

    elif user == "6":
        funcs.top_ten()

    elif user == "7":
        funcs.top_ten_population()
    
    elif user == "8":
        funcs.most_spoken_language()
