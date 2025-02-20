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
```python
res_based_generator_list_technologies(inputs_users)
```
Generates a list of recommended renewable energy technologies based on user goals and country selection, as shown before.
```python
match_actions(action_keys, data)
```
Matches actions from the RES library with input actions based on a predefined key mapping. To do that,     actions_keys_csv_file_path = os.path.join(directory_path, 'action_keys.csv')
    action_keys = pd.read_csv(actions_keys_csv_file_path)  are used
```python
calculate_action_values(goal_numeric_value, country_properties, json_file_path_country_vs_actions_df)
```
Calculates action values using multi-criteria decision analysis (MCDA).
```python
goal_vs_country(goal_numeric_value)
```
Maps energy goals to country-specific feasibility parameters.
```python
get_goal_values(goal_name, json_file_path_goals_vs_actions_df)
```
Fetches action values related to user-defined energy goals.
```python
top_values(df)
```
Ranks actions and selects the top renewable energy solutions based on calculated weights.
```python
baseline_pathway_simple(data, front_data, demand_profile, building_consumption_dict)
```
Computes baseline energy demand and generation profiles.
```python
baseline_pathway_intermediate(data, front_data, geojson_file, demand_profile, building_consumption_dict)
```
Processes geospatial building data to assess energy demand.
```python
calculate_areas(geojson_file)
```
Computes areas and heating demand from geoJSON building footprints.
```python
fetch_geojson(geojson_object)
```
Fetches demand data from external sources based on a provided geoJSON file.
```python
generate_geojson(front_data)
```
Converts input data into a structured geoJSON format.
### Functions from countr_RES_library.py

```python
country_res_recommendations(country_code)
```
Retrieves country-specific RES recommendations based on predefined datasets.
```python
country_library(country_code)
```
Creates a country object containing relevant RES attributes for decision-making.
```python
assign_country_from_json()
```
Loads user inputs from a JSON file and assigns country data accordingly.