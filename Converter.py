
class Converter:
    @staticmethod
    def convert_length(value, unit_from, unit_to):
        conversion_factors = {
            'meter': 1,
            'kilometer': 1000,
            'centimeter': 0.01,
            'millimeter': 0.001,
        }
       
        if unit_from in conversion_factors and unit_to in conversion_factors:
            value_in_meters = float(value) * conversion_factors[unit_from]
            converted_value = value_in_meters / conversion_factors[unit_to]
            return converted_value
        else:
            return 'Invalid unit'   
        
    def convert_weight(value, unit_from, unit_to):
        conversion_factors = {
            'gram': 1,
            'kilogram': 1000,
            'pound': 453.592,
            'ounce': 28.3495,
        }
        if unit_from in conversion_factors and unit_to in conversion_factors:
            value_in_grams = float(value) * conversion_factors[unit_from]
            converted_value = value_in_grams / conversion_factors[unit_to]
            return converted_value
        else:
            return 'Invalid unit'
        
    def convert_temperature(value, unit_from, unit_to):
        conversion_factors = {
            'celsius': 1,
            'fahrenheit': 1.8,
            'kelvin': 1,
        }
        if unit_from in conversion_factors and unit_to in conversion_factors:
            if unit_from == 'celsius' and unit_to == 'fahrenheit':
                converted_value = (float(value) * conversion_factors[unit_from]) + 32
            elif unit_from == 'fahrenheit' and unit_to == 'celsius':
                converted_value = (float(value) - 32) / conversion_factors[unit_from]
            elif unit_from == 'celsius' and unit_to == 'kelvin':
                converted_value = float(value) + 273.15
            elif unit_from == 'kelvin' and unit_to == 'celsius':
                converted_value = float(value) - 273.15
            else:
                converted_value = float(value) * conversion_factors[unit_from] / conversion_factors[unit_to]
            return converted_value  
       
        
        