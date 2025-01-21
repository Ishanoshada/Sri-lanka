# Srilanka

The `srilanka` package provides data and utility functions to work with information about Sri Lanka, including its provinces, districts, cities, and divisional secretariats.

## Installation

```sh
pip install srilanka
```

## Usage

```python
from srilanka import SriLanka

# Access core data
info = SriLanka.sri_lanka_info
provinces = SriLanka.sri_lanka_provinces
districts = SriLanka.sri_lanka_districts
cities = SriLanka.sri_lanka_cities
divisional = SriLanka.sri_lanka_divisional


```

<!-- # Example usage
province = SriLanka.get_province_by_name("Western")
districts = SriLanka.get_districts_by_province_name("Western")
cities = SriLanka.get_cities_by_district_name("Colombo") -->

## Available Data

- `sri_lanka_info`: General information about Sri Lanka
- `sri_lanka_provinces`: List of provinces
- `sri_lanka_districts`: List of districts
- `sri_lanka_cities`: List of cities
- `sri_lanka_divisional`: List of divisional secretariats
<!-- 
## Methods

### Location Queries
- `get_province_by_name(name)`: Get province by name
- `get_district_by_name(name)`: Get district by name
- `get_divisional_by_name(name)`: Get divisional secretariat by name

### Hierarchical Queries
- `get_districts_by_province_name(name)`: Get districts in province
- `get_cities_by_district_name(name)`: Get cities in district
- `get_province_by_district_name(name)`: Get province of district
- `get_province_by_divisional_name(name)`: Get province of divisional secretariat

### ID-based Queries
- `get_province_by_id(id)`
- `get_district_by_id(id)`
- `get_divisional_by_id(id)`
- `get_districts_by_province_id(id)`
- `get_cities_by_district_id(id)`
- `get_cities_by_province_id(id)`

### Data Connections
- `connect_province_district()`
- `connect_district_divisional()`
- `connect_divisions_to_districts_and_provinces()` -->

## License

MIT License - see [LICENSE](LICENSE)
