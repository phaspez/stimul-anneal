import math
import random
from itertools import repeat
from numba import njit

class TraversalPath:
    distance_matrix = []

    def __init__(self, path):
        self.path = path
        self.num_cities = len(path)

    def mutate(self, temperature, city_num):
        iteration = max(round(temperature * city_num), 1)
        for _ in repeat(None, iteration):
            i, j = sorted(random.sample(range(0, self.num_cities), 2))
            self.path[i:j + 1] = reversed(self.path[i:j + 1])

    @classmethod
    def _get_distance(cls, city_a:set, city_b:set) -> float:
        return cls.distance_matrix[city_a[2]-1][city_b[2]-1]

    @classmethod
    def _pre_calculate_distance_matrix(cls, cities):
        num_cities = len(cities)
        cls.distance_matrix = [[0] * num_cities for _ in range(num_cities)]

        for i in range(num_cities):
            for j in range(i+1, num_cities):
                city_a, city_b = cities[i], cities[j]
                dist = math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)
                cls.distance_matrix[city_a[2]-1][city_b[2]-1] = dist
                cls.distance_matrix[city_b[2]-1][city_a[2]-1] = dist

    def get_path_length(self):
        total_length = sum(
            self._get_distance(self.path[i], self.path[i + 1]) for i in range(-1, self.num_cities-1)
        )
        return total_length