#!/usr/bin/env python3

import time
import json
import csv
import os

def get_dictionary(path):
    info_dictionary     = {}
    for json_file in os.scandir(path):
        path_to_file = "{}/{}".format(path,json_file.name)
        if(json_file.is_file()):
            item = json.load(open(path_to_file))
            info_dictionary[item["{}Id".format(path.split("/")[-1])]] = item["name"]
    return info_dictionary

# İstanbul;Avcılar;GÜMÜŞPALA Mh.;
def csv_updater(city, town, quarter, quarterId):
    with open("./Kapali-Mahalleler_quarterId.csv", newline='') as csvfile:
        for row in csvfile:
            row_id       = row.split(";")[0]
            city_name    = row.split(";")[1].upper()
            town_name    = row.split(";")[2].upper() 
            quarter_name = row.split(";")[3].upper()[0:-2].split(" ")[0:-1]
            passed_quarter = quarter.upper().split(" ")[0:-1]
            if(           
                    (city_name    == city.upper())       & 
                    (town_name    == town.upper())       &
                    (quarter_name == passed_quarter)
            ):
                # print(row[0:-2], "\n", "000;{};{};{}".format(city.lower(), town.lower(), quarter.lower()))
                with open("second.csv", "a") as f:
                    f.write(row[0:-2] + ";" + str(quarterId) + '\n')
                break

def main(path, cities, towns):
    for json_file in os.scandir(path):
        if(json_file.name[-4:] == "json"):
            file_path = "{}/{}".format(path,json_file.name)
            quarter   = json.load(open(file_path))
            # if( quarter["quarterId"] == 9 ):
            if( quarter["cityId"] <= 81 ):
                city     = cities.get(quarter["cityId"])
                town     = towns.get(quarter["townId"])
                quarterName  = quarter["name"]
                quarterId = quarter["quarterId"]
                # print(city , ", ", town, ", ", quarterName, ", ", quarterId)
                csv_updater(city, town, quarterName, quarterId)

if __name__ == "__main__":
    cities = get_dictionary("./TurkeyGeoData/city")
    towns  = get_dictionary("./TurkeyGeoData/town")
    main("./TurkeyGeoData/quarters", cities, towns)
