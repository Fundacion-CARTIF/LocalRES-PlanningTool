# Key Performance Indicators (KPI) Calculation: `key_performance_indicators.py`

## Overview
`key_performance_indicators.py` is a Python module that calculates detailed energy-related Key Performance Indicators (KPIs) for buildings and communities. It processes energy consumption data, evaluates energy efficiency, and provides sustainability insights by integrating renewable energy self-sufficiency, CO₂ emissions, and economic costs.

This module ensures accurate performance assessment and supports energy transition strategies by offering scenario-based evaluations.

## Features
- **Self-Consumption and Self-Sufficiency Calculation**: Determines on-site renewable energy utilization.
- **Primary Energy and CO2 Emissions**: Evaluates total energy consumption and carbon footprint.
- **Building and Community-Level KPIs**: Aggregates performance metrics for both individual buildings and energy communities.
- **Comparison Metrics for Citizens**: Converts energy data into relatable comparisons (e.g., TV hours, battery charges, wine bottle production).
- **Demand and Consumption Analysis**: Computes energy demand for heating, cooling, DHW, and electricity.

---

# Functions and Their Functionalities

## 1. `handle_demand_profile(building_asset_context, generation_system_profile, consumption_profile)`
Processes demand profiles for buildings, ensuring accurate energy demand calculations based on system efficiencies.

### Parameters:
- `building_asset_context (dict)`: Contains building-related energy attributes.
- `generation_system_profile (dict)`: Defines energy generation system parameters.
- `consumption_profile (dict)`: Stores energy consumption data for different systems.

### Returns:
- `dict`: A dictionary containing the computed demand profile.

---

## 2. `calculate_self_consumption(total_electricity_use, total_PV)`
Computes the amount of locally generated electricity that is self-consumed within the building or community.

### Parameters:
- `total_electricity_use (list)`: List of total electricity demand values.
- `total_PV (list)`: List of PV energy generation values.

### Returns:
- `list`: Self-consumed electricity values.

---

## 3. `calculate_grid_consumption(total_electricity_use, self_consumption)`
Determines the electricity drawn from the grid after accounting for self-consumed PV energy.

### Parameters:
- `total_electricity_use (list)`: Electricity demand values.
- `self_consumption (list)`: Self-consumed electricity values.

### Returns:
- `list`: Electricity demand met by the grid.

---

## 4. `calculate_building_indicators(consumption_profile, generation_system_profile, building_energy_asset, timestep_count)`
Evaluates building-level energy indicators such as self-sufficiency, self-consumption, and final energy consumption.

### Parameters:
- `consumption_profile (dict)`: Building's energy consumption data.
- `generation_system_profile (dict)`: Installed energy systems.
- `building_energy_asset (list)`: List of energy assets installed in the building.
- `timestep_count (int)`: Number of time steps (e.g., 8760 for hourly data).

### Returns:
- `tuple`: Contains self-consumption, total energy use, final energy demand, and KPIs.

---

## 5. `get_totals_per_building(KPIs, timestep_count, final_energy)`
Aggregates energy performance metrics for each building, including primary energy consumption and CO₂ emissions.

### Parameters:
- `KPIs (dict)`: Key performance indicators of the building.
- `timestep_count (int)`: Number of time steps.
- `final_energy (dict)`: Final energy data per carrier.

### Returns:
- `tuple`: Contains total primary energy, CO₂ emissions, and household costs.

---

## 6. `recalculate_indicators(community_context)`
Recomputes energy KPIs for an entire community by aggregating individual building results.

### Parameters:
- `community_context (dict)`: Contains information on buildings and energy systems in the community.

### Returns:
- `tuple`: Citizen-oriented KPIs and aggregated demand profiles.

---

## 7. `get_indicators_from_baseline(front_data, data, building_consumption_dict, demand_profile)`
Extracts and calculates baseline KPIs before energy system modifications.

### Parameters:
- `front_data (dict)`: User interface data.
- `data (dict)`: Contains building statistics and system information.
- `building_consumption_dict (dict)`: Energy consumption per system type.
- `demand_profile (dict)`: Demand profiles for energy systems.

### Returns:
- `dict`: Contains citizen-oriented KPIs for the baseline scenario.

---

## Conclusion
The `key_performance_indicators.py` module plays a crucial role in evaluating building and community energy performance. By integrating demand profiles, renewable energy utilization, and sustainability indicators, it facilitates informed decision-making for energy-efficient urban planning.
