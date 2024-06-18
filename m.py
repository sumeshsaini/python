def favorite_planet_position(planets, favorite_planet):
    sorted_distances = sorted(planets.values())
    return sorted_distances.index(favorite_planet) + 1

# Example usage:
planet_distances = {
    "Mercury": 57.9,
    "Venus": 108.2,
    "Earth": 149.6,
    "Mars": 227.9,
    "Jupiter": 778.6
}
favorite_planet = 149.6
position = favorite_planet_position(planet_distances, favorite_planet)
print("Aman's favorite planet position is:", position)
