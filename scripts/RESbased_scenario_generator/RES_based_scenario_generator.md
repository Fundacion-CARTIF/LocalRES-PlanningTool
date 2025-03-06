# LocalRES Project Repository

## About the RES-based scenario generator

The **RES-based Scenario Generator** is an open-source Python module designed to generate renewable energy system (RES) scenarios based on user-defined objectives and country-specific recommendations. It integrates multiple data sources and methodologies to suggest technologies suitable for different energy goals.

## License
License: GNU GPLv3  
The GNU General Public License is a free, copyleft license for software and other kinds of works.
GNU General Public License Version 3

You may copy, distribute and modify the software as long as you track changes/dates in source files. Any modifications to or software including (via compiler) GPL-licensed code must also be made available under the GPL along with build & install instructions. This means, you must:

- Include original
- State Changes
- Disclose source
- Include the same license -- to make sure it remains free software for all its users.
- Include copyright
- Include install instructions

You cannot: sublicense or hold liable.

## Disclaimer
The content of this repository reflects only the authors' view and the European Union is not responsible for any use that may be made of the information it contains. The LocalRES consortium does not guarantee the accuracy of the data included in this repository and is not responsible for any third-party use of its contents. 
## Dependencies
    Python 3.11
    Pillow 10.2.0
    Pandas 2.2.0
    Spyder 5.5.0
    GeoPandas 0.14.2
    Shapely
    PyProj
    pvlib
## Usage
Import the module and generate RES recommendations:

```python
from RESbased_scenario_generator import res_based_generator_list_technologies

user_inputs = {
    "goals": "3",  # Energy goal ID
    "country": "AT"  # Country code (ISO-2 format)
}

recommendations = res_based_generator_list_technologies(user_inputs)
```
The function returns a JSON-style dictionary containing recommended technologies:
```python
{
    "0": {"id": 1, "action_name": "reduction_of_demand"},
    "1": {"id": 2, "action_name": "demand_response"},
    "2": {"id": 16, "action_name": "heat_storage"},
    "3": {"id": 3, "action_name": "solar_fleet"},
    "4": {"id": 7, "action_name": "solar_thermal"}
}

```
The module also supports geospatial data in GeoJSON format for building assessments:

Input:
```python
{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[16.3725, 48.2082], [16.3726, 48.2083], [16.3724, 48.2084], [16.3725, 48.2082]]]
            },
            "properties": {
                "height": 6,
                "building_use_id": 1,
                "construction_year": 1990
            }
        }
    ]
}
```
Output
```python
{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[16.3725, 48.2082], [16.3726, 48.2083], [16.3724, 48.2084], [16.3725, 48.2082]]]
            },
            "properties": {
                "energy_demand": {
                    "heating": 12000,
                    "cooling": 3000,
                    "electricity": 5000
                }
            }
        }
    ]
}
```

### Functions 
The RESbased_scenario_generator.py has several functions:

# RESbased_scenario_generator.py

## 1. res_based_generator_list_technologies(inputs_users)
Generates a list of recommended renewable energy technologies based on user-defined goals and country selection.

### Parameters
- `inputs_users` (dict): A dictionary containing user-selected energy goals and country information.
  - `"goals"` (str): The energy goal identifier (e.g., "3" for self-sufficiency).
  - `"country"` (str): The ISO country code (e.g., "AT" for Austria).

### Returns
- `output_dictionary_matched` (dict): A dictionary mapping recommended actions to their respective action keys and descriptions.

### Usage Example
```python
from RESbased_scenario_generator import res_based_generator_list_technologies

# Define user inputs
user_inputs = {
    "goals": "3",  # Goal for energy self-sufficiency
    "country": "AT"  # Austria
}

# Get recommended technologies
recommendations = res_based_generator_list_technologies(user_inputs)

# Print recommendations
for key, value in recommendations.items():
    print(f"Action {value['id']}: {value['action_name']}")
```

## 2. match_actions(action_keys, data)
Matches actions from the RES library with input actions based on a predefined key mapping.

### Parameters
- `action_keys` (DataFrame): A dataset containing predefined action mappings.
- `data` (dict): Dictionary of user-defined actions.

### Returns
- `matched_actions` (dict): A dictionary where each action is associated with its corresponding action key.

### Usage Example
```python
from RESbased_scenario_generator import match_actions
import pandas as pd

# Load action keys CSV into a DataFrame
action_keys_df = pd.read_csv("path/to/action_keys.csv")

# Example user actions
user_data = {
    1: {"id": 1, "action_name": "solar_fleet"},
    2: {"id": 2, "action_name": "biomass_boiler"}
}

# Match actions
matched_actions = match_actions(action_keys_df, user_data)

# Display matched actions
print(matched_actions)
```

## 3. calculate_action_values(goal_numeric_value, country_properties, json_file_path_country_vs_actions_df)
Calculates action values using a multi-criteria decision analysis (MCDA) approach.

### Parameters
- `goal_numeric_value` (float): Numeric representation of the selected energy goal.
- `country_properties` (dict): Country-specific energy feasibility parameters.
- `json_file_path_country_vs_actions_df` (str): Path to the JSON file containing country-action mappings.

### Returns
- `w2_df` (DataFrame): Weighted scores of different energy actions.

### Usage Example
```python
from RESbased_scenario_generator import calculate_action_values
import json

# Load country properties from JSON
with open("path/to/country_properties.json", "r") as file:
    country_properties = json.load(file)

# Define goal
goal_numeric_value = 3  # Energy self-sufficiency

# Calculate action values
action_values = calculate_action_values(goal_numeric_value, country_properties, "path/to/country_vs_actions.json")

# Display results
print(action_values.head())
```

## 4. goal_vs_country(goal_numeric_value)
Maps energy goals to country-specific feasibility parameters.

### Parameters
- `goal_numeric_value` (int): Numeric identifier for an energy goal.

### Returns
- `dict`: A dictionary mapping goal feasibility parameters for different energy scenarios.

### Usage Example
```python
from RESbased_scenario_generator import goal_vs_country

# Define goal
goal_numeric_value = 3  # Self-sufficiency

# Get country feasibility mapping
goal_mappings = goal_vs_country(goal_numeric_value)

# Print mappings
print(goal_mappings)
```

## 5. get_goal_values(goal_name, json_file_path_goals_vs_actions_df)
Fetches action values related to user-defined energy goals.

### Parameters
- `goal_name` (str): Name of the energy goal.
- `json_file_path_goals_vs_actions_df` (str): Path to the JSON file containing goal-action mappings.

### Returns
- `DataFrame`: A filtered dataset containing action values for the specified goal.

### Usage Example
```python
from RESbased_scenario_generator import get_goal_values

# Define goal
goal_name = "Higher rate of renewable energy"

# Fetch goal values
goal_values = get_goal_values(goal_name, "path/to/goals_vs_actions.json")

# Display results
print(goal_values.head())
```

## 6. baseline_pathway_simple(data, front_data, demand_profile, building_consumption_dict)
Computes baseline energy demand and generation profiles.

### Parameters
- `data` (dict): Energy system and building data.
- `front_data` (dict): User-provided data.
- `demand_profile` (dict): Energy demand profile.
- `building_consumption_dict` (dict): Building energy consumption details.

### Returns
- `dict`: The baseline energy scenario data.

### Usage Example
```python
from RESbased_scenario_generator import baseline_pathway_simple

# Define example input data
data = {...}
front_data = {...}
demand_profile = {...}
building_consumption_dict = {...}

# Compute baseline
baseline = baseline_pathway_simple(data, front_data, demand_profile, building_consumption_dict)

# Display result
print(baseline)
```

## 7. fetch_geojson(geojson_object)
Fetches demand data from external sources based on a provided geoJSON file.

### Parameters
- `geojson_object` (dict): A geoJSON-formatted dataset.

### Returns
- `dict`: Processed geoJSON data with energy demand information.

### Usage Example
```python
from RESbased_scenario_generator import fetch_geojson

# Define example geoJSON object
geojson_object = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {"id": 1},
            "geometry": {"type": "Point", "coordinates": [16.37, 48.21]}
        }
    ]
}

# Fetch demand data
geojson_data = fetch_geojson(geojson_object)

# Print result
print(geojson_data)
```

---

# country_RES_library.py

## 8. country_res_recommendations(country_code)
Retrieves country-specific RES recommendations based on predefined datasets.

### Parameters
- `country_code` (str): The ISO country code.

### Returns
- `dict`: Renewable energy system recommendations for the specified country.

### Usage Example
```python
from country_RES_library import country_res_recommendations

# Get recommendations for Austria
recommendations = country_res_recommendations("AT")

# Display recommendations
print(recommendations)
```
