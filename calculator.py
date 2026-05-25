def hitung(operator, number1, number2):
    if operator == 'penambahan':
        return number1 + number2
    elif operator == 'pengurangan':
        return number1 - number2
    elif operator == 'perkalian':
        return number1 * number2
    elif operator == 'pembagian':
        return number1 / number2
    return None
