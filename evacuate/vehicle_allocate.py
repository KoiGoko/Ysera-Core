import numpy as np

evacuate_population = [12354, 43113, 65314, 89431, 9841, 23421]
population_array = np.array(evacuate_population)
normalized = population_array / np.sum(population_array)

vehicle_count = np.sum(population_array) / 100

vehicle_capacity = [4, 40, 3, 4, 6]
vehicle_array = np.array(vehicle_capacity)
normalized_vehicle = 1 - (vehicle_array / np.sum(vehicle_array))
normalized_vehicle = normalized_vehicle / np.sum(normalized_vehicle)

vehicle_count_array = normalized * vehicle_count

allocated_vehicle = []

for vehicle in vehicle_count_array:
    vehicle1 = vehicle * normalized_vehicle
    sum1 = np.sum(vehicle1)
    allocated_vehicle.append(vehicle1)


print('hello')
