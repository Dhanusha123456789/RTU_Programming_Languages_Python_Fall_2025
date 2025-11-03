"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# TODO: Create the datasets - up to you to fill in the data
temperatures = [16.5, 17.2, 18.0, 19.1, 18.4, 17.9, 16.8]  # one week (7 days)
city_population = {
    "Riga": 632614,
    "Daugavpils": 82425,
    "Liepaja": 68771,
    "Jelgava": 54212,
    "Jurmala": 49149,
}

# TODO: Compute aggregates
average_temperature = None
if temperatures:
    average_temperature = sum(temperatures) / len(temperatures)

total_population = sum(city_population.values()) if city_population else 0

largest_city, largest_population = (None, 0)
smallest_city, smallest_population = (None, 0)
if city_population:
    largest_city, largest_population = max(city_population.items(), key=lambda x: x[1])
    smallest_city, smallest_population = min(
        city_population.items(), key=lambda x: x[1]
    )

# TODO: Print results
print("Weekly temperatures:", temperatures)
if average_temperature is not None:
    print(f"Average temperature: {average_temperature:.2f} °C")
else:
    print("Average temperature: N/A")

if largest_city is not None:
    print(f"Largest city: {largest_city} — {largest_population:,} inhabitants")
else:
    print("Largest city: N/A")

if smallest_city is not None:
    print(f"Smallest city: {smallest_city} — {smallest_population:,} inhabitants")
else:
    print("Smallest city: N/A")

print(f"Total population: {total_population:,} inhabitants")
