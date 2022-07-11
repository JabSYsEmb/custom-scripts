#!/usr/bin/env python3

import shutil
import sys
import os

import json

def get_dictionary(path):
    info_dictionary     = {}

    for json_file in os.scandir(path):
        path_to_file = "{}/{}".format(path,json_file.name)
        if(json_file.is_file()):
            if(path == "cities"):
                city = json.load(open(path_to_file))
                info_dictionary[city["cityId"]] = city["name"]

            if(path == "towns"):
                town = json.load(open(path_to_file))
                info_dictionary[town["townId"]] = town["name"]

    return info_dictionary

def recursive_mkdir(path):
    root = path.split("/")[0]
    city_dir  = path.split("/")[1]
    town_dir  = path.split("/").pop()
    os.chdir(root)
    os.makedirs(city_dir, exist_ok=True)
    os.chdir(city_dir)
    os.makedirs(town_dir, exist_ok=True)
    os.chdir("../../")

def main(path, cities, towns):
    for json_file in os.scandir(path):
        if(json_file.name[-4:] == "json"):
            file_path = "./{}/{}".format(path,json_file.name)
            quarter = json.load(open(file_path))
            if( quarter["cityId"] <= 81):
                city_name     = cities.get(quarter["cityId"])
                town_name     = towns.get(quarter["townId"])
                path_to_save  = "Turkiye/{}/{}".format(city_name, town_name)
                recursive_mkdir(path_to_save)

                quarter_name = quarter["name"].replace(" ","-")
                full_path = path_to_save + "/" + quarter_name + ".json"
                shutil.copyfile(file_path,full_path) 
                os.remove(file_path)

    print("all {} has been organized".format(path))

if __name__ == "__main__":
    os.makedirs("Turkiye",exist_ok=True)
    cities = get_dictionary("cities")
    towns  = get_dictionary("towns")
    main("quarters", cities, towns)
