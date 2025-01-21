from .data import provinces, districts, info
from .data2 import cities,divisional_into,divisional_into2

# Ensure data is properly loaded
provinces = provinces
districts = districts
cities = cities if cities else []  # Ensure cities is at least an empty list
divisional = divisional_into + divisional_into2

class SriLanka:
    sri_lanka_info = info
    sri_lanka_provinces = provinces
    sri_lanka_districts = districts
    sri_lanka_cities = cities  
    sri_lanka_divisional = divisional

    