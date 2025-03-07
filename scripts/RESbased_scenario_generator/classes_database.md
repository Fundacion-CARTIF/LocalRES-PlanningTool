# Classes and Object-Oriented Programming in `classes_database.py`

## Overview
`classes_database.py` is a Python module designed to model energy generation, consumption, and efficiency within buildings and communities. It provides structured object-oriented implementations for handling energy assets, calculating consumption, and evaluating energy performance through KPIs. 

This module is crucial for integrating renewable energy sources, optimizing energy efficiency, and managing demand response strategies in urban and industrial settings.

## Features
- **Building and Community Energy Asset Management**: Define and manage energy generation and consumption assets at building and community levels.
- **Energy Input-Output Modeling**: Simulate energy flow within assets based on demand, fuel yields, and operational constraints.
- **Consumption Profiling**: Compute and store energy consumption for heating, cooling, DHW, and electricity systems.
- **Final Energy Calculation**: Aggregate hourly, monthly, and yearly energy data for comprehensive analysis.
- **Key Performance Indicator (KPI) Computation**: Calculate important energy KPIs, including Primary Energy Factors (PEF), CO₂ emissions, and cost assessments.

---

# Classes and Their Methods

## 1. `BuildingEnergyAsset`
Represents an energy asset within a building, including attributes for energy inputs, outputs, and generation system information.

### Attributes:
- `generation_system_id (int)`: ID of the generation system.
- `pmaxmin_scalar (float)`: Minimum capacity scaling factor.
- `pmaxmax_scalar (float)`: Maximum capacity scaling factor.
- `building_asset_context_id (int)`: Context ID related to the building asset.
- `name (str)`: Name of the energy asset.
- `input1 (list)`: Input energy values, e.g., electricity.
- `input2 (list)`: Secondary input energy values.
- `output1 (list)`: Output energy values, e.g., heating demand.
- `output2 (list)`: Secondary output energy values.
- `generation_system_info (dict)`: Information about the generation system.

### Methods:
- `add_PV_profile(self, pvprofile)`: Adds a photovoltaic profile as input.
- `calculate_inputs_and_outputs(self, demand, fuel_yield1, fuel_yield2, type="heat_pump")`: Computes energy inputs and outputs based on demand and fuel yields.
- `add_generation_systems_info(self, Generation_system_info)`: Adds information about the energy generation system.
- `to_dict(self)`: Converts the object to a dictionary for JSON compatibility.

## 2. `CommunityEnergyAsset`
Represents a shared energy asset at the community level, with attributes for generation, input, and output nodes.

### Attributes:
- `generation_system_id (int)`: ID of the generation system.
- `pmaxmin_scalar (float)`: Minimum capacity scaling factor.
- `pmaxmax_scalar (float)`: Maximum capacity scaling factor.
- `input_node_geom (dict)`: Geometric data for the input node.
- `output_node_geom (dict)`: Geometric data for the output node.
- `name (str)`: Name of the community energy asset.
- `input1 (list)`: Input energy values.
- `input2 (list)`: Secondary input energy values.
- `output1 (list)`: Output energy values.
- `output2 (list)`: Secondary output energy values.
- `generation_system_info (dict)`: Information about the generation system.
- `pmax_scalar (float)`: Maximum power scaling factor.

### Methods:
- `add_input1_profile(self, input1_profile)`: Adds an input profile.
- `add_generation_systems_info(self, Generation_system_info)`: Adds information about the energy generation system.
- `add_inputs_ARTELYS(self, inputs_ARTELYS)`: Integrates ARTELYS input data into the model.
- `to_dict(self)`: Converts the object to a dictionary for JSON compatibility.

## 3. `BuildingConsumption`
Represents energy consumption data for a building.

### Attributes:
- `building_consumption_id_temp (int)`: Temporary ID for the building consumption data.
- `heat_consumption (list)`: Hourly heating consumption values.
- `dhw_consumption (list)`: Hourly domestic hot water (DHW) consumption values.
- `elec_consumption (list)`: Hourly electricity consumption values.
- `cool_consumption (list)`: Hourly cooling consumption values.

### Methods:
- `to_dict(self)`: Converts the object to a dictionary format.
- `re_calculate_consumption(self, demand, fuel_yield1, type="heat_consumption")`: Recalculates consumption based on demand and fuel yield.

## 4. `FinalEnergy`
Manages final energy consumption data over different time frames (hourly, monthly, yearly).

### Attributes:
- `id (int)`: Unique ID for the final energy instance.
- `name (str)`: Name of the energy type.
- `final (bool)`: Whether the energy is final energy.
- `_hourly_data (list)`: Hourly energy consumption values.
- `monthly_data (list)`: Monthly energy consumption values.
- `yearly_data (float)`: Total yearly energy consumption.

### Methods:
- `recalculate(self)`: Recalculates monthly and yearly values based on hourly data.
- `calculate_monthly(self, hourly_data)`: Computes monthly data from hourly data.
- `final_energy_to_dic(self)`: Converts the object to a dictionary.
- `add_new_consumption(self, consumption)`: Adds new consumption data.

## 5. `BuildingKPIs`
Calculates Key Performance Indicators (KPIs) for a building's energy consumption and efficiency.

### Attributes:
- `final_energy (FinalEnergy)`: Instance of FinalEnergy for KPI calculations.
- `energy_carrier_name (str)`: Name of the energy carrier.
- `energy_carrier_id (int)`: ID of the energy carrier.
- `pef_tot (float)`: Total Primary Energy Factor.
- `pef_nren (float)`: Non-renewable Primary Energy Factor.
- `pef_ren (float)`: Renewable Primary Energy Factor.
- `f_co2_eq_g_kwh (float)`: CO2 emissions factor (g/kWh).
- `non_h_costs_eur_kwh (float)`: Non-household energy costs (€/kWh).
- `house_costs_eur_kwh (float)`: Household energy costs (€/kWh).

### Methods:
- `calculate_kpis(self)`: Computes various KPIs based on energy consumption data.
- `calculate_monthly(self, hourly_data)`: Converts hourly data into monthly values.
- `to_dict(self)`: Converts KPI data into dictionary format.

---

## Conclusion
The `classes_database.py` module provides a structured way to model energy generation, consumption, and efficiency KPIs. Using classes allows for modular, reusable, and scalable code, making it easier to manage energy-related computations in various scenarios.