# Key Performance Indicators (KPI) Module: `KPI_module.py`

## Overview
`KPI_module.py` is a Python module designed to compute Key Performance Indicators (KPIs) related to energy consumption, peak demands, and environmental impact. It processes energy demand profiles and evaluates metrics such as total primary energy consumption, peak electricity and heating demand, and CO₂ emissions.

This module is integral to assessing energy efficiency, sustainability, and user-friendly comparisons of energy consumption with daily activities like TV watching, streaming, and electric vehicle charging.

## Features
- **Peak Demand Calculation**: Determines maximum electricity and heating demand.
- **Primary Energy Estimation**: Computes total primary energy consumption.
- **Citizen-Oriented KPIs**: Converts energy consumption into relatable comparisons (TV hours, battery charges, pizza consumption, etc.).
- **Scenario-Based Evaluations**: Assesses the energy impact of different building and system configurations.

---

# Functions and Their Functionalities

## 1. `kpi_peak_heat_demand(demand_profile)`
Calculates the peak heat demand (space heating, cooling, and DHW demand) from the demand profile.

### Parameters:
- `demand_profile (list or dict)`: A dataset containing energy demand values.

### Returns:
- `float`: Maximum peak heat demand in MWh.

---

## 2. `kpi_peak_electricity_demand(demand_profile)`
Calculates the peak electricity demand from the demand profile.

### Parameters:
- `demand_profile (list or dict)`: A dataset containing electricity demand values.

### Returns:
- `float`: Maximum peak electricity demand in MWh.

---

## 3. `total_primary_energy_function(data, building_consumption_dict)`
Computes the total primary energy consumption based on the energy consumption of buildings.

### Parameters:
- `data (dict)`: Building statistics profile, including energy carrier production.
- `building_consumption_dict (dict)`: Energy consumption details for each system (electricity, heating, cooling, DHW).

### Returns:
- `tuple`: Total primary energy consumption in kWh and MWh.

---

## 4. `kpi_ctz_factors()`
Defines factors for calculating citizen KPIs (e.g., TV hours, car charges, CO₂ savings).

### Returns:
- `dict`: A dictionary with energy-saving and CO₂ emission reduction factors.

---

## 5. `kpi_scenario_objective(front_data)`
Calculates the number of buildings (or members) in a scenario based on input data.

### Parameters:
- `front_data (dict)`: Contains information about the buildings in the scenario.

### Returns:
- `int`: The number of buildings/members in the energy scenario.

---

## 6. `tv_h(citizen_kpis_factors, total_primary_energy)`
Computes the equivalent TV watching hours for the energy consumed.

### Parameters:
- `citizen_kpis_factors (dict)`: Dictionary of predefined conversion factors.
- `total_primary_energy (float)`: Total primary energy in kWh.

### Returns:
- `float`: Equivalent TV hours.

---

## 7. `battery_charges(citizen_kpis_factors, total_primary_energy)`
Estimates how many times a battery could be fully charged using the total consumed energy.

### Parameters:
- `citizen_kpis_factors (dict)`: Dictionary of predefined conversion factors.
- `total_primary_energy (float)`: Total primary energy in kWh.

### Returns:
- `float`: Number of battery charges.

---

## 8. `trees_number(citizen_kpis_factors, total_co2)`
Calculates the number of trees needed to offset the CO2 emissions generated.

### Parameters:
- `citizen_kpis_factors (dict)`: Dictionary of predefined conversion factors.
- `total_co2 (float)`: Total CO2 emissions in kg.

### Returns:
- `float`: Number of trees required for CO2 offset.

---

## 9. `save_to_csv(...)`
Saves building energy consumption and calculated KPI data into a CSV file.

### Parameters:
- `building_consumption_dict (dict)`: Energy consumption per system type.
- `demand_profile (dict)`: Energy demand data.
- `total_primary_energy_MWh (float)`: Total primary energy in MWh.
- `KPI_peak_heat_demand (float)`: Peak heat demand.
- `KPI_peak_elec_demand (float)`: Peak electricity demand.
- `num_members (int)`: Number of members in the energy scenario.
- `TV_h, streaming_h, Pizza_h, Battery_charges, ElCar_charges, Trees_number, streaming_emissionhours, ICV_km, Wine_bottles (float)`: Various KPIs.

### Returns:
- `pandas.DataFrame`: DataFrames containing KPI results and building energy consumption.

---

## Conclusion
The `KPI_module.py` module is an essential tool for evaluating energy efficiency, demand peaks, and sustainability impacts. By offering structured calculations and relatable comparisons, it enhances decision-making for renewable energy projects and policy assessments.
