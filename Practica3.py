def roman_to_int(roman):
    # Diccionario que mapea los números romanos a sus valores
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Recorremos el string de derecha a izquierda
    for char in reversed(roman):
        value = roman_values[char]
        # Si el valor actual es menor que el valor previo, restamos, de lo contrario sumamos
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

# Ejemplo de uso
roman_number = "MCMXCIV"  # Ejemplo: 1994
arabic_number = roman_to_int(roman_number)
print(f"El número romano {roman_number} es {arabic_number}")
