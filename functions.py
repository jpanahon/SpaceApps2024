import numpy as np

# Function to calculate the vector that has the starting point at the planet and the end point at the star
def resultantVector(planet, star):
    return np.subtract(star, planet)


# Calculates RA
def phi(vector):
    return np.sign(vector[1])*np.arccos(vector[0]/np.sqrt(vector[0]**2 + vector[1]**2))

# Calculates distance
def distance(vector):
    return np.sqrt(vector[0]**2 + vector[1]**2+ vector[2]**2)

# Calculates DEC
def theta(vector):
    return np.arccos(vector[2]/distance(vector))

