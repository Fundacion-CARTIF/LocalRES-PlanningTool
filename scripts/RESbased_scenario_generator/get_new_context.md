# Context Generation Module: `get_new_context.py`

## Overview
`get_new_context.py` is a Python module designed to modify and update energy system contexts based on recommended renewable energy actions. It integrates multiple functionalities, including:
- Assigning unique IDs to building and community energy assets.
- Removing duplicate systems in an energy context.
- Generating updated contexts based on predefined energy goals and recommended actions.
- Fetching geospatial and demand-related energy data to adjust energy systems accordingly.

This module is a critical component for energy planning, particularly in renewable energy transition scenarios where different technologies and strategies must be applied dynamically.

## Features
- **Context Modification**: Updates the energy context of buildings and communities based on predefined renewable energy goals.
- **Incremental ID Assignment**: Ensures unique IDs for community and building energy assets.
- **Duplicate Removal**: Identifies and removes redundant energy systems from a given context.
- **Scenario-Based Adjustments**: Adapts energy systems dynamically based on selected goals.
- **Integration with PVGIS and Demand Profiles**: Retrieves irradiance, temperature, and demand profiles for location-based energy adjustments.

---

# Functions and Their Functionalities

## 1. `assign_incremental_ids_to_community_assets(community_energy_asset)`
Assigns unique incremental IDs to community energy assets, ensuring proper organization of energy system data.

### Parameters:
- `community_energy_asset (list)`: List of community energy assets.

### Returns:
- `list`: Updated list of community energy assets with unique IDs assigned.

---

## 2. `assign_incremental_ids(building_asset_context)`
Assigns unique incremental IDs to building energy assets within a context.

### Parameters:
- `building_asset_context (list)`: List of building assets within the energy context.

### Returns:
- `list`: Updated list of building assets with unique IDs assigned.

---

## 3. `asset_exists(community_context, new_gen_system_id)`
Checks if an energy asset with a specific generation system ID already exists in the community context.

### Parameters:
- `community_context (dict)`: Dictionary containing community energy system information.
- `new_gen_system_id (int)`: Generation system ID to check.

### Returns:
- `bool`: `True` if the asset exists, otherwise `False`.

---

## 4. `remove_duplicates(old_systems, assets_list)`
Removes duplicate energy systems from a list of assets.

### Parameters:
- `old_systems (dict)`: Dictionary containing existing energy system IDs.
- `assets_list (list)`: List of energy assets in the building context.

### Returns:
- `list`: Filtered list of energy assets with duplicates removed.

---

## 5. `resbased_generator_context_creation(goal, community_context, recommendations_dic)`
Modifies the energy systems of buildings and communities based on recommended actions for a given scenario.

### Parameters:
- `goal (int)`: An integer representing the selected renewable energy goal.
- `community_context (dict)`: Input context representing the energy community.
- `recommendations_dic (dict)`: Dictionary containing recommended actions and corresponding IDs.

### Returns:
- `dict`: Updated community context with modified building systems and new energy assets.

### Functionality:
- Retrieves geospatial and demand data for contextual modifications.
- Updates generation system profiles in response to recommended actions.
- Integrates new energy systems into the existing context.
- Removes redundant or conflicting energy assets.
- Ensures a structured and optimized energy system for the given goal.

---

## Conclusion
The `get_new_context.py` module plays a vital role in energy system adaptation, allowing dynamic modifications of community and building energy assets based on renewable energy strategies. This module enhances energy planning by integrating geospatial, demand-based, and policy-driven changes into a structured and scalable framework.
