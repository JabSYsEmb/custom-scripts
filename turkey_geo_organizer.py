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
    index = path.find("/") 
    if(index == 0 ):
        recursive_mkdir(path[index+1:])
        return # function terminator
    if(index != -1):
        directory = path[:index]
        os.makedirs(directory, exist_ok=True)
        os.chdir(directory)
        recursive_mkdir(path.replace(directory+"/",""))
        os.chdir("..")
        return # function terminator
    if(len(path) != 0):
        os.makedirs(path, exist_ok=True)
        return # function terminator

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
    cities = get_dictionary("cities")
    towns  = get_dictionary("towns")
    main("quarters", cities, towns)
