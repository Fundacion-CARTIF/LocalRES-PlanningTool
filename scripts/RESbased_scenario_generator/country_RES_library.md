# Country RES Library

## Overview
`country_RES_library.py` is a Python module designed to manage country-specific renewable energy scenarios and recommendations. It provides functionalities to create country objects, fetch energy system recommendations, and read structured data from CSV and JSON files for further energy analysis.

This module supports decision-making by offering predefined energy pathways, scenario recommendations, and structured national data integration.

## Features
- **Country Object Management**: Defines a `Country` class to encapsulate country-level energy attributes.
- **RES Recommendations**: Retrieves renewable energy system scenarios based on country-specific settings.
- **CSV Data Handling**: Reads structured energy data from CSV files to build country-specific energy profiles.
- **JSON Data Integration**: Loads scenario recommendations from JSON files for renewable energy decision support.

---

# Classes and Their Methods

## 1. `Country`
Represents a country with its name, country code, and additional energy-related attributes.

### Attributes:
- `name (str)`: Name of the country.
- `country_code (str)`: ISO country code.
- `additional_info (dict)`: Dictionary containing additional attributes dynamically assigned.

### Methods:
- `__str__(self)`: Returns a string representation of the country.
- `get_all_attributes(self)`: Retrieves all attributes of the country as a dictionary.

---

# Functions and Their Functionalities

## 2. `country_res_recommendations(country_code)`
Retrieves predefined renewable energy system recommendations for a given country.

### Parameters:
- `country_code (str)`: The ISO country code.

### Returns:
- `dict`: A dictionary containing the recommended energy actions based on predefined scenarios.

### Functionality:
- Reads country-specific scenario data from a JSON file.
- Matches the country code with available energy scenarios.
- Extracts attributes such as high electrification potential, biomass, solar energy use, and smart heating recommendations.

## 3. `country_library(country_code)`
Reads CSV data and creates a `Country` object with relevant attributes.

### Parameters:
- `country_code (str)`: The ISO country code.

### Returns:
- `tuple`: A dictionary of filtered CSV data and a `Country` object containing the structured information.

### Functionality:
- Loads multiple CSV files containing country-specific energy information.
- Filters the dataset to match the given country code.
- Creates a `Country` object with energy-related attributes derived from the CSV files.

## 4. `assign_country_from_json()`
Assigns a country from a user-defined JSON input file.

### Returns:
- `tuple`: User inputs, a `Country` object, and a dictionary containing recommended scenarios.

### Functionality:
- Reads user input from a JSON file.
- Extracts the country code.
- Calls `country_library()` to build a country-specific dataset.
- Calls `country_res_recommendations()` to fetch predefined energy recommendations.

---

## Conclusion
The `country_RES_library.py` module provides structured country-level energy data and renewable energy system recommendations. It enables seamless integration of country-based energy planning strategies, making it valuable for energy analysts and policymakers.
