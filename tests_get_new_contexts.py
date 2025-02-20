# -*- coding: utf-8 -*-
"""
Dependencies:
    python 3.11
    pillow                    10.2.0
    pandas                    2.2.0
    spyder                    5.5.0
    geopandas                 0.14.2
Created on October 2023

@author: Andrea Gabaldon Moreno
License: GNU GPLv3
The GNU General Public License is a free, copyleft license for software and other kinds of works.
https://www.gnu.org/licenses/gpl-3.0.html
You may copy, distribute and modify the software as long as you track changes/dates in source files.
 Any modifications to or software including (via compiler) GPL-licensed code must also be made
 available under the GPL along with build & install instructions.
 This means, you must:
     - Include original
     - State Changes
     - Disclose source
     - Include the same license -- to make sure it remains free software for all its users.
     - Include copyright
     - Include install instructions

You cannot: sublicense or hold liable.

Copyright @CARTIF 2025

***********************************************************************************************

This part of the code is changes the

***********************************************************************************************
"""



import os
import json
import pandas as pd
from scripts.RESbased_scenario_generator.RESbased_scenario_generator import res_based_generator_list_technologies
from scripts.RESbased_scenario_generator.get_new_context import resbased_generator_context_creation
from scripts.KPI_module.key_performance_indicators import recalculate_indicators, community_KPIs, aggregate_demand_profiles
def test_get_new_context():
    # context_object = r'd:\Documents\localres_local\scripts\data\ispaster_two_buildings.json'
    context_object = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts","data_example","dummy_data_example.json")
    import json

    with open(context_object) as f:
        community_context = json.load(f)
    # List of countries and goals to vary
    # countries = ["ES", "AT", "FI", "IT"]
    # goals = {
    #     "1": "Higher rate of renewable energy",
    #     "2": "Higher efficiency",
    #     "3": "Energy self-sufficiency",
    #     "4": "Decarbonisation of H&C",
    #     "5": "Electrification",
    #     "6": "E-mobility",
    #     "7": "Otra cosa,No estoy seguro"
    # }
    user = {
        "goals": 2,
        "country": "ES"
    }
    # recommendations = res_based_generator_list_technologies(user)
    recommendations = {#0: {"id": 3, "action_name": "solar_fleet"}
        0: {"id": 4, "action_name": "wind_fleet"}
    }
    community_context_updated_2=resbased_generator_context_creation(goal=user["goals"], community_context=community_context,
                                                                    recommendations_dic=recommendations)

    # #grupo de escenairos, uno por cada action key
    # #
    # scenarios=scenarios(goal, recommendations,community_context)
    #

    output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"outputs", "output_context.json")
    with open(output_file_path, "w") as json_file:
        json.dump(community_context_updated_2, json_file, indent=4)

def try_resbased_generator_list():
    countries = ["ES"]
    # , "AT", "FI","IT"]
    goals = {
        "1": "Higher rate of renewable energy",
        # "2": "Higher efficiency",
        # "3": "Energy self-sufficiency",
        # "4": "Decarbonisation of H&C",
        # "5": "Electrification",
        # "6": "E-mobility",
        # "7": "Otra cosa,No estoy seguro"
    }

    # Initialize an empty list to store the results
    results = []
        # Loop through each combination of country and goal
    for country in countries:
        for goal_key, goal_value in goals.items():
            try:
                # Create the user object
                user = {
                    "goals": goal_key,
                    "country": country
                }
                # Call the function and capture the result
                usage_for_one = res_based_generator_list_technologies(user)
                print(f"run {goal_key} for {country}, with recommendations: {usage_for_one}")
                # Store the result in the list
                results.append({
                    "Country": country,
                    "Goal": goal_value,
                    "Result": usage_for_one,
                })
            except Exception as e:
                # In case of an error, store the error message
                results.append({
                    "Country": country,
                    "Goal": goal_value,
                    "Result": str(e)
                })

    return results

def get_KPIs():
    context_object_2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts","data_example",
                                    "output_context_with_results_from_optimisation.json")

    with open(context_object_2) as f:
        community_context_for_KPIs = json.load(f)

    citizen_KPIs_per_building, demand_profiles_context, areas_buildings = recalculate_indicators(
        community_context_for_KPIs)
    # citizen_KPIs_per_building, demand_profiles_context,areas_buildings=recalculate_indicators(community_context)
    # calculate total aggregated demand
    total_demand = aggregate_demand_profiles(demand_profiles_context)
    # calculate total community indicators
    community_indicators = community_KPIs(citizen_KPIs_per_building, total_demand, areas_buildings)
    # try_resbased_generator_list()
    return community_indicators

print('test')