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
            item = json.load(open(path_to_file))
            info_dictionary[item["{}Id".format(path)]] = item["name"]
 
    return info_dictionary

def path_creater(path):
    f_path = ""
    for _dir in path: 
        f_path += "".join(_dir + "/")

    return f_path

def recursive_mkdir(path):
    index = path.find("/") 
    if( (index == 0) & (len(path) > 1) ):
        recursive_mkdir(path[index+1:])
        return
    if(index != -1):
        directory = path[:index]
        os.makedirs(directory, exist_ok=True)
        os.chdir(directory)
        recursive_mkdir(path.replace(directory+"/",""))
        os.chdir("..")
        return
    if(len(path) != 0):
        os.makedirs(path, exist_ok=True)
        return

def main(path, country, cities, towns):
    for json_file in os.scandir(path):
        if(json_file.name[-4:] == "json"):
            file_path = "./{}/{}".format(path,json_file.name)
            quarter = json.load(open(file_path))
            suffix = json_file.name.split(".")[0]
            if( quarter["cityId"] <= 81 ):
                city_name     = cities.get(quarter["cityId"])
                town_name     = towns.get(quarter["townId"])
                path_to_save  = path_creater([country, city_name, town_name])
                recursive_mkdir(path_to_save)

                quarter_name = quarter["name"].replace(" ","-")
                full_path = path_to_save + "/" + quarter_name + "_" + suffix + ".json"
                shutil.copyfile(file_path,full_path) 
                os.remove(file_path)

    print("all {} has been organized".format(path))

if __name__ == "__main__":
    cities = get_dictionary("city")
    towns  = get_dictionary("town")
    main("quarters","Turkiye", cities, towns)
