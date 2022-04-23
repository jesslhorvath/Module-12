"""
Programs: counties_class.py, import.py
Author: Jessie Horvath
Modified: 4/23/22

The purpose of this program is to import and save data from a csv file
to a class and use that class to view and calculate data of interest.
"""

import csv
from counties_class import County

def find_pop_per_household(county_name):
    population = county[county_name].population
    households = county[county_name].num_households
    pop_per_house = int(population.replace(',','')) / int(households.replace(',',''))
    pop_per_house = round(pop_per_house, 2)
    return "Population per household for " + str(county_name) + " county: " + str(pop_per_house)

with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    county = {}

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        if row[0] != "":
            county[str(row[1])] = County(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

dallas_county = print(find_pop_per_household('Dallas'))

total_pop = 0
for key in county:
    total_pop += int(county[key].population.replace(',',''))
print("Total Population: " + str(total_pop))
