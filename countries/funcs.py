import requests as req
import csv
import json
import os
from languages import languages

real_path = os.path.dirname(__file__)

def menu():
    print("COUNTRIES".center(50, "-"))
    print("1. Find Country")
    print("2. Find Region")
    print("3. Countries by language")
    print("4. Download flag")
    print("5. History")
    print("6. TopTenArea")
    print("7. TopTenPop")
    print("8. MostSpokenLanguage")
    print("q. Exit")


# def get_by_country_name (country_name, res):
#     get_country= list(filter(lambda country: country["name"] == country_name , res))
#     return get_country[0]

def get_by_name (country_name):
    res = req.get(f"https://restcountries.eu/rest/v2/name/{country_name}").json()

    if type(res) == list:
        country = res[0]
        result = [country["name"], country["capital"], country["region"], country["population"], country["area"], country["languages"][0]["name"], country["flag"]]
        return result
    elif type(res) == dict:
        return res["message"]


def export_countries(result):
    if type(result) == list:
        with open(f"{real_path}/export_countries.csv", "a",  encoding="utf8", newline="") as file:
            csv_writer = csv.writer(file, delimiter=",")
            csv_writer.writerow(result)



def get_countries_by_continent (region):
    res = req.get(f"https://restcountries.eu/rest/v2/region/{region}").json()

    if type(res) == list:
        region = res
        return region

    elif type(res) == dict:
        return res["message"]

def export_region(region, region_name):

    if type(region) == list:
        with open(f"{real_path}/{region_name}.json", "w", encoding="utf8") as file:
            json.dump({"region": region}, file, ensure_ascii=False, indent = 4)

def total_population(region, region_name):
    region = []
    if type(region) == list:
        with open(f"{real_path}/{region_name}.json", "r", encoding="utf8") as file:
            data = json.load(file)["region"]
            population = list(map(lambda country: country["population"], data))
            return sum(population)

# def get_by_languages(et):
#     res = req.get(f"https://restcountries.eu/rest/v2/lang/{et}").json()

#     if type(res) == list:
#         languagelist = res
#         return languagelist
    
#     elif type(res) == dict:
#         return res["message"]


def get_iso(user_language):
    result = list(filter(lambda tupla:tupla[1].lower().find(user_language) == 0 , languages))

    if len(result) >= 1:
        return result[0][0]
    else:
        return False

def get_by_language(iso_language):
    if iso_language:
        res = req.get(f"https://restcountries.eu/rest/v2/lang/{iso_language}").json()
        return len(res)
    else:
        return f"No matches for your search"

def get_flag(country_name):
    res = req.get(f"https://restcountries.eu/rest/v2/name/{country_name}").json()

    if type(res) == list:
        country = res[0]
        result = country["flag"]
        flag = req.get(result).content
        with open(f"{real_path}/img/{country_name}.svg", "wb") as file:
            file.write(flag)
            return "download sucessfully"
    
    elif type(res) == dict:
        return res["message"]
    
def history():
    with open(f"{real_path}/export_countries.csv", "r",  encoding="utf8") as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] != "name":
                print(f"name: {line[0]} - population: {line[3]}")
        
def top_ten():
    res = req.get(f"https://restcountries.eu/rest/v2/all").json()
    areasord = sorted(res, key=lambda country: country["area"] if country["area"] else 0, reverse=True)[0:11]
    print (areasord)

def top_ten_population():
    res = req.get(f"https://restcountries.eu/rest/v2/all").json()
    areasord = sorted(res, key=lambda country: country["population"] / country["area"] if country["population"] and country["area"] else 0, reverse=True)[0:11] #si es que population y country son "verdad"
    print (areasord)

def most_spoken_language():
    res = req.get(f"https://restcountries.eu/rest/v2/all").json()
    result = {}
    for country in res:
        try:
            result[country["languages"][0]["name"]] += 1
        except:
            result[country["languages"][0]["name"]] = 1
    print(type(result))
    
    sortedresult = sorted(result.items(), key=lambda tupla:tupla[1], reverse=True)
    print(sortedresult)
    
    