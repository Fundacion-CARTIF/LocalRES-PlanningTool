# **Context Generation for Energy Systems**

## **Overview**
This project provides functionalities for handling energy system recommendations, updating building and community energy assets, and processing energy demand and generation profiles. It is developed as part of a renewable energy optimization framework.

## **Features**
- Grouping and ungrouping buildings based on energy system profiles.
- Handling updates to building energy systems based on recommended actions.
- Calculating peak load distribution curves and energy signatures.
- Interacting with PVGIS for solar and wind energy potential estimation.
- Managing energy asset data, including heating, cooling, DHW, and electricity systems.

---

## **Installation**
### **Prerequisites**
Ensure you have **Python 3.12** installed. Required dependencies include:

- `pandas` (2.2.2)
- `pillow` (10.3.0)
- `spyder` (5.5.1)
- `geopandas` (0.14.3)
- `pvlib`
- `numpy`
- `shapely`

### **Installation using pip**
You can install the required dependencies using:

```sh
pip install pandas pillow spyder geopandas pvlib numpy shapely
```

---

## **License**
This project is licensed under the **GNU General Public License v3.0 (GPLv3)**. You are free to:

✅ Copy, distribute, and modify the software as long as modifications are tracked.  
✅ Include the original license and copyright notices.  
❌ You **cannot** sublicense or hold the authors liable.  

More details: [GNU GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.html)

---

## **Contributing**
We welcome contributions! Please follow these steps:

1. **Fork** the repository.
2. **Create a feature branch** (`git checkout -b feature-branch`).
3. **Commit changes** (`git commit -m "Add new feature"`).
4. **Push to the branch** (`git push origin feature-branch`).
5. **Submit a Pull Request (PR)** for review.

---

## **Contact**
**Author**: Andrea Gabaldon Moreno  
📧 **Email**: angamo1994@gmail.com  
🏢 **Organization**: CARTIF, iciber@cartif.es, manper@cartif.es  

---


## **Usage**

### **Group and Ungroup Buildings**
#### *Grouping buildings by `generation_system_profile_id`*
```python
from context_creation import group_buildings_by_generation_system

context_data = {
    "building_asset_context": [
        {"id": 1, "generation_system_profile_id": 101},
        {"id": 2, "generation_system_profile_id": 102},
        {"id": 3, "generation_system_profile_id": 101},
    ]
}

grouped = group_buildings_by_generation_system(context_data)
print(grouped)
```

#### *Ungrouping buildings to restore the original context*
```python
from context_creation import ungroup_buildings_to_context

ungrouped = ungroup_buildings_to_context(grouped)
print(ungrouped)
```

---

### **Updating Building Systems**
To update the energy system of a building based on recommended actions:

```python
from context_creation import update_building_system

goal = 1  # Example: Higher rate of renewable energy
building_id = 123
building_geom = 500  # in square meters
demandprofile = {
    "heating_demand": [100, 120, 130],  # Example demand profile
    "cooling_demand": [90, 80, 85],
    "dhw_demand": [50, 55, 60],
}
pvprofile = [0.8, 0.9, 0.85]
buildings_generation_system = {
    "heating_system_id": 10,
    "cooling_system_id": 20,
    "dhw_system_id": 30,
    "electricity_system_id": 40,
}
building_energy_asset = []
actions_to_generation_systems = {}  # Load appropriate mappings
action_key = 3  # Example action key

updated_system, new_assets, new_system = update_building_system(
    goal, building_id, building_geom, demandprofile, pvprofile,
    buildings_generation_system, building_energy_asset, actions_to_generation_systems, action_key, None
)

print(updated_system)
print(new_assets)
```

---

### **Handling Community Energy Assets**
#### *Updating community assets with a new system*
```python
from context_creation import update_community_energy_assets

community_node = "Community_Center"
action_key = 15  # Storage system
actions_to_generation_systems = {}  # Provide appropriate mappings
wind_potential_kWh_per_kWp = [0.5, 0.6, 0.55]

updated_community_asset = update_community_energy_assets(
    community_node, action_key, actions_to_generation_systems, wind_potential_kWh_per_kWp
)

print(updated_community_asset)
```


---
## **Peak Load Distribution Curve**
### **Function:**
```python
def peak_load_distribution_curve(demand):
```
### **Description:**
This function calculates the peak load distribution curve by sorting the demand data in descending order. It also determines the capacity required to meet 70% and 90% of the peak demand.

### **Parameters:**
- `demand` (*list*): A list of demand values representing energy consumption over time.

### **Returns:**
- `capacity_70` (*float*): The capacity required to meet 70% of the peak demand.
- `capacity_90` (*float*): The capacity required to meet 90% of the peak demand.
- `sorted_demand` (*list*): The demand values sorted in descending order.

### **Example Usage:**
```python
from context_creation import peak_load_distribution_curve

demand = [100, 150, 200, 180, 220, 210]
capacity_70, capacity_90, sorted_demand = peak_load_distribution_curve(demand)
print(capacity_70, capacity_90, sorted_demand)
```

---

## **Obtain Energy Signature**
### **Function:**
```python
def obtain_energy_signature(outdoor_temperatures, demand, mode):
```
### **Description:**
This function determines the energy signature by analyzing demand based on temperature conditions. It sorts demand data and calculates the peak loads.

### **Parameters:**
- `outdoor_temperatures` (*list*): A list of outdoor temperature readings.
- `demand` (*list*): A list of energy demand values.
- `mode` (*int*): 
  - `0` for heating (considers temperatures below 18°C).
  - `1` for cooling (considers temperatures above 26°C).

### **Returns:**
- `capacity_70` (*float*): Capacity required to meet 70% of peak demand.
- `capacity_90` (*float*): Capacity required to meet 90% of peak demand.
- `sorted_demand` (*list*): The sorted demand values.

### **Example Usage:**
```python
from context_creation import obtain_energy_signature

temperatures = [10, 15, 20, 25, 30]
demand = [100, 200, 150, 80, 50]
mode = 0  # Heating mode

capacity_70, capacity_90, sorted_demand = obtain_energy_signature(temperatures, demand, mode)
print(capacity_70, capacity_90, sorted_demand)
```

---

## **Call PVGIS**
### **Function:**
```python
def call_PVGIS(longitude, latitude, tilt_angle):
```
### **Description:**
This function retrieves solar and wind energy data from PVGIS, returning irradiation values, temperature, wind potential, and solar elevation. For the wind potential an additional function is used, called wind_power(wind_speed). This one takes the wind speed from the PVGIS file, to transform it into power considering a 18 meters height, nominal power of 20 kW, starts functioning at 1.85 m/s  interpolating power for each wind speed in tmy_data['WS10m'].

### **Parameters:**
- `longitude` (*float*): Longitude of the location.
- `latitude` (*float*): Latitude of the location.
- `tilt_angle` (*float*): Tilt angle for solar panel calculations.

### **Returns:**
- `irradiance_dic` (*dict*): Irradiance values for different orientations.
- `pv_profile_in_kWh_kWp` (*list*): Solar PV generation profile.
- `solar_elevation_midday_values` (*pandas.DataFrame*): Midday solar elevation data.
- `T2m` (*list*): 2-meter air temperature values.
- `wind_potential_kWh_per_kWp` (*list*): Wind power generation potential.
- `irradiance_dic_with_tmy_data` (*dict*): Detailed irradiance data including direct, global, and diffuse radiation.

### **Example Usage:**
```python
from context_creation import call_PVGIS

longitude, latitude = -3.7038, 40.4168
tilt_angle = 35

irradiance, pv_profile, solar_elevation, temperatures, wind_potential, irradiance_full = call_PVGIS(
    longitude, latitude, tilt_angle
)

print(pv_profile)
```

---

## **Handle Electricity System**
### **Function:**
```python
def handle_electricity_system(updated_generation_system_profile, new_gen_system_id, energy_systems_catalogue, building_id, building_geom, generation_profile):
```
### **Description:**
Handles the update of electricity generation systems for buildings. It supports adding photovoltaic assets and updating system profiles.

### **Parameters:**
- `updated_generation_system_profile` (*dict*): Dictionary containing the updated system profile.
- `new_gen_system_id` (*int*): ID of the new electricity generation system.
- `energy_systems_catalogue` (*dict*): Dictionary of available energy systems.
- `building_id` (*int*): ID of the building.
- `building_geom` (*float*): Area of the building (m²).
- `generation_profile` (*list*): Solar PV generation profile.

### **Returns:**
- `updated_generation_system_profile` (*dict*): Updated system profile with new electricity settings.
- `new_building_energy_asset_dic` (*dict*): Dictionary containing details of the new energy asset.

### **Example Usage:**
```python
from context_creation import handle_electricity_system

updated_system_profile = {"electricity_system_id": 40}
new_system_id = 83  # Solar PV
energy_catalogue = {}  # Load appropriate energy system data
building_id = 101
building_geom = 500
generation_profile = [0.8, 0.9, 0.85]

updated_profile, new_asset = handle_electricity_system(
    updated_system_profile, new_system_id, energy_catalogue, building_id, building_geom, generation_profile
)

print(updated_profile, new_asset)
```

---

## **Get Centroid**
### **Function:**
```python
def get_centroid(group_of_geoms, target_epsg=4326):
```
### **Description:**
Calculates the geometric centroids of buildings and a community-wide centroid based on input geometries.

### **Parameters:**
- `group_of_geoms` (*dict*): A dictionary where keys are building IDs and values contain geometry and name information.
- `target_epsg` (*int*, default=4326): The EPSG code for coordinate reference systems.

### **Returns:**
- `gdf` (*GeoDataFrame*): A GeoDataFrame containing building geometries and their centroids.
- `community_centroid` (*Point*): The calculated centroid of the entire community.

### **Example Usage:**
```python
from context_creation import get_centroid

group_of_geoms = {
    "1": {"name": "Building 1", "geom": "POINT(10 20)"},
    "2": {"name": "Building 2", "geom": "POINT(15 25)"}
}

gdf, community_centroid = get_centroid(group_of_geoms)
print(community_centroid)
```

---

## **Handle Storage System**
### **Function:**
```python
def handle_storage_system(action_key, actions_to_generation_systems, community_node, energy_systems_catalogue):
```
### **Description:**
Handles the integration of storage systems in the community's energy assets.

### **Parameters:**
- `action_key` (*int*): Action identifier related to storage system implementation.
- `actions_to_generation_systems` (*DataFrame*): A mapping of actions to generation systems.
- `community_node` (*geometry*): The location of the community node.
- `energy_systems_catalogue` (*dict*): A catalogue containing available energy systems.

### **Returns:**
- `new_community_energy_asset_dic` (*dict*): A dictionary containing details of the new storage asset.

---

## **Handle Wind System**
### **Function:**
```python
def handle_wind_system(action_key, actions_to_generation_systems, community_node, wind_potential_kWh_per_kWp, energy_systems_catalogue):
```
### **Description:**
Handles the integration of wind power systems into the community energy assets.

### **Parameters:**
- `action_key` (*int*): Action identifier related to wind system implementation.
- `actions_to_generation_systems` (*DataFrame*): A mapping of actions to generation systems.
- `community_node` (*geometry*): The location of the community node.
- `wind_potential_kWh_per_kWp` (*list*): The wind power generation potential.
- `energy_systems_catalogue` (*dict*): A catalogue containing available energy systems.

### **Returns:**
- `new_community_energy_asset_dic` (*dict*): A dictionary containing details of the new wind energy asset.

---

## **Handle CHP System**
### **Function:**
```python
def handle_chp_system(action_key, actions_to_generation_systems, community_node, energy_systems_catalogue):
```
### **Description:**
Handles the implementation of Combined Heat and Power (CHP) systems.

### **Parameters:**
- `action_key` (*int*): Action identifier related to CHP system implementation.
- `actions_to_generation_systems` (*DataFrame*): A mapping of actions to generation systems.
- `community_node` (*geometry*): The location of the community node.
- `energy_systems_catalogue` (*dict*): A catalogue containing available energy systems.

### **Returns:**
- `new_community_energy_asset_dic` (*dict*): A dictionary containing details of the new CHP system.

---

## **Add New Building Energy Asset System**
### **Function:**
```python
def add_new_building_energy_asset_system(system_id, energy_systems_catalogue, capacity, building_id, system, demand):
```
### **Description:**
Adds a new energy asset for a building.

### **Parameters:**
- `system_id` (*int*): The ID of the new system.
- `energy_systems_catalogue` (*dict*): The catalogue of available energy systems.
- `capacity` (*float*): The capacity of the system.
- `building_id` (*int*): The ID of the building.
- `system` (*str*): The type of system (heating, cooling, DHW, electricity).
- `demand` (*list*): The demand profile.

### **Returns:**
- `new_building_energy_asset_dic` (*dict*): New energy asset details.
- `filtered_systems_info` (*dict*): Updated system information.

---

## Handle DHW System
```python
def handle_dhw_system(updated_generation_system_profile, new_gen_system_id, dhw_demand, energy_systems_catalogue, building_id):
    """
    Handles updates to the Domestic Hot Water (DHW) system in buildings.

    Parameters:
    updated_generation_system_profile (dict): Dictionary containing the updated system profile.
    new_gen_system_id (int): ID of the new DHW generation system.
    dhw_demand (list): List of DHW demand values.
    energy_systems_catalogue (dict): Catalogue of available energy systems.
    building_id (int): ID of the building.

    Returns:
    updated_generation_system_profile (dict): Updated system profile with new DHW settings.
    new_building_energy_asset_dic (dict): Dictionary containing details of the new DHW energy asset.
    """
```

## Handle Cooling System
```python
def handle_cooling_system(updated_generation_system_profile, new_gen_system_id, cooling_demand, energy_systems_catalogue, building_id):
    """
    Handles updates to the cooling system in buildings.

    Parameters:
    updated_generation_system_profile (dict): Dictionary containing the updated system profile.
    new_gen_system_id (int): ID of the new cooling system.
    cooling_demand (list): List of cooling demand values.
    energy_systems_catalogue (dict): Catalogue of available energy systems.
    building_id (int): ID of the building.

    Returns:
    updated_generation_system_profile (dict): Updated system profile with new cooling settings.
    new_building_energy_asset_dic (dict): Dictionary containing details of the new cooling energy asset.
    """
```

## **Create Grid Community Asset**
### **Function:**
```python
def create_grid_community_asset(community_centroid):
```
### **Description:**
Creates a grid energy asset at the community level.

### **Parameters:**
- `community_centroid` (*geometry*): The centroid of the community.

### **Returns:**
- `grid` (*dict*): Dictionary containing grid asset details.

---

## **Convert Geometries to Strings**
### **Function:**
```python
def convert_geometries_to_strings(geom):
```
### **Description:**
Converts geometric objects to their WKT string representation.

### **Parameters:**
- `geom` (*geometry*): A geometric object.

### **Returns:**
- `new_geom` (*str*): The WKT representation of the geometry.

---

## **Update Building Consumption**
### **Function:**
```python
def update_building_consumption(temp_id, demandprofile, building_asset_context):
```
### **Description:**
Updates the energy consumption data for a building based on the demand profile and system configurations.

### **Parameters:**
- `temp_id` (*int*): Temporary ID for the building.
- `demandprofile` (*dict*): Energy demand profiles for electricity, heating, cooling, and DHW.
- `building_asset_context` (*dict*): The building's asset context.

### **Returns:**
- `updated_building_dic` (*dict*): Updated energy consumption data.

---
