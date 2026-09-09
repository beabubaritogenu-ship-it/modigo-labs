def count_unique_coordinates(coordinates):
    unique = []
    for coord in coordinates:
        if coord not in unique:
            unique.append(coord)
    return len(set(unique))