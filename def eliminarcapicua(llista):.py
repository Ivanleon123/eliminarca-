def eliminarcapicua(llista):
    """Elimina el primer i l'últim element d'una llista i retorna la nova llista."""
    if len(llista) <= 2:
        return []  # Retorna una llista buida si la llista original té 2 o menys elements
    return llista[1:-1]  # Retorna la subllista sense el primer i l'últim element

# Proves de la funció
print(eliminarcapicua([1, 2, 3, 4, 5]))  # Retorna [2, 3, 4]
print(eliminarcapicua(['a', 'b', 'c', 'd']))  # Retorna ['b', 'c']
print(eliminarcapicua([10, 20]))  # Retorna []
print(eliminarcapicua(['x']))  # Retorna []
print(eliminarcapicua([]))  # Retorna []