# Classes and Object-Oriented Programming in `classes_database.py`

## Introduction to Classes in Python
Classes are a fundamental concept in object-oriented programming (OOP). They allow us to define blueprints for objects that encapsulate both data and behaviors. In Python, a class is defined using the `class` keyword, and objects (instances of a class) are created by calling the class like a function.

Each class can contain attributes (variables that store data) and methods (functions that define behavior). The special method `__init__` is called a constructor and is used to initialize the attributes of a class when an object is created.

## Overview of `classes_database.py`
The `classes_database.py` module defines several classes related to energy assets, consumption, and performance indicators. These classes facilitate the modeling of energy generation and consumption in buildings and communities.

## Classes and Their Methods

### 1. `BuildingEnergyAsset`
Represents an energy asset within a building, including attributes for energy inputs, outputs, and generation system information.

#### Methods:
- `__init__(self, generation_system_id, pmaxmin_scalar, pmaxmax_scalar, building_asset_context_id, name)`: Initializes an energy asset with given parameters.
- `add_PV_profile(self, pvprofile)`: Adds a photovoltaic profile as input.
- `calculate_inputs_and_outputs(self, demand, fuel_yield1, fuel_yield2, type="heat_pump")`: Computes energy inputs and outputs based on demand and fuel yields.
- `add_generation_systems_info(self, Generation_system_info)`: Adds information about the energy generation system.
- `to_dict(self)`: Converts the object to a dictionary for JSON compatibility.

### 2. `CommunityEnergyAsset`
Represents a shared energy asset at the community level, with attributes for generation, input, and output nodes.

#### Methods:
- `__init__(self, generation_system_id, pmaxmin_scalar, pmaxmax_scalar, input_node_geom, output_node_geom, name)`: Initializes a community energy asset.
- `add_input1_profile(self, input1_profile)`: Adds an input profile.
- `add_generation_systems_info(self, Generation_system_info)`: Adds information about the energy generation system.
- `add_inputs_ARTELYS(self, inputs_ARTELYS)`: Integrates ARTELYS input data into the model.
- `to_dict(self)`: Converts the object to a dictionary for JSON compatibility.

### 3. `BuildingConsumption`
Represents energy consumption data for a building.

#### Methods:
- `__init__(self, building_consumption_id_temp, elec_consumption)`: Initializes a building consumption object with electricity consumption data.
- `to_dict(self)`: Converts the object to a dictionary format.
- `re_calculate_consumption(self, demand, fuel_yield1, type="heat_consumption")`: Recalculates consumption based on demand and fuel yield.

### 4. `FinalEnergy`
Manages final energy consumption data over different time frames (hourly, monthly, yearly).

#### Methods:
- `__init__(self, id)`: Initializes a final energy object.
- `recalculate(self)`: Recalculates monthly and yearly values based on hourly data.
- `calculate_monthly(self, hourly_data)`: Computes monthly data from hourly data.
- `final_energy_to_dic(self)`: Converts the object to a dictionary.
- `add_new_consumption(self, consumption)`: Adds new consumption data.

### 5. `BuildingKPIs`
Calculates Key Performance Indicators (KPIs) for a building's energy consumption and efficiency.

#### Methods:
- `__init__(self, final_energy_instance, kpi_data)`: Initializes a KPI object with energy instance and KPI factors.
- `calculate_kpis(self)`: Computes various KPIs based on energy consumption data.
- `calculate_monthly(self, hourly_data)`: Converts hourly data into monthly values.
- `to_dict(self)`: Converts KPI data into dictionary format.

## Conclusion
The `classes_database.py` module provides a structured way to model energy generation, consumption, and efficiency KPIs. Using classes allows for modular, reusable, and scalable code, making it easier to manage energy-related computations in various scenarios.
